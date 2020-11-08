import requests
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

import config.config as CONFIG


def mkdir(path):
    """
    创建文件夹目录
    :param path:路径
    :return:Ture False
    """
    # 去除首位空格,去除尾部 \ 符号
    path = path.strip().rstrip("\\")

    # 判断路径是否存在
    is_exists = os.path.exists(path)

    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        # print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path + ' 目录已存在')
        return False


def get_html_data(url):
    """
    写文件,默认操作类型为w，编码为GBK
    :param file_name:文件名
    :param operation_type:操作类型：w：写入
    :param encoding:
    :return:
    """
    # 请求头,让网站监测是浏览器
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36',
    }
    # 爬取网页的URL
    html_data = requests.get(url, headers=headers, timeout=30)

    encoding = html_data.apparent_encoding
    status_code = html_data.status_code
    html_content = html_data.text.replace('670px', '100%').replace('getQueryString(\'amount\')', url.split('=')[-1])
    return html_content, encoding, status_code

def get_contact_html_data(url):
    """
    写文件,默认操作类型为w，编码为GBK
    :param file_name:文件名
    :param operation_type:操作类型：w：写入
    :param encoding:
    :return:
    """
    # 爬取网页的URL
    print(url)
    payload = {}

    html_data = requests.request("GET", url, headers=CONFIG.headers_2, data=payload)
    encoding = html_data.apparent_encoding
    status_code = html_data.status_code
    html_content = html_data.text
    return html_content, encoding, status_code

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
