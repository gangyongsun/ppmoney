import requests
import csv
import time
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

from util.common_util import mkdir
import config.config as CONFIG


def generate_html_result(csv_file_name, csv_file):
    for line_data in csv_file:
        time.sleep(4)
        # 出借人序号、出借人金额、出借人姓、出借人信息URL、出借人合同数组
        data_array = [line_data[0], line_data[1], line_data[2], line_data[3], line_data[4]]
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

        url = CONFIG.basic_url + borrower_contract_url
        print(url)
        import requests
        url='https://www.ppmoney.com//stepup/investcontract?investId=2679152&assetId=A3974AF8C535F08CCCE62EA3C1EF8C34AFD57DDF54F4DB74&shareId=840894815959646234&type=1&projectType=104043&assetType=10'
        payload = {}
        headers = {
            'Host': 'www.ppmoney.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': ''
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        write_file(response.text, './test.html', encoding=response.encoding, mode='w')


def write_file(html_content, file_name, encoding, mode):
    """
    写文件,默认操作类型为w，编码为GBK
    :param html_content:文件内容
    :param file_name:文件名
    :param encoding:编码
    :param mode:操作类型
    :return:
    """
    # 新建一个文件名 ,注意文件格式的编码和 获取的编码 要一致，不然出现乱码问题
    file = open(file_name, mode, encoding=encoding)
    for i in html_content:
        # 将数据写入文件
        file.write(i)
    # 关闭文件
    file.close()


csv_file_name = '自助投20180828-1'
csv_file = csv.reader(open('../csv/' + csv_file_name + '.csv', 'r', encoding='utf-8-sig'))
generate_html_result(csv_file_name, csv_file)
