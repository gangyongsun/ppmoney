import os

import platform

print(os.cpu_count())
print(os.name)
print(os.environ)

platform.system()  # 获取系统类型
platform.platform()  # 获取操作系统名称及版本号，'Windows-10-10.0.17134-SP0'
platform.version()  # 获取操作系统版本号，'10.0.17134'
platform.architecture()  # 获取操作系统的位数，('64bit', 'WindowsPE')
platform.machine()  # 计算机硬件架构，'AMD64'
platform.node()  # 计算机的网络名称，'TDM'
platform.processor()  # 计算机处理器信息，'Intel64 Family 6 Model 158 Stepping 9, GenuineIntel'
platform.uname()  # 包含上面所有的信息汇总，
