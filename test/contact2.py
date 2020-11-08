import requests


def write_file(html_content, file_name, encoding, mode):
    """
    写文件,默认操作类型为w，编码为GBK
    :param html_content:文件内容
    :param file_name:文件名
    :param encoding:编码
    :param mode:操作类型
    :return:
    """
    # 新建一个文件名 ,注意文件格式的编码和 获取的编码 要一致，不然出现乱码问题
    file = open(file_name, mode, encoding=encoding)
    for i in html_content:
        # 将数据写入文件
        file.write(i)
    # 关闭文件
    file.close()


url_array = [
    'https://www.ppmoney.com/stepup/investcontract?investId=2674203&assetId=CB6C520A235781408986043F44CC377CBBF854E0D67788D6&shareId=755424912940077056&type=2&projectType=104043&assetType=10',
    'https://www.ppmoney.com/stepup/investcontract?investId=2674203&assetId=CB6C520A235781408986043F44CC377CBBF854E0D67788D6&shareId=755424912940077056&type=2&projectType=104043&assetType=10',
    'https://www.ppmoney.com/stepup/investcontract?investId=2679152&assetId=25FDF4553DC0AE2E34800120C161900DD333B03F82D25DA2&shareId=897983541680144454&type=2&projectType=104043&assetType=10',
    'https://www.ppmoney.com/stepup/investcontract?investId=2679152&assetId=28EAEB7C61971D30A9B3376412FC8DD02EA7B53BAEAC4544&shareId=899362718186602498&type=2&projectType=104043&assetType=10&transfereeInvestId=2679152&reInvestId=null&assignorId=13234668',
    'https://www.ppmoney.com/stepup/investcontract?investId=2679152&assetId=28EAEB7C61971D30A9B3376412FC8DD02EA7B53BAEAC4544&shareId=899362718186602498&type=2&projectType=104043&assetType=10&transfereeInvestId=2679152&reInvestId=null&assignorId=13059641',
    'https://www.ppmoney.com/stepup/investcontract?investId=2679152&assetId=F72F9689002E9BA35727EB69E3CE36863959B318BDD191F1&shareId=899727708437479454&type=2&projectType=104043&assetType=10',
    'https://www.ppmoney.com/stepup/investcontract?investId=2679152&assetId=303799C9E91B913161D64A94E4A6431CFD8FE56158F3D198&shareId=901310991877144583&type=2&projectType=104043&assetType=10'
]
url = "https://www.ppmoney.com/stepup/investcontract?investId=2674203&assetId=CB6C520A235781408986043F44CC377CBBF854E0D67788D6&shareId=755424912940077056&type=2&projectType=104043&assetType=10"
payload = {}
headers = {
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
    'Cookie': '__jsluid_s=a699ec62be5a522b936e11ad480e504d; Wt0e_5254_saltkey=Z61bBmsI; Wt0e_5254_lastvisit=1603367628; ppPartnerShow=1; ppPartner=1; __jsluid_h=1a6f73cd4cdc078a0f56c1193e05ad04; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221052813175920%22%2C%22%24device_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22175505de099ab5-05f2b97e80c022-333769-2073600-175505de09a773%22%7D; ASP.NET_SessionId=msh1yuynneanqhaucigc5wma; PPmoney.AUTH=32C63FAF912718B58A77AA2185F9989BE4718E050716C2CF6CA101678F78C5BAE8C46FC5AE4B243319BEDD4821711933AE6F6CD9DF07142F92A03785B61E97C00DA8C5AA5C4F7A447AAB7D37787FB12D89DE4253ACA7C81CE75798826D5789A03E4FBB2B; cj_uid=B85CB4FA5EC084E6B37E766441E66689; cj_user=92DB1D6D028767C862DF988D2444E4D2; __mscd3a__=0ro5dkcw; Wt0e_5254_sid=m5g78d; Wt0e_5254_lip=123.112.171.75%2C1604844481; Wt0e_5254_lastact=1604849646%09uc.php%09; Wt0e_5254_auth=8249j0qYjrNx5ZJw9%2B0P7FumZuXCOK8JxdFIkTHe9QS%2B4RNRyHfvi%2B8WecAR94hKdcxIwQMDONyP0TGTAYU9MXfiLQtj; sensorsInitUser=%7B%22NickName%22%3A%22%E6%9D%8E**%E5%A5%B3%E5%A3%AB%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.00%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A%222020%2F11%2F8%2023%3A34%3A01%22%2C%22Sex%22%3A2%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221052813175920_91E18282BD95BC1AEB0DD069EBA373DF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D; InitUser=%7B%22value%22%3A%7B%22NickName%22%3A%22%E6%9D%8E**%E5%A5%B3%E5%A3%AB%22%2C%22NotReadLetterCount%22%3A0%2C%22Amount%22%3A%220.00%22%2C%22IsAdmin%22%3Afalse%2C%22AdminUrl%22%3A%22%22%2C%22NowTime%22%3A-6230%2C%22Sex%22%3A2%2C%22IsVip%22%3Afalse%2C%22RegNum%22%3A%221052813175920_91E18282BD95BC1AEB0DD069EBA373DF%22%2C%22IsShowNewHandProject%22%3Atrue%2C%22UserRiskLevel%22%3A5%2C%22UserRiskLevelName%22%3A%22%E4%BF%9D%E5%AE%88%E5%9E%8B%22%7D%2C%22expires%22%3A1604849826961%7D; __RequestVerificationToken=0JAhX6XwVLRksv1H4IxblL7wc2Rpk12e2N0024k3_7VQHrmiB3-wclcvWnDVQ0d1BSyZaw2'
}

# response = requests.request("GET", url_array[0], headers=headers, data=payload)
# write_file(response.text, 'test.html', response.encoding, 'w')

for url in url_array:
    response = requests.request("GET", url, headers=headers, data=payload)
    write_file(response.text, str(url_array.index(url) + 1) + 'test.html', response.encoding, 'w')
