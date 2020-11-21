cookie_value = '__jsluid_s=a699ec62be5a522b936e11ad480e504d; Wt0e_5254_saltkey=Z61bBmsI; Wt0e_5254_lastvisit=1603367628; ppPartnerShow=1; __jsluid_h=1a6f73cd4cdc078a0f56c1193e05ad04; ppPartner=1; ASP.NET_SessionId=saefazizdaqxabm55zqrnc0t; __RequestVerificationToken=9jQi5w--JUcNjHVZcS_GP59N6IXfciC-8PBVFn_uHLUO95n6G9wH9tFI9bXFjjDMnlaOkQ2; Wt0e_5254_lip=123.112.170.160%2C1605939229; PPmoney.AUTH=E481C1D7E33FEA17FC6CC38B83BD9257BEFFCBF190EDD2B08EB720F44328EEF559FBE4D3B851833B7BA221AA12F0D7431F32444C768DE1DF4C467AD882EB2046F41FC93AB95D19A21904D921C938EB2D8C028342F9D75319D1A92AD681F51623BA00EEB7; cj_uid=B85CB4FA5EC084E6B37E766441E66689; cj_user=92DB1D6D028767C862DF988D2444E4D2; __mscd3a__=0ro5dkcw; Wt0e_5254_sid=B9BXKE; Wt0e_5254_lastact=1605939293%09uc.php%09; Wt0e_5254_auth=3cbfdMwuoGCktAK7IRkCPkN1AbIP7eOfzqtj98HggPTRpLvxH5k7Nu8L7BybtVREbpOR7J64JRYsHH3fwXVEw0qIWOeT; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221052813175920%22%2C%22%24device_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%7D; sensorsInitUser=%7B%22NickName%22%3A%22%E6%9D%8E**%E5%A5%B3%E5%A3%AB%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.00%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A%222020%2F11%2F21%2014%3A14%3A51%22%2C%22Sex%22%3A2%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221052813175920_91E18282BD95BC1AEB0DD069EBA373DF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D; InitUser=%7B%22value%22%3A%7B%22NickName%22%3A%22%E6%9D%8E**%E5%A5%B3%E5%A3%AB%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.00%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A-2196%2C%22Sex%22%3A2%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221052813175920_91E18282BD95BC1AEB0DD069EBA373DF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D%2C%22expires%22%3A1605939473006%7D'
# 请求头
headers = {
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
# credit_csv_file = r'C:\pp\csv\安心投债权明细配置信息.csv'

# 程序生成的自助投csv文件目录
# credit_generated_csv_folder_4_zizhu = '/Users/alvin/Downloads/pp/csv/自助投'  # r'C:\pp\自助投'
# credit_generated_csv_folder_4_anxin = '/Users/alvin/Downloads/pp/csv/安心投'  # r'C:\pp\安心投'

credit_generated_csv_folder_4_zizhu = r'C:\pp\自助投'
credit_generated_csv_folder_4_anxin = r'C:\pp\安心投'

# csv文件解析失败记录目录
# csv_analysis_failed_folder_4_zizhu = '/Users/alvin/Downloads/pp/csv/自助投/failed'  # r'C:\pp\自助投\failed'
# info_contact_result_folder_4_zizhu = '/Users/alvin/Downloads/pp/csv/自助投'  # r'C:\pp\自助投\result'

csv_analysis_failed_folder_4_zizhu = r'C:\pp\自助投\failed'
info_contact_result_folder_4_zizhu = r'C:\pp\自助投'

# csv文件解析失败记录目录
# csv_analysis_failed_folder_4_anxin = '/Users/alvin/Downloads/pp/csv/安心投/failed'  # r'C:\pp\安心投\failed'
# info_contact_result_folder_4_anxin = '/Users/alvin/Downloads/pp/csv/安心投'  # r'C:\pp\安心投\result'

csv_analysis_failed_folder_4_anxin = r'C:\pp\安心投\failed'
info_contact_result_folder_4_anxin = r'C:\pp\安心投'

# 自助投project type
zi_zhu_tou_project_type = 104043
# 安心投project type
an_xin_tou_project_type = 104046
# 自助投、安心投基础csv文件生成目录
# basic_csv_folder = '/Users/alvin/Downloads/pp/csv'  # r'C:\pp\csv'
basic_csv_folder = r'C:\pp\csv'
