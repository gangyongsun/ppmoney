import platform
import os

# print(os.environ['HOME'])
# print(os.path.expandvars('$HOME'))
# print(os.path.expanduser('~'))
#
# # ouput system type and version info
# print("platform.machine()=%s", platform.machine())
# print("platform.node()=%s", platform.node())
# print("platform.platform()=%s", platform.platform())
# print("platform.processor()=%s", platform.processor())
# print("platform.python_build()=%s", platform.python_build())
# print("platform.python_compiler()=%s", platform.python_compiler())
# print("platform.python_branch()=%s", platform.python_branch())
# print("platform.python_implementation()=%s", platform.python_implementation())
# print("platform.python_revision()=%s", platform.python_revision())
# print("platform.python_version()=%s", platform.python_version())
# print("platform.python_version_tuple()=%s", platform.python_version_tuple())
# print("platform.release()=%s", platform.release())
# print("platform.system()=%s", platform.system())
# # print("platform.system_alias()=%s", platform.system_alias())
# print("platform.version()=%s", platform.version())
# print("platform.uname()=%s", platform.uname())

import sys

# print(sys.platform)
# 系统类型
os_type = platform.system()
if os_type == 'Windows':
    print(os_type)
elif os_type == 'Mac':
    print(os_type)
else:
    print('others')
#
# if sys.platform.startwith('linux'):
#     # linux 代码
#     pass
# elif sys.platform.startwith('freebsd'):
#     # freebsd 代码
#     pass
