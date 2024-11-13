import string as STR
import os
from colorama import Fore, Style, init as coloramaInit
coloramaInit()

def greenText(text):
    return f"{Fore.LIGHTGREEN_EX}{text}{Style.RESET_ALL}"

def redText(text):
    return f"{Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"

def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(f"Failed to create directory '{path}': {e}")


def readFile(input_css_file_path):
    try:
        with open(input_css_file_path, mode='r') as data:
            return data.read()
    except Exception as e:
        if type(e).__name__ == "FileNotFoundError":
            print(f"<Error - {redText(input_css_file_path)} Doesn't Exist>")
        else:
            print(f"Failed to Read File '{redText(input_css_file_path)}': {e}")
        return 'error--33*/901438-*--2324'    

def writeFile(content,file_path,good_msg=f"<Dev> - Default Success Msg ",error_msg="<Dev> - Default Error Msg"):
    try:
        folder_path=os.path.dirname(file_path)
        if folder_path:
            create_directory(folder_path)
        with open(file_path,'w')as file:
            file.write(content)
        print(good_msg)
    except Exception as e:
        print(error_msg)
        
def parseStr(string: str):
    nums=''.join([str(each) for each in range(0,10)])
    str_ = ''
    for each in string:
        if each not in nums:
            str_ += each
    return str_.strip()

def parseInt(string: str):
    ii = ''
    for each in string:
        if each not in ['-', ' ', '(', ')']:
            ii += each
    ii = ii.strip(STR.ascii_letters + '-').strip()
    if ii == '':
        return 0
    return int(ii)
