import requests
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
# 先引入目录的上级
sys.path.append(rootPath)

import config.config as CONFIG


def format_time(date_time, source_format, target_format):
    """
    格式化时间字符串
    :param date_time: 时间字符串
    :param source_format: 原格式
    :param target_format: 目标格式
    :return:
    """
    time_struct = time.strptime(date_time, source_format)
    return time.strftime(target_format, time_struct)


def walk_file(path):
    """
    遍历文件夹拿文件
    :param path: 主文件夹
    :return: 文件名数组
    """
    csv_file_array = []
    for root, dirs, files in os.walk(path):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        for file in files:
            full_file_name = os.path.join(root, file)
            file_name = os.path.basename(full_file_name)
            if file_name.endswith('.csv'):
                csv_file_array.append(full_file_name)
    return csv_file_array


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
    # 爬取网页的URL
    response = requests.get(url, headers=CONFIG.headers_2)
    new_header = response.headers
    new_url = response.url
    # print(response.cookies)
    new_response = requests.get(new_url, headers=new_header)
    print(new_response.text)

    encoding = response.apparent_encoding
    status_code = response.status_code
    html_content = response.text
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


def screenshot(url, pic_name):
    """
    截图
    :param url: URL路径
    :param pic_name: 保存的图片名
    :return:
    """
    # chromedriver的路径
    chromedriver = "/Applications/Google Chrome.app/Contents/MacOS/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver

    # 设置chrome开启的模式，headless就是无界面模式(一定要使用这个模式，不然截不了全页面，只能截到你电脑的高度)
    chrome_options = Options()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

    # 控制浏览器写入并转到链接
    driver.get(url)
    # time.sleep(1)

    # 接下来是全屏的关键，用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(width, height)

    # 将浏览器的宽高设置成刚刚获取的宽高
    driver.set_window_size(width, height)
    # time.sleep(1)

    # 截图并关掉浏览器
    driver.save_screenshot(pic_name)
    driver.close()
