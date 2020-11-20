# 请求头,让网站监测是浏览器
headers = {
    'user-agent'':' 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36',
}
cookie_value = '__jsluid_s=bc14361af3bee8e064c71134d6d8b0a0; ASP.NET_SessionId=gn3k3qll0lvgyqns5jiwvimq; Wt0e_5254_saltkey=zpsi7ZSp; Wt0e_5254_lastvisit=1605679251; __RequestVerificationToken=JKW2-6OLG6GwgyHMahX0r8CqXjiUiK4_QYbR7864S2i_hE7rStIZ9V2BRW4HoWNL53GZBQ2; ppPartnerShow=1; ppPartner=1; Wt0e_5254_lip=222.130.23.1%2C1605832869; PPmoney.AUTH=60BCBF3CF0502A77FA24D0F38B1C97DF64143345F2326AA0607231A367C59EAECCEA63A01C137B9CC21F9C09CDCF992525AED82ECE651278F0756D2FF1AAC33094C295BB88CCC5E344495CC8C89A87F64B1942FCF30456C313983877D532DCC4E1BCFE01; cj_uid=B85CB4FA5EC084E6B37E766441E66689; cj_user=92DB1D6D028767C862DF988D2444E4D2; __mscd3a__=0ro5dkcw; Wt0e_5254_sid=pRvvpt; Wt0e_5254_lastact=1605833284%09uc.php%09; Wt0e_5254_auth=1e580nxuW5eopJHCuMxbqbTIIPt9l5sFEWyhZXgRVI%2B1Jc%2F614g5bE3KAbw4%2B%2BQhseAL%2FS34rkqECaZWIx7C4AjhvIWn; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221052813175920%22%2C%22%24device_id%22%3A%2217591a254b42c2-021270176b48dd-32667001-1764000-17591a254b5828%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2217591a254b42c2-021270176b48dd-32667001-1764000-17591a254b5828%22%7D; sensorsInitUser=%7B%22NickName%22%3A%22%E6%9D%8E**%E5%A5%B3%E5%A3%AB%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.00%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A%222020%2F11%2F20%208%3A53%3A12%22%2C%22Sex%22%3A2%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221052813175920_91E18282BD95BC1AEB0DD069EBA373DF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D; InitUser=%7B%22value%22%3A%7B%22NickName%22%3A%22%E6%9D%8E**%E5%A5%B3%E5%A3%AB%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.00%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A-3978%2C%22Sex%22%3A2%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221052813175920_91E18282BD95BC1AEB0DD069EBA373DF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D%2C%22expires%22%3A1605833775754%7D'
headers_2 = {
    # 'Host': 'www.ppmoney.com',
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
    'Cookie': cookie_value
}

basic_url = 'https://www.ppmoney.com'
borrower_html = '出借人信息.html'
borrower_contact_html = '出借人合同.html'

# 【查看债权明细】弹出页面的URL相关配置
credit_right_basic_url = 'https://www.ppmoney.com/stepup/CreditRightList?id='
credit_page_index = '&pageIndex='
credit_page_size = '&pageSize='
credit_project_type = '&projectType='
credit_timestamp = '&_='

# 【出借人信息】弹出页面的URL相关配置
borrower_info_basic_url = 'https://www.ppmoney.com/stepup/CredisRightDetail?assetId='
borrower_info_prj_id = '&prjId='
borrower_info_amount = '&amount='

# 【出借人合同】弹出页面的URL相关配置
borrower_contact_basic_url = 'https://www.ppmoney.com/stepup/investcontract?investId='
borrower_contact_asset_id = '&assetId='
borrower_contact_share_id = '&shareId='
borrower_contact_share_type = '&type='
borrower_contact_project_type = '&projectType='
borrower_contact_asset_type = '&assetType='

# 此文件需要用户自己整理
credit_csv_file = r'C:\ppmoney_doc\csv\安心投债权明细配置信息.csv'

# 程序生成的自助投csv文件目录
credit_generated_csv_folder_4_zizhu = '/Users/alvin/Downloads/pp/csv/自助投'  # r'C:\ppmoney_doc\自助投'
credit_generated_csv_folder_4_anxin = '/Users/alvin/Downloads/pp/csv/安心投'  # r'C:\ppmoney_doc\安心投'

# csv文件解析失败记录目录
csv_analysis_failed_folder_4_zizhu = '/Users/alvin/Downloads/pp/csv/自助投/failed'  # r'C:\ppmoney_doc\自助投\failed'
info_contact_result_folder_4_zizhu = '/Users/alvin/Downloads/pp/csv/自助投'  # r'C:\ppmoney_doc\自助投\result'

# csv文件解析失败记录目录
csv_analysis_failed_folder_4_anxin = '/Users/alvin/Downloads/pp/csv/安心投/failed'  # r'C:\ppmoney_doc\安心投\failed'
info_contact_result_folder_4_anxin = '/Users/alvin/Downloads/pp/csv/安心投'  # r'C:\ppmoney_doc\安心投\result'

# 自助投project type
zi_zhu_tou_project_type = 104043
# 安心投project type
an_xin_tou_project_type = 104046
# 自助投、安心投基础csv文件生成目录
basic_csv_folder = '/Users/alvin/Downloads/pp/csv'  # r'C:\ppmoney_doc\csv'
