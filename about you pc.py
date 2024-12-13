import  platform
import socket
import os

def show_info():
    print("Информация о твоём компьютере следующая:")
    print(f"Имя компьютера: {socket.gethostname()}")
    print(f"Имя пользователя: {socket.getfqdn()}")
    print(f"Ваша опперационная система: {platform.system()}")
    print(f"Версия вашей операционной системы: {platform.version()}")
    print(f"Архитектура вашей системы: {platform.architecture()[0]}")
    print(f"Ваш процессор: {platform.processor()}")
    print(f"Платформа: {platform.platform()}")
    print(f"Номер и дата сборки: {platform.python_build()}")
    print(f"Ваш компилятор: {platform.python_compiler()}")
    print(f"Путь к нынешнему каталогу: {os.getcwd()}")
    input()

if __name__ =="__main__":
    show_info()

