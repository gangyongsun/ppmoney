#!/user/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from PIL import Image
import time


def short_sc(el, b):
    start_higth = el.location["y"]
    js = "scrollTo(0,%s)" % (start_higth)
    b.execute_script(js)  # 执行js
    time.sleep(0.5)
    fp = r"C:\Users\wdj\Desktop\test.png"  # 图片地址，运行的话，改一下
    b.get_screenshot_as_file(fp)
    img = Image.open(fp=fp)
    img2 = img.crop((el.location["x"], 0, el.size["width"] + el.location["x"], el.size["height"]))  # 剪切图片
    img2.save(fp)


def long_sc(el, b):
    count = int(el.size["height"] / sc_hight)  # 元素的高度除以你每次截多少就是次数
    start_higth = el.location["y"]  # 元素的初始高度
    max_px = start_higth + (count - 1) * sc_hight  # for循环中最大的px
    last_px = el.size["height"] + start_higth - sc_hight  # 元素最底部的位置
    surplus_px = last_px - max_px  # 剩余的边的高度
    img_path = []  # 用来存放图片地址
    for i in range(0, count):
        js = "scrollTo(0,%s)" % (start_higth + i * sc_hight)  # 用于移动滑轮，每次移动614px，初始值是元素的初始高度
        b.execute_script(js)  # 执行js
        time.sleep(0.5)
        fp = "./%s.png" % i  # 图片地址，运行的话，改一下
        b.get_screenshot_as_file(fp)  # 屏幕截图,这里是截取是完整的网页图片，你可以打断点看一下图片
        img = Image.open(fp=fp)
        img2 = img.crop((el.location["x"], 0, el.size["width"] + el.location["x"], sc_hight))  # 剪切图片
        img2.save(fp)  # 保存图片，覆盖完整的网页图片
        img_path.append(fp)  # 添加图片路径
        time.sleep(0.5)
        print(js)
    else:
        js = "scrollTo(0,%s)" % last_px  # 滚动到最后一个位置
        b.execute_script(js)
        fp = r"C:\Users\wdj\Desktop\last.png"
        b.get_screenshot_as_file(fp)
        img = Image.open(fp=fp)
        print((el.location["x"], sc_hight - surplus_px, el.size["width"] + el.location["x"], sc_hight))
        img2 = img.crop((el.location["x"], sc_hight - surplus_px, el.size["width"] + el.location["x"], sc_hight))
        img2.save(fp)
        img_path.append(fp)
        print(js)
    new_img = Image.new("RGB", (el.size["width"], el.size["height"]))  # 创建一个新图片,大小为元素的大小
    k = 0
    for i in img_path:
        tem_img = Image.open(i)
        new_img.paste(tem_img, (0, sc_hight * k))  # 把图片贴上去,间隔一个截图的距离
        k += 1
    else:
        new_img.save("./test.png")  # 保存


b = webdriver.Chrome(executable_path="/Applications/Google Chrome.app/Contents/MacOS/chromedriver")  # 指定一下driver
b.get("https://www.w3school.com.cn/html/html_links.asp")
b.maximize_window()  # 最大化窗口
# b.get_screenshot_as_file(fp)
sc_hight = 614  # 你屏幕截图默认的大小，可以去截一张，去画图里面看看是多少像素，我这里是614像素
# b.switch_to.frame(b.find_element_by_xpath('//*[@id="intro"]/iframe'))
el = b.find_element_by_id("maincontent")  # 找到元素
if el.size["height"] > sc_hight:
    long_sc(el, b)
else:
    short_sc(el, b)
