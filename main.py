from util.generate_info_contact_html import generate_html_result
# from util.generate_info_contact_csv import generate_credit_csv
from util.common_util import walk_file
import config.config as CONFIG

# csv文件目录
credit_generated_csv_folder = CONFIG.credit_generated_csv_folder

if __name__ == "__main__":
    # # 第一步，生成csv文件
    # print('============csv文件生成开始============')
    # # generate_credit_csv()
    # print('============csv文件生成完成============')
    # 第二步，遍历csv文件生成结果
    csv_file_array = walk_file(credit_generated_csv_folder)
    for file_path in csv_file_array:
        print('============开始解析：【' + file_path + '】 生成出借人信息、合同html============')
        generate_html_result(file_path)
        print('============结束解析：【' + file_path + '】 生成出借人信息、合同html============')
    # generate_html_result(r'C:\ppmoney_doc\自助投\自助投[20180425-23].csv')
