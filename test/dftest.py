#!/user/bin/env python3
# -*- coding: utf-8 -*-
# import pandas as pd
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

char_array = ['A', 'B', 'C', 'D', 'E']

# for i, char in enumerate(char_array):
#     print(i)
#     print(char)

print(char_array[2])
