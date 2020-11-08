import csv
import time
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

import config.config as CONFIG
from util.common_util import mkdir
from util.common_util import get_html_data
from util.common_util import write_file


def generate_html_result(csv_file_name, csv_file):
    for line_data in csv_file:
        time.sleep(1)
        # 出借人序号
        borrower_no = line_data[0]
        # 出借人金额
        borrower_value = line_data[1]
        # 出借人姓
        borrower_family_name = line_data[2]
        # 出借人信息URL
        borrower_info_url = line_data[3]

        # 最终出借人信息URL
        final_borrower_info_url = CONFIG.basic_url + borrower_info_url
        # 网页内容
        request_data = get_html_data(final_borrower_info_url)
        html_content = request_data[0]
        encoding = request_data[1]
        status_code = request_data[2]

        # 获取当前编码
        if status_code == 403:
            csv_line = line_data[0] + ',' + line_data[1] + ',' + line_data[2] + ',' + line_data[3]
            print(csv_line + '：写入失败')
            write_file(csv_line + '\n', './csv/' + csv_file_name + '-failed.csv', encoding='utf-8', mode='a')
        else:
            # 文件夹
            folder_name = CONFIG.super_folder + '/' + csv_file_name + '/' + str(borrower_no) + '-' + str(
                borrower_value) + '-' + borrower_family_name
            mkdir(folder_name)

            # 出借人信息html文件
            borrower_info_file_name = folder_name + '/' + CONFIG.borrower_html
            write_file(html_content, borrower_info_file_name, encoding=encoding, mode='w')


if __name__ == "__main__":
    csv_file_name = '自助投20180827-4-110342-test'
    csv_file = csv.reader(open('./csv/' + csv_file_name + '.csv', 'r', encoding='utf-8-sig'))
    generate_html_result(csv_file_name, csv_file)

