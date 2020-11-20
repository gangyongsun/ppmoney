#!/user/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import random
#
# columns_values = ['Amount', 'Debtor', 'LoanAmount', 'Publisher', 'Name', 'borrower_info_url', 'borrower_contact_url']
# sub_array = [1, 2, 3, 4, 5, 6, 7]
# sub_df = pd.DataFrame(sub_array, index=columns_values)
#
# sub_df2 = pd.DataFrame(sub_array, index=columns_values)
#
# super_df = pd.DataFrame(columns=columns_values)
# super_df = super_df.append(sub_df.T, ignore_index=True).append(sub_df2.T, ignore_index=True)
# print(super_df)


# import time
#
# t = "2018-08-28 11:19"  # 将其转换为时间数组
# timeStruct = time.strptime(t, "%Y-%m-%d %H:%M")
#
# # print(timeStruct)
# # # 转换为时间戳:
# # timeStamp = int(time.mktime(timeStruct))
# # print(timeStamp)
#
# strTime = time.strftime("%Y-%m-%d-%H-%M", timeStruct)
# print(strTime)

# name = '张**'
#
# print(name.replace('*', ''))

# char_array = ['A', 'B', 'C', 'D', 'E']
#
# # for i, char in enumerate(char_array):
# #     print(i)
# #     print(char)
#
# df = pd.DataFrame(char_array)
# print(df.T)
# 收集到的常用Header
my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
item = random.choice(my_headers)
random_header = {
    'User-Agent': item
}
