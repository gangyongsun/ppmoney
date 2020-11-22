import socket
import getpass

user_name = getpass.getuser()  # 获取当前用户名
hostname = socket.gethostname()  # 获取当前主机名

print(type(user_name))

print('C:\\Users\\' + user_name + '\\AppData\Local\Temp\\')

print(hostname)
print(user_name)
