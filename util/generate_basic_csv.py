import os
import sys
import time
import json
import pandas as pd

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

from util.common_util import get_contact_html_data

# 安心投
an_xin_tou_project_type = 104046
an_xin_tou_total_record = 16
# 自助投
zi_zhu_tou_project_type = 104043
zi_zhu_tou_total_record = 18


def generate_csv(total_record, project_type):
    """
    生成安心投自助投csv文件
    :param total_record:总条数
    :param project_type:投资类型
    :return:
    """
    page_size = 6
    total_page_num = int((int(total_record) + page_size - 1) / page_size)

    index = ['Name', 'InvestId', 'ProjectId', 'ProjectType', 'ReInvestType', 'AssetType', 'InvestMode', 'TotalCount',
             'Amount',
             'AccruedRevenue', 'InvestDate']
    super_df = pd.DataFrame(columns=index)
    for page_no in range(total_page_num):
        curr_page_no = page_no + 1
        # 毫秒级时间戳
        timestamp = int(round(time.time() * 1000))
        url = 'https://www.ppmoney.com/stepup/InvestProjectList?type=1&pageIndex=' + str(
            curr_page_no) + '&pageSize=' + str(
            page_size) + '&projectType=' + str(project_type) + '&_=' + str(timestamp)
        result = get_contact_html_data(url)
        json_data = json.loads(result[0])
        for sub_data in json_data['Data']['Rows']:
            credit_url = 'https://www.ppmoney.com/stepup/CreditRightList?id=' + str(
                sub_data['InvestId']) + '&pageIndex=1&pageSize=6&projectType=' + str(
                sub_data['ProjectType']) + '&_=' + str(timestamp)
            credit_result = get_contact_html_data(credit_url)
            credit_json_data = json.loads(credit_result[0])
            total_count = credit_json_data['Data']['TotalCount']

            sub_array = [sub_data['Name'], sub_data['InvestId'], sub_data['ProjectId'], sub_data['ProjectType'],
                         sub_data['ReInvestType'], sub_data['AssetType'], sub_data['InvestMode'], total_count,
                         sub_data['Amount'],
                         sub_data['AccruedRevenue'], sub_data['InvestDate']]
            sub_df = pd.DataFrame(sub_array, index=index)
            super_df = super_df.append(sub_df.T)

    if project_type == an_xin_tou_project_type:
        file_name = '安心投.csv'
    elif project_type == zi_zhu_tou_project_type:
        file_name = '自助投.csv'
    super_df.reset_index(drop=True).to_csv(file_name, encoding='utf-8-sig')


generate_csv(an_xin_tou_total_record, an_xin_tou_project_type)
generate_csv(zi_zhu_tou_total_record, zi_zhu_tou_project_type)
