# 请求头,让网站监测是浏览器
headers = {
    'user-agent'':' 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36',
}
cookie_value = '__jsluid_s=a699ec62be5a522b936e11ad480e504d; Wt0e_5254_saltkey=Z61bBmsI; Wt0e_5254_lastvisit=1603367628; ppPartnerShow=1; ppPartner=1; __jsluid_h=1a6f73cd4cdc078a0f56c1193e05ad04; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221052813175920%22%2C%22%24device_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%7D; ASP.NET_SessionId=msh1yuynneanqhaucigc5wma; PPmoney.AUTH=32C63FAF912718B58A77AA2185F9989BE4718E050716C2CF6CA101678F78C5BAE8C46FC5AE4B243319BEDD4821711933AE6F6CD9DF07142F92A03785B61E97C00DA8C5AA5C4F7A447AAB7D37787FB12D89DE4253ACA7C81CE75798826D5789A03E4FBB2B; cj_uid=B85CB4FA5EC084E6B37E766441E66689; cj_user=92DB1D6D028767C862DF988D2444E4D2; __mscd3a__=0ro5dkcw; Wt0e_5254_sid=m5g78d; Wt0e_5254_lip=123.112.171.75%2C1604844481; Wt0e_5254_lastact=1604849646%09uc.php%09; Wt0e_5254_auth=8249j0qYjrNx5ZJw9%2B0P7FumZuXCOK8JxdFIkTHe9QS%2B4RNRyHfvi%2B8WecAR94hKdcxIwQMDONyP0TGTAYU9MXfiLQtj; sensorsInitUser=%7B%22NickName%22%3A%22%E6%9D%8E**%E5%A5%B3%E5%A3%AB%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.00%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A%222020%2F11%2F8%2023%3A34%3A01%22%2C%22Sex%22%3A2%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221052813175920_91E18282BD95BC1AEB0DD069EBA373DF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D; InitUser=%7B%22value%22%3A%7B%22NickName%22%3A%22%E6%9D%8E**%E5%A5%B3%E5%A3%AB%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.00%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A-6230%2C%22Sex%22%3A2%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221052813175920_91E18282BD95BC1AEB0DD069EBA373DF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D%2C%22expires%22%3A1604849826961%7D; __RequestVerificationToken=0JAhX6XwVLRksv1H4IxblL7wc2Rpk12e2N0024k3_7VQHrmiB3-wclcvWnDVQ0d1BSyZaw2'
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
