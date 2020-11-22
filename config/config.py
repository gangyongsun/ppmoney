cookie_value = '__jsluid_s=a699ec62be5a522b936e11ad480e504d; ppPartnerShow=1; __jsluid_h=1a6f73cd4cdc078a0f56c1193e05ad04; Wt0e_5254_saltkey=nHSmvvnp; Wt0e_5254_lastvisit=1606010127; ppPartner=1; ASP.NET_SessionId=tjuep3lwjyrm32xseanyugkv; __RequestVerificationToken=qhXXnZ9XjHAHXe-7GiJBHygZXvESlRlAGCdcuthvjFj-tU2aX08GTzJtbJ1a3Ci1cCFy0w2; PPmoney.AUTH=81CF04D2FC5A8741DDC1F8280ECFCE35E0293FAEF2B7FACA84D66F11820DBD850B3F57F6C88DF9EA7191618BF9FB187DC7C07637304F246BBE32F5D9ABAE822AAE53B09B892AA32C27DE6ADEC14465313D1C59EB40015A0F9DB64E5C7EC57B6BBDB086C8; cj_uid=E8BF68BA49FBEB319EB19917AA98AECB; cj_user=377CBFB5E0532B936769E8A6B88E0461; __mscd3a__=02wM8JtG; Wt0e_5254_sid=nWiwAd; Wt0e_5254_lip=114.84.193.184%2C1601514560; Wt0e_5254_lastact=1606052402%09uc.php%09; Wt0e_5254_auth=08a6pFphGx6wi8hISrapTYvE1GkB2ekpdWNYVX9JOkQ5Mt3xLJFarbESTtr5AuxoxUNe%2FBXkj%2FnQ4kjNWc1JfHf2Jco; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2297202081444%22%2C%22%24device_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%7D; sensorsInitUser=%7B%22NickName%22%3A%22%E6%BB%95%E5%9B%BD%E6%95%85%E5%9F%8E%22%2C%22NotReadLetterCount%22%3A10%2C%22Amount%22%3A%2210.09%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A%222020%2F11%2F22%2021%3A39%3A57%22%2C%22Sex%22%3A1%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%2297202081444_F1A8C0E0FE6C4975DBA9EDBBB3AEE1CF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D; InitUser=%7B%22value%22%3A%7B%22NickName%22%3A%22%E6%BB%95%E5%9B%BD%E6%95%85%E5%9F%8E%22%2C%22NotReadLetterCount%22%3A10%2C%22Amount%22%3A%2210.09%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A-5272%2C%22Sex%22%3A1%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%2297202081444_F1A8C0E0FE6C4975DBA9EDBBB3AEE1CF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D%2C%22expires%22%3A1606052582087%7D'
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

# 程序生成的csv文件目录
target_folder_4_zizhu_mac = '/Users/alvin/Downloads/pp/csv/自助投'
target_folder_4_anxin_mac = '/Users/alvin/Downloads/pp/csv/安心投'
target_folder_4_zizhu = r'C:\pp\csv\自助投'
target_folder_4_anxin = r'C:\pp\csv\安心投'

# 自助投project type
zi_zhu_tou_project_type = 104043
# 安心投project type
an_xin_tou_project_type = 104046
# 自助投、安心投基础csv文件生成目录
# basic_csv_folder_mac = '/Users/alvin/Downloads/pp/csv'
basic_csv_folder = r'C:\pp\csv'
