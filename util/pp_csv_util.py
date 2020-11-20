#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import pandas as pd
from itertools import islice

from util.common_util import get_html_data
from util.common_util import format_time
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


def generate_basic_csv(total_record, project_type, target_folder):
    """
    生成安心投、自助投基础csv文件
    :param total_record:总条数
    :param project_type:投资类型
    :param target_folder:csv保存目录
    :return:
    """
    if total_record != 0:
        page_size = 6
        total_page_num = int((int(total_record) + page_size - 1) / page_size)

        index = ['Name', 'InvestId', 'ProjectId', 'ProjectType', 'ReInvestType', 'AssetType', 'InvestMode', 'TotalCount', 'Amount', 'AccruedRevenue', 'InvestDate']
        super_df = pd.DataFrame(columns=index)
        for page_no in range(total_page_num):
            curr_page_no = page_no + 1
            # 毫秒级时间戳
            timestamp = int(round(time.time() * 1000))
            url = 'https://www.ppmoney.com/stepup/InvestProjectList?type=1&pageIndex=' + str(curr_page_no) + '&pageSize=' + str(page_size) + '&projectType=' + str(project_type) + '&_=' + str(timestamp)
            result = get_html_data(url)
            json_data = json.loads(result[0])
            for sub_data in json_data['Data']['Rows']:
                credit_url = 'https://www.ppmoney.com/stepup/CreditRightList?id=' + str(sub_data['InvestId']) + '&pageIndex=1&pageSize=6&projectType=' + str(sub_data['ProjectType']) + '&_=' + str(timestamp)
                credit_result = get_html_data(credit_url)
                credit_json_data = json.loads(credit_result[0])
                total_count = credit_json_data['Data']['TotalCount']
                invest_date_time = format_time(sub_data['InvestDate'], "%Y-%m-%d %H:%M", "%Y-%m-%d-%H-%M")
                sub_array = [sub_data['Name'] + invest_date_time, sub_data['InvestId'], sub_data['ProjectId'], sub_data['ProjectType'], sub_data['ReInvestType'], sub_data['AssetType'], sub_data['InvestMode'], total_count,
                             sub_data['Amount'], sub_data['AccruedRevenue'], sub_data['InvestDate']]
                sub_df = pd.DataFrame(sub_array, index=index)
                super_df = super_df.append(sub_df.T, ignore_index=True)

        mkdir(target_folder)
        if project_type == CONFIG.an_xin_tou_project_type:
            file_name = target_folder + '/安心投.csv'
        elif project_type == CONFIG.zi_zhu_tou_project_type:
            file_name = target_folder + '/自助投.csv'
        super_df.to_csv(file_name, encoding='utf-8-sig')


def generate_credit_csv(basic_csv_file, target_folder):
    """
    生成债权明细出借人csv文件，用于程序获取数据
    :param basic_csv_file: 基础CSV文件
    :param target_folder: 目标文件夹
    :return:
    """
    # 每页条数（最大100，再调高无用）
    page_size = 100
    for line_data in islice(basic_csv_file, 1, None):
        name = line_data[1]
        total_record = line_data[8]
        total_page_num = (int(total_record) + page_size - 1) / page_size

        # 点开【查看债权明细】弹出页面，调试拿到的URL
        id_value = line_data[2]
        invest_id = line_data[2]
        project_id = line_data[3]
        project_type_value = line_data[4]
        _type = line_data[5]
        asset_type = line_data[6]

        columns_values = ['Amount', 'Debtor', 'LoanAmount', 'borrower_info_url', 'borrower_contact_url', 'borrower_contact_url_bak']
        # 每条记录对应一个csv文件，这是相应的dataframe
        result_data = pd.DataFrame(columns=columns_values)
        for i in range(int(total_page_num)):
            page_index = i + 1
            # 毫秒级时间戳
            timestamp = int(round(time.time() * 1000))
            # 组合【查看债权明细】弹出页面的URL
            url = credit_url_1 + str(id_value) + credit_url_2 + str(page_index) + credit_url_3 + str(page_size) + credit_url_4 + str(project_type_value) + CONFIG.credit_timestamp + str(timestamp)

            # 抓取json数据
            result_array = get_html_data(url)
            # 获得json字符串
            json_content = result_array[0]
            # json转dict
            dict_data = json.loads(json_content)
            # 拿到相要的数据，是list类型
            list_info = dict_data['Data']['Rows']

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
                borrower_info_url = info_url_1 + asset_id + info_url_2 + str(project_id) + info_url_3 + str(amount)
                item['borrower_info_url'] = borrower_info_url

                # 出借人合同完整URL
                # TODO 这里有可能一个item对应多个合同URL，需要生成URL数组
                borrower_contact_url = cat_url_1 + str(invest_id) + cat_url_2 + asset_id + cat_url_3 + shar_id + cat_url_4 + str(_type) + cat_url_5 + str(project_type) + cat_url_6 + str(asset_type)
                borrower_contact_url_bak = cat_url_1 + str(invest_id) + cat_url_2 + asset_id + cat_url_3 + shar_id + cat_url_4 + '2' + cat_url_5 + str(project_type) + cat_url_6 + str(asset_type)
                item['borrower_contact_url'] = borrower_contact_url
                item['borrower_contact_url_bak'] = borrower_contact_url_bak
                # 自定义数组
                sub_array = [item['Amount'], item['Debtor'].replace('*', ''), item['LoanAmount'], item['borrower_info_url'], item['borrower_contact_url'], item['borrower_contact_url_bak']]
                sub_df = pd.DataFrame(sub_array, index=columns_values)
                # 合并的df
                result_data = result_data.append(sub_df.T, ignore_index=True)
            mkdir(target_folder)
            result_data.to_csv(target_folder + '/' + name + '.csv', encoding='utf_8_sig')
