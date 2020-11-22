#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import platform

from util.common_util import mkdir
from util.pp_contact_util import generate_info_html_result
from util.pp_contact_util import generate_contact_html_result
from util.pp_csv_util import get_project_count
from util.pp_csv_util import generate_basic_csv
from util.pp_csv_util import generate_credit_csv
from util.common_util import walk_file
import config.config as CONFIG

# 自助投安心投project type
zi_zhu_tou_project_type = CONFIG.zi_zhu_tou_project_type
an_xin_tou_project_type = CONFIG.an_xin_tou_project_type

# 系统类型
os_type = platform.system()
# 不同系统的csv文件目录
if os_type == 'Windows':
    # 自助投目录
    target_folder_4_zizhu = CONFIG.target_folder_4_zizhu
    failed_folder_4_zizhu = target_folder_4_zizhu + r'\failed'
    # 安心投目录
    target_folder_4_anxin = CONFIG.target_folder_4_anxin
    failed_folder_4_anxin = target_folder_4_anxin + r'\failed'
elif os_type == 'Mac':
    # 自助投目录
    target_folder_4_zizhu = CONFIG.target_folder_4_zizhu_mac
    failed_folder_4_zizhu = target_folder_4_zizhu + '/failed'
    # 安心投目录
    target_folder_4_anxin = CONFIG.target_folder_4_anxin_mac
    failed_folder_4_anxin = target_folder_4_anxin + '/failed'
else:
    print('others')


def build_csv_step1(target_folder):
    """
    生成自助投、安心投基础csv文件
    :param target_folder: 生成目录
    :return:
    """
    # 第一步，生成自助投、安心投基础csv文件
    print('============1.自助投、安心投基础csv文件生成开始============')
    # 安心投
    an_xin_tou_total_record = get_project_count(an_xin_tou_project_type)
    generate_basic_csv(an_xin_tou_total_record, an_xin_tou_project_type, target_folder)

    # 自助投
    zi_zhu_tou_total_record = get_project_count(zi_zhu_tou_project_type)
    generate_basic_csv(zi_zhu_tou_total_record, zi_zhu_tou_project_type, target_folder)
    print('============1.自助投、安心投基础csv文件生成结束============')


def build_csv_step2(target_folder):
    """
    生成债权明细出借人csv文件
    :param target_folder: 生成目录
    :return:
    """
    # 第二步，生成债权明细出借人csv文件
    print('============2.债权明细出借人csv文件生成开始============')
    # 债权明细配置信息文件
    # 安心投
    csv_file_path_anxin = target_folder + '/安心投.csv'
    if os.path.exists(csv_file_path_anxin):
        csv_file_anxin = csv.reader(open(csv_file_path_anxin, 'r', encoding='utf-8-sig'))
        generate_credit_csv(csv_file_anxin, target_folder_4_anxin)

    # 自助投
    csv_file_path_zizhu = target_folder + '/自助投.csv'
    if os.path.exists(csv_file_path_zizhu):
        csv_file_zizhu = csv.reader(open(csv_file_path_zizhu, 'r', encoding='utf-8-sig'))
        generate_credit_csv(csv_file_zizhu, target_folder_4_zizhu)
    print('============2.债权明细出借人csv文件生成结束============')


def step3():
    """
    生成出借人合同
    :return:
    """
    # 第三步，遍历债权明细出借人csv文件生成结果
    mkdir(failed_folder_4_anxin)
    mkdir(failed_folder_4_zizhu)

    # 安心投
    anxin_csv_file_array = walk_file(target_folder_4_anxin)
    for file_path in anxin_csv_file_array:
        print('============开始解析：【' + file_path + '】 生成出借人合同html============')
        generate_contact_html_result(target_folder_4_anxin, failed_folder_4_anxin, file_path)
        print('============结束解析：【' + file_path + '】 生成出借人合同html============')

    # 自助投
    zizhu_csv_file_array = walk_file(target_folder_4_zizhu)
    for file_path in zizhu_csv_file_array:
        print('============开始解析：【' + file_path + '】 生成出借人合同html============')
        generate_contact_html_result(target_folder_4_zizhu, failed_folder_4_zizhu, file_path)
        print('============结束解析：【' + file_path + '】 生成出借人合同html============')


def step4():
    """
    生成出借人信息
    :return:
    """
    # 第三步，遍历债权明细出借人csv文件生成结果
    mkdir(failed_folder_4_anxin)
    mkdir(failed_folder_4_zizhu)

    # 安心投
    anxin_csv_file_array = walk_file(target_folder_4_anxin)
    for file_path in anxin_csv_file_array:
        print('============开始解析：【' + file_path + '】 生成出借人信息html============')
        generate_info_html_result(target_folder_4_anxin, failed_folder_4_anxin, file_path)
        print('============结束解析：【' + file_path + '】 生成出借人信息html============')

    # 自助投
    zizhu_csv_file_array = walk_file(target_folder_4_zizhu)
    for file_path in zizhu_csv_file_array:
        print('============开始解析：【' + file_path + '】 生成出借人信息html============')
        generate_info_html_result(target_folder_4_zizhu, failed_folder_4_zizhu, file_path)
        print('============结束解析：【' + file_path + '】 生成出借人信息html============')


if __name__ == "__main__":
    # 第一步，生成自助投、安心投基础csv文件
    build_csv_step1(CONFIG.basic_csv_folder)
    # 第二步，生成债权明细出借人csv文件
    build_csv_step2(CONFIG.basic_csv_folder)
    # 第三步，遍历债权明细出借人合同csv文件生成结果
    step3()
    # 第四步，遍历债权明细出借人信息csv文件生成结果
    step4()
