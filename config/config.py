# 请求头,让网站监测是浏览器
headers = {
    'user-agent'':' 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36',
}
cookie_value = '__jsluid_s=a699ec62be5a522b936e11ad480e504d; Wt0e_5254_saltkey=Z61bBmsI; Wt0e_5254_lastvisit=1603367628; ppPartnerShow=1; ppPartner=1; __jsluid_h=1a6f73cd4cdc078a0f56c1193e05ad04; ASP.NET_SessionId=rnsnf3oervxdpa2h2kybbywd; cj_uid=B85CB4FA5EC084E6B37E766441E66689; cj_user=92DB1D6D028767C862DF988D2444E4D2; __mscd3a__=0ro5dkcw; __RequestVerificationToken=VWDDIO3LqPxnY2Q-7nrJKAyYoEqnzaGFkcrnjcVUXFJQcCdP8bwYe8SpZaXGXNBg1-mvyw2; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221052813175920%22%2C%22%24device_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%7D; PPmoney.AUTH=9ECC97BBCE2C77F267E90ED01A3BB42FDC03B59F11023D51E4536B05699EDE35B9C524C7F9A7F28FE11C10C203E9B3C76668081D372B6EBDD68E43FABBE5EA4BAE70E5BE09FFCA1A467B7D809FD5A5ED6B4511EFBFA8C8585FB1AC27886FF52BC9B4EF87; Wt0e_5254_sid=PNGuQG; Wt0e_5254_lip=123.112.171.75%2C1604939494; Wt0e_5254_lastact=1604947923%09uc.php%09; Wt0e_5254_auth=f164%2F02Sd8fq147zUNJoYmtKL3Iow2Kmw0CLIbPf0GhoFoxrtX5UlST%2BioHOkeILL6zreMchJidRKbpea7lGJrO4e0D5; sensorsInitUser=%7B%22NickName%22%3A%22%E6%9D%8E**%E5%A5%B3%E5%A3%AB%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.00%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A%222020%2F11%2F10%202%3A52%3A02%22%2C%22Sex%22%3A2%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221052813175920_91E18282BD95BC1AEB0DD069EBA373DF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D; InitUser=%7B%22value%22%3A%7B%22NickName%22%3A%22%E6%9D%8E**%E5%A5%B3%E5%A3%AB%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.00%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A-1280%2C%22Sex%22%3A2%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221052813175920_91E18282BD95BC1AEB0DD069EBA373DF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D%2C%22expires%22%3A1604948103065%7D'
headers_2 = {
    'Host': 'www.ppmoney.com',
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
super_folder = 'ppmoney'

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
