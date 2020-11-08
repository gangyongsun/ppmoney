# -*- coding: utf8 -*-
import time
import xlrd
from selenium import webdriver


def read_excel(filename):
    data = xlrd.open_workbook(filename)  # 打开xls文件
    sheet = data.sheets()[0]  # 打开第一张表
    rows = sheet.nrows  # 获取表的行数
    cols = sheet.ncols  # 获取表的列数
    nrows = bytes(rows)
    ncols = bytes(cols)
    print("共:" + str(nrows)+ "行,  " + str(ncols) + "列")
    # for i in range(rows):
    for i in range(3):
        if i == 0:
            continue
        for j in range(cols - 1):
            ctype = sheet.cell(i, j).ctype  # 表格的数据类型
            cell = sheet.cell_value(i, j)
            if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
                cell = int(cell)  # 浮点转成整型
            cell = bytes(cell)
            url = "https://china.nba.com/"
            print(url)
            browser = webdriver.Firefox()
            browser.set_window_size(1200, 900)
            browser.get(url)  # Load page
            time.sleep(10)
            js = "var q=document.documentElement.scrollTop=10000"
            browser.execute_script(js)
            time.sleep(10)
            browser.execute_script("""
                    $('#main').siblings().remove();
                    $('#aside__wrapper').siblings().remove();
                    $('.ui.sticky').siblings().remove();
                    $('.follow-me').siblings().remove();
                    $('img.ui.image').siblings().remove();
                    """)
            browser.save_screenshot("图片保存路径\\图片名称.png")
            browser.close()


if __name__ == "__main__":
    url = "https://china.nba.com/"
    print(url)
    browser = webdriver.Firefox()
    browser.set_window_size(1200, 900)
    browser.get(url)  # Load page
    time.sleep(10)
    js = "var q=document.documentElement.scrollTop=10000"
    browser.execute_script(js)
    time.sleep(10)
    browser.execute_script("""
            $('#main').siblings().remove();
            $('#aside__wrapper').siblings().remove();
            $('.ui.sticky').siblings().remove();
            $('.follow-me').siblings().remove();
            $('img.ui.image').siblings().remove();
            """)
    browser.save_screenshot("./nba.png")
    browser.close()
