#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
from util.common_util import mkdir
from util.pp_contact_util import generate_html_result
from util.pp_csv_util import generate_basic_csv
from util.pp_csv_util import generate_credit_csv
from util.common_util import walk_file
import config.config as CONFIG

# csv文件目录
# 自助投目录
credit_generated_csv_folder_4_zizhu = CONFIG.credit_generated_csv_folder_4_zizhu
info_contact_result_folder_4_zizhu = CONFIG.info_contact_result_folder_4_zizhu
csv_analysis_failed_folder_4_zizhu = CONFIG.csv_analysis_failed_folder_4_zizhu
# 安心投目录
credit_generated_csv_folder_4_anxin = CONFIG.credit_generated_csv_folder_4_anxin
info_contact_result_folder_4_anxin = CONFIG.info_contact_result_folder_4_anxin
csv_analysis_failed_folder_4_anxin = CONFIG.csv_analysis_failed_folder_4_anxin

if __name__ == "__main__":
    # # 第一步，生成自助投、安心投基础csv文件
    # print('============1.自助投、安心投基础csv文件生成开始============')
    # # 自助投、安心投基础csv文件生成目录
    # basic_csv_folder = CONFIG.basic_csv_folder
    #
    # # 安心投
    # an_xin_tou_total_record = 1
    # an_xin_tou_project_type = CONFIG.an_xin_tou_project_type
    # generate_basic_csv(an_xin_tou_total_record, an_xin_tou_project_type, basic_csv_folder)
    #
    # # 自助投
    # zi_zhu_tou_total_record = 0
    # zi_zhu_tou_project_type = CONFIG.zi_zhu_tou_project_type
    # generate_basic_csv(zi_zhu_tou_total_record, zi_zhu_tou_project_type, basic_csv_folder)
    # print('============1.自助投、安心投基础csv文件生成结束============')
    #
    # # 第二步，生成债权明细出借人csv文件
    # print('============2.债权明细出借人csv文件生成开始============')
    # # 债权明细配置信息文件
    # # 安心投
    # csv_file_path_anxin = CONFIG.basic_csv_folder + '/安心投.csv'
    # if os.path.exists(csv_file_path_anxin):
    #     csv_file_anxin = csv.reader(open(csv_file_path_anxin, 'r', encoding='utf-8-sig'))
    #     generate_credit_csv(csv_file_anxin, credit_generated_csv_folder_4_anxin)
    #
    # # 自助投
    # csv_file_path_zizhu = CONFIG.basic_csv_folder + '/自助投.csv'
    # if os.path.exists(csv_file_path_zizhu):
    #     csv_file_zizhu = csv.reader(open(csv_file_path_zizhu, 'r', encoding='utf-8-sig'))
    #     generate_credit_csv(csv_file_zizhu, credit_generated_csv_folder_4_zizhu)
    #
    # print('============2.债权明细出借人csv文件生成结束============')

    # 第三步，遍历债权明细出借人csv文件生成结果
    mkdir(csv_analysis_failed_folder_4_anxin)
    mkdir(csv_analysis_failed_folder_4_zizhu)
    # 安心投
    anxin_csv_file_array = walk_file(credit_generated_csv_folder_4_anxin)
    for file_path in anxin_csv_file_array:
        print('============开始解析：【' + file_path + '】 生成出借人信息、合同html============')
        generate_html_result(info_contact_result_folder_4_anxin, csv_analysis_failed_folder_4_anxin, file_path)
        print('============结束解析：【' + file_path + '】 生成出借人信息、合同html============')

    # 自助投
    zizhu_csv_file_array = walk_file(credit_generated_csv_folder_4_zizhu)
    for file_path in zizhu_csv_file_array:
        print('============开始解析：【' + file_path + '】 生成出借人信息、合同html============')
        generate_html_result(info_contact_result_folder_4_zizhu, csv_analysis_failed_folder_4_zizhu, file_path)
        print('============结束解析：【' + file_path + '】 生成出借人信息、合同html============')
