#!/user/bin/env python3
# -*- coding: utf-8 -*-
import json
import time
from util.common_util import get_html_data
from util.common_util import get_contact_html
from util.common_util import get_contact_html_no_redirection
from util.pp_contact_util import generate_html_result


# url = 'https://www.ppmoney.com/stepup/investcontract?investId=4005850&assetId=125F14DDC1DA152F205A0A41DC784FF0E4E51AF4AAD07497&shareId=1018059215056142809&type=1&projectType=104046&assetType=10'
# url_bak = 'https://www.ppmoney.com/stepup/investcontract?investId=4005850&assetId=125F14DDC1DA152F205A0A41DC784FF0E4E51AF4AAD07497&shareId=1018059215056142809&type=2&projectType=104046&assetType=10'
#
# # get_contact_html(url, url_bak)
#
# response = get_contact_html_no_redirection(url, url_bak)
# print(response[2])

# folder = r'C:\pp\自助投\自助投[20180425-23]2018-04-26-10-55\14-7.41-邓'
# generate_html_result(folder, folder, folder + '/自助投[20180425-23]2018-04-26-10-55.csv', )

# def get_project_count(project_type):
#     """
#     根据投资类型，获取投资笔数
#     :param project_type:
#     :return:
#     """
#     # 毫秒级时间戳
#     timestamp = int(round(time.time() * 1000))
#     url = 'https://www.ppmoney.com/stepup/InvestProjectList?type=1&pageIndex=1&pageSize=6&projectType=' + str(project_type) + '&_=' + str(timestamp)
#     response = get_html_data(url)
#     json_data = json.loads(response[0])
#     return json_data['Data']['TotalCount']
#
#
# print(get_project_count(104043))
