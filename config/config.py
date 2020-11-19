# 请求头,让网站监测是浏览器
headers = {
    'user-agent'':' 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36',
}
cookie_value = '__jsluid_s=bc14361af3bee8e064c71134d6d8b0a0; ASP.NET_SessionId=gn3k3qll0lvgyqns5jiwvimq; Wt0e_5254_saltkey=zpsi7ZSp; Wt0e_5254_lastvisit=1605679251; __RequestVerificationToken=JKW2-6OLG6GwgyHMahX0r8CqXjiUiK4_QYbR7864S2i_hE7rStIZ9V2BRW4HoWNL53GZBQ2; ppPartnerShow=1; ppPartner=1; cj_uid=5B258326620E86BE4BD40B78F2D5B536; cj_user=DC2F61D8EBDBBB26DD8568D58A0E03C5; __mscd3a__=0sfDgMTn; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221086014001193%22%2C%22%24device_id%22%3A%2217591a254b42c2-021270176b48dd-32667001-1764000-17591a254b5828%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2217591a254b42c2-021270176b48dd-32667001-1764000-17591a254b5828%22%7D; PPmoney.AUTH=067C51A921570EAE04DB547AAEB1D42F49ABBF78D0E3BA47CE3C3F6C0225A3274B319AA58EE1943F0E5C8A3906FB7FCAA41ADFF00C7FA5976A849D87EEA2F333F0CF11AE8B2FFC414ED036E8D4472DB17655A9247DD4C15342AB6F088F699B0D72153BFA; Wt0e_5254_sid=C33G0c; Wt0e_5254_lip=3.34.6.181%2C1605771766; Wt0e_5254_lastact=1605774167%09uc.php%09; Wt0e_5254_auth=b0895rrwIAdOn218KlLRy5J3ahnQl3kC2Wkd4zGwFhpl4XJHwVwyOy%2FMoAxlmVJ5h6HSrl85S7DyGDsmWcEY%2BZi0VoR4; sensorsInitUser=%7B%22NickName%22%3A%22%E5%AD%99**%E5%85%88%E7%94%9F%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.27%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A%222020%2F11%2F19%2016%3A22%3A47%22%2C%22Sex%22%3A1%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221086014001193_F83EC6ECD9D2A4F73F7F712B886601FC%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D; InitUser=%7B%22value%22%3A%7B%22NickName%22%3A%22%E5%AD%99**%E5%85%88%E7%94%9F%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.27%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A-823%2C%22Sex%22%3A1%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221086014001193_F83EC6ECD9D2A4F73F7F712B886601FC%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D%2C%22expires%22%3A1605774347374%7D'
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
info_contact_result_folder_4_zizhu = '/Users/alvin/Downloads/pp/csv/自助投/html'  # r'C:\ppmoney_doc\自助投\result'

# csv文件解析失败记录目录
csv_analysis_failed_folder_4_anxin = '/Users/alvin/Downloads/pp/csv/安心投/failed'  # r'C:\ppmoney_doc\安心投\failed'
info_contact_result_folder_4_anxin = '/Users/alvin/Downloads/pp/csv/安心投/html'  # r'C:\ppmoney_doc\安心投\result'

# 自助投project type
zi_zhu_tou_project_type = 104043
# 安心投project type
an_xin_tou_project_type = 104046
# 自助投、安心投基础csv文件生成目录
basic_csv_folder = '/Users/alvin/Downloads/pp/csv'  # r'C:\ppmoney_doc\csv'
