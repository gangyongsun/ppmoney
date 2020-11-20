#!/user/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import sys
import csv

from util.common_util import mkdir
from util.common_util import get_html_data
from util.common_util import get_contact_html
from util.common_util import get_contact_html_data
from util.common_util import write_file

from itertools import islice

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

import config.config as CONFIG


def generate_contact(url, folder_name):
    # 抓取合同网页内容
    request_contract_data = get_contact_html(url)
    contract_html_content = request_contract_data[0]
    contract_encoding = request_contract_data[1]
    contract_status_code = request_contract_data[2]
    if contract_status_code == 404:
        print('404:' + url)
        return False
    elif '协议生成中' in contract_html_content:
        print('协议生成中...')
        return False
    else:
        # 出借人信息html文件
        borrower_contract_file_name = folder_name + '/' + CONFIG.borrower_contact_html
        write_file(contract_html_content, borrower_contract_file_name, encoding=contract_encoding, mode='w')
        return True


def generate_contact_html(success_folder, failed_folder, csv_file_name, data_array):
    """
    生成出借人合同html
    :param success_folder: 执行成功目录
    :param failed_folder: 执行失败目录
    :param csv_file_name: 读取的csv文件名
    :param data_array: 需要的信息数组
    :return:
    """
    # 出借人序号
    borrower_no = data_array[0]
    # 出借人金额
    borrower_value = data_array[1]
    # 出借人姓
    borrower_family_name = data_array[2]
    # 出借人信息URL
    borrower_info_url = data_array[3]
    # 出借人合同数组
    borrower_contract_url = data_array[4]
    # 扩展出借人合同数组
    borrower_contract_url_bak = data_array[5]

    borrower_contract_url_array = borrower_contract_url.split(',')
    borrower_contract_url_bak_array = borrower_contract_url_bak.split(',')

    folder_name = success_folder + '/' + os.path.basename(csv_file_name) + '/' + str(borrower_no) + '-' + str(borrower_value) + '-' + str(borrower_family_name)
    mkdir(folder_name)

    # 循环生成合同最终URL
    for index, sub_url in enumerate(borrower_contract_url_array):
        return_value = generate_contact(sub_url, folder_name)
        if not return_value:
            return_value = generate_contact(borrower_contract_url_bak_array[index], folder_name)
            if not return_value:
                print(borrower_no + '：出借人合同写入失败！可通过此URL手动获取\n' + sub_url + '\n' + borrower_contract_url_bak)
                csv_line = borrower_no + ',' + borrower_value + ',' + borrower_family_name + ',' + borrower_info_url + ',' + borrower_contract_url + ',' + borrower_contract_url_bak
                write_file(csv_line + '\n', failed_folder + '/' + csv_file_name + '-failed.csv', encoding='utf-8', mode='a')


def generate_info_html(success_folder, failed_folder, csv_file_name, data_array):
    """
    生成出借人信息html
    :param success_folder: 执行成功目录
    :param failed_folder: 执行失败目录
    :param csv_file_name: 读取的csv文件名
    :param data_array: 需要的信息数组
    :return:
    """
    # 出借人序号
    borrower_no = data_array[0]
    # 出借人金额
    borrower_value = data_array[1]
    # 出借人姓
    borrower_family_name = data_array[2]
    # 出借人信息URL
    borrower_info_url = data_array[3]
    # 出借人合同数组
    borrower_contract_url = data_array[4]
    # 扩展出借人合同数组
    borrower_contract_url_bak = data_array[5]

    # 网页内容
    request_data = get_html_data(borrower_info_url)
    html_content = request_data[0]
    encoding = request_data[1]
    status_code = request_data[2]

    # 获取当前编码
    if status_code == 403:
        print(borrower_no + '：出借人信息写入失败！可通过此URL手动获取\n' + borrower_info_url)
        csv_line = borrower_no + ',' + borrower_value + ',' + borrower_family_name + ',' + borrower_info_url + ',' + borrower_contract_url + ',' + borrower_contract_url_bak
        write_file(csv_line + '\n', failed_folder + '/' + csv_file_name + '-failed.csv', encoding='utf-8', mode='a')
    else:
        # 文件夹
        folder_name = success_folder + '/' + csv_file_name + '/出借人信息/' + str(borrower_no) + '-' + str(borrower_value) + '-' + str(borrower_family_name)
        mkdir(folder_name)

        # 出借人信息html文件
        borrower_info_file_name = folder_name + '/' + CONFIG.borrower_html
        write_file(html_content, borrower_info_file_name, encoding=encoding, mode='w')


def generate_html_result(success_folder, failed_folder, file_path):
    """
    统一调用
    :param success_folder: 执行成功目录
    :param failed_folder: 执行失败目录
    :param file_path: csv文件全路径名
    :return:
    """
    # 不带扩展名
    csv_file_name = os.path.basename(file_path).split('.')[0]
    csv_file = csv.reader(open(file_path, 'r', encoding='utf-8-sig'))
    for line_data in islice(csv_file, 1, None):
        time.sleep(5)
        # 出借人序号、出借人金额、出借人姓、出借人信息URL、出借人合同URL数组、扩展出借人合同URL数组
        # TODO 出借人合同URL数组，需要进一步处理，这里只是URL字符串
        data_array = [line_data[0], line_data[1], line_data[2], line_data[4], line_data[5], line_data[6]]
        # 调用生成出借人信息html函数
        generate_info_html(success_folder, failed_folder, csv_file_name, data_array)
        # 调用生成出借人合同html函数
        # generate_contact_html(success_folder, failed_folder, csv_file_name, data_array)
