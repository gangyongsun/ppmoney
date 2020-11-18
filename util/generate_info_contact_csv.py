import os
import sys
import json
import pandas as pd
import time
import csv

from util.common_util import get_contact_html_data
from util.common_util import mkdir

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

import config.config as CONFIG

credit_url_1 = CONFIG.credit_right_basic_url
credit_url_2 = CONFIG.credit_page_index
credit_url_3 = CONFIG.credit_page_size
credit_url_4 = CONFIG.credit_project_type

info_url_1 = CONFIG.borrower_info_basic_url
info_url_2 = CONFIG.borrower_info_prj_id
info_url_3 = CONFIG.borrower_info_amount

cat_url_1 = CONFIG.borrower_contact_basic_url
cat_url_2 = CONFIG.borrower_contact_asset_id
cat_url_3 = CONFIG.borrower_contact_share_id
cat_url_4 = CONFIG.borrower_contact_share_type
cat_url_5 = CONFIG.borrower_contact_project_type
cat_url_6 = CONFIG.borrower_contact_asset_type

# 债权明细配置信息文件
credit_csv_file = CONFIG.credit_csv_file
# 总配置信息（需要用户自己收集）
csv_file = csv.reader(open(credit_csv_file, 'r', encoding='utf-8-sig'))

# 每页条数（最大100，再调高无用）
pageSize = 100


def generate_credit_csv(credit_generated_csv_folder):
    """
    生成债权明细出借人csv文件，用于程序获取数据
    :return:
    """
    for line_data in csv_file:
        name = line_data[0]
        totalRecord = line_data[1]
        totalPageNum = (int(totalRecord) + pageSize - 1) / pageSize

        # 点开【查看债权明细】弹出页面，调试拿到的URL
        id_value = line_data[2]
        project_type_value = line_data[3]

        # 需要单独配置prjId
        prjId = line_data[4]

        # 需要单独配置investId、type、assetType
        investId = line_data[5]
        _type = line_data[6]
        assetType = line_data[7]

        colunms_values = ['AssetId', 'SharId', 'Amount', 'AssetCode', 'Debtor', 'LoanAmount', 'TotalPeriodCount',
                          'RepaymentCount',
                          'Status', 'BusinessType', 'RecvedAmt', 'IsFirst', 'ProductCode', 'Publisher', 'BorrowerCode',
                          'Name',
                          'ProjectType', 'borrower_info_url', 'borrower_contact_url']
        # 每条记录对应一个csv文件，这是相应的dataframe
        result_data = pd.DataFrame(columns=colunms_values)
        for i in range(int(totalPageNum)):
            page_index = i + 1
            # 毫秒级时间戳
            timestamp = int(round(time.time() * 1000))
            # 组合【查看债权明细】弹出页面的URL
            url = credit_url_1 + str(id_value) + credit_url_2 + str(page_index) + credit_url_3 + str(
                pageSize) + credit_url_4 + str(project_type_value) + CONFIG.credit_timestamp + str(timestamp)

            # 抓取json数据
            result_array = get_contact_html_data(url)
            # 获得json字符串
            json_content = result_array[0]

            # json转dict
            dict_data = json.loads(json_content)

            # 拿到相要的数据，是list类型
            list_info = dict_data['Data']['Rows']

            new_list_info = []

            # 遍历list获取每个出借人的信息
            for item in list_info:
                # 需要
                asset_id = item['AssetId']
                # 需要
                shar_id = item['SharId']
                # 需要
                amount = item['Amount']
                # 需要
                project_type = item['ProjectType']
                # 出借人信息完整URL
                borrower_info_url = info_url_1 + asset_id + info_url_2 + str(prjId) + info_url_3 + str(amount)
                # print(borrower_info_url)
                item['borrower_info_url'] = borrower_info_url

                # 出借人合同完整URL
                borrower_contact_url = cat_url_1 + str(
                    investId) + cat_url_2 + asset_id + cat_url_3 + shar_id + cat_url_4 + str(_type) + cat_url_5 + str(project_type) + cat_url_6 + str(assetType)
                # print(borrower_contact_url)
                item['borrower_contact_url'] = borrower_contact_url

                new_list_info.append(item)
            # 子df
            credit_df = pd.DataFrame(new_list_info)
            # 合并的df
            result_data = result_data.append(credit_df, ignore_index=True)

            mkdir(credit_generated_csv_folder)
            result_data.to_csv(credit_generated_csv_folder + '/' + name + '.csv', encoding='utf_8_sig')
