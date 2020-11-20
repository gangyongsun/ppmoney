cookie_value = '__jsluid_s=a699ec62be5a522b936e11ad480e504d; Wt0e_5254_saltkey=Z61bBmsI; Wt0e_5254_lastvisit=1603367628; ppPartnerShow=1; __jsluid_h=1a6f73cd4cdc078a0f56c1193e05ad04; ppPartner=1; ASP.NET_SessionId=gacfprpnf2zgwxgmgx2hqfbj; __RequestVerificationToken=yWi-8uGQWR7GiW92lSnzqQMT4TWMgxb9YnbUGm1MUQT3ToOuR3ZJqC2zy_LcyUlN9OLrCA2; cj_uid=5B258326620E86BE4BD40B78F2D5B536; cj_user=DC2F61D8EBDBBB26DD8568D58A0E03C5; __mscd3a__=0sfDgMTn; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221086014001193%22%2C%22%24device_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%7D; PPmoney.AUTH=2B2020BDC2B2FEC5912FFEC1CFAE3316CEF398D66A706C3454AE7322502E1CEAEA7B83703EC70D42B121F77673BF972E3FB67A3A77DCDE5AC434C9D1A517EF72D56F0952EFA638C6DB753A604C549CA8F6F3DD5DB3440A7172CD7013E554938505ACCE64; Wt0e_5254_sid=o988Is; Wt0e_5254_lip=222.130.23.1%2C1605851798; Wt0e_5254_lastact=1605892033%09uc.php%09; Wt0e_5254_auth=8efbreZ0%2BCFbB%2F%2BWqyy5KDJqN54KqNqiQkGjaKzQAGpm3cjUk0MIwQ1qLUNrNObJgTThr6ZIDy5AR1YXHlLvoVdHrbq5; sensorsInitUser=%7B%22NickName%22%3A%22%E5%AD%99**%E5%85%88%E7%94%9F%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.27%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A%222020%2F11%2F21%201%3A07%3A10%22%2C%22Sex%22%3A1%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221086014001193_F83EC6ECD9D2A4F73F7F712B886601FC%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D; InitUser=%7B%22value%22%3A%7B%22NickName%22%3A%22%E5%AD%99**%E5%85%88%E7%94%9F%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.27%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A-3686%2C%22Sex%22%3A1%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221086014001193_F83EC6ECD9D2A4F73F7F712B886601FC%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D%2C%22expires%22%3A1605892213491%7D'
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
