from util.generate_info_contact_html import generate_html_result
from util.generate_info_contact_csv import generate_credit_csv
from util.common_util import walk_file
import config.config as CONFIG

# csv文件目录
# 自助投目录
credit_generated_csv_folder = CONFIG.credit_generated_csv_folder
info_contact_result_folder = CONFIG.info_contact_result_folder
csv_analysis_failed_folder = CONFIG.csv_analysis_failed_folder
# 安心投目录
credit_generated_csv_folder2 = CONFIG.credit_generated_csv_folder2
info_contact_result_folder2 = CONFIG.info_contact_result_folder2
csv_analysis_failed_folder2 = CONFIG.csv_analysis_failed_folder2

if __name__ == "__main__":
    # # 第一步，生成csv文件
    # print('============csv文件生成开始============')
    # generate_credit_csv(credit_generated_csv_folder2)
    # print('============csv文件生成完成============')
    # 第二步，遍历csv文件生成结果
    csv_file_array = walk_file(credit_generated_csv_folder2)
    for file_path in csv_file_array:
        print('============开始解析：【' + file_path + '】 生成出借人信息、合同html============')
        generate_html_result(info_contact_result_folder2, csv_analysis_failed_folder2, file_path)
        print('============结束解析：【' + file_path + '】 生成出借人信息、合同html============')
