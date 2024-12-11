import string as STR
from colorama import Fore, Style, init as coloramaInit

import os
import shutil

coloramaInit()




class Colors:
    """
    A utility class for styling text with color using the colorama library.

    Provides static methods to return text wrapped in ANSI escape codes for specific colors.
    """
    GREEN_STYLE = Fore.LIGHTGREEN_EX + "{}" + Style.RESET_ALL
    RED_STYLE = Fore.LIGHTRED_EX + "{}" + Style.RESET_ALL
    YELLOW_STYLE = Fore.LIGHTYELLOW_EX + "{}" + Style.RESET_ALL

    @staticmethod
    def green_text(text):
        if not isinstance(text, str):
            raise TypeError("The 'text' parameter must be a string.")
        return Colors.GREEN_STYLE.format(text)

    @staticmethod
    def red_text(text):
        if not isinstance(text, str):
            raise TypeError("The 'text' parameter must be a string.")
        return Colors.RED_STYLE.format(text)

    @staticmethod
    def yellow_bright(text):
        if not isinstance(text, str):
            raise TypeError("The 'text' parameter must be a string.")
        return Colors.YELLOW_STYLE.format(text)

# def main():
#     """Main function for demonstrating the Color class."""
#     print(Color.green_text("This is green text"))
#     print(Color.red_text("This is red text"))
#     print(Color.yellow_bright("This is bright yellow text"))




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
            print(f"<Error - {Colors.red_text(input_css_file_path)} Doesn't Exist>")
        else:
            print(f"Failed to Read File '{Colors.red_text(input_css_file_path)}': {e}")
        return None

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

def failSafeRootPath(inputted_path):
    """Returns right format for root path or inputted path

    Args:
        inputted_path (string): Unformatted path from user

    Returns:
        string: Right Format of Root path or inputted path
    """
    new_path = inputted_path
    if inputted_path in [" ", "", '/']:
        print(Colors.yellow_bright(f"Waring use './' as Based Directory, not '{inputted_path}'"))
        new_path = "."

    return new_path


def canReadandWritePermission(absolute_path):
    """Checks read and write permission for File/Folder

    Args:
        absolute_path (path): Location of File/Folder

    Returns:
        boolean: Either true or false
    """
    return os.access(absolute_path,os.R_OK) and os.access(absolute_path,os.W_OK)

def isFolderEmpty(folder_path):
    try:
        return next(os.scandir(folder_path), None) is None
    except:     #Incase Folder is Moved
        return False
    
    

def move_file_to_directory(src, dest_dir):
    file_name = os.path.basename(src)
    dest = os.path.join(dest_dir, file_name)

    # Check if the file already exists in the destination directory
    counter = 1
    while os.path.exists(dest):
        extname = os.path.splitext(file_name)[1]  # Get the file extension
        basename = os.path.splitext(file_name)[0]  # Get the base name without extension
        new_file_name = f"{basename} ({counter}){extname}"
        dest = os.path.join(dest_dir, new_file_name)
        counter += 1
    shutil.move(src, dest)
    