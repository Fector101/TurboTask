from ..helper import failSafeRootPath,canReadandWritePermission,Colors,isFolderEmpty, moveFile
import os
def myStrip(code:str):
    """Removes unnesseccary white space and empty selectors. (div{})"""
    new_str=''
    i=0
    remove_space=False
    # code=replaceAllFromList(repr(code),[r'\t',r'\v',r'\n',r'\r',r'\f'],'')#.replace('\n','')
    # code=repr(code)
    code=code.replace('\n','')
    # code=removeComments(code)
    # print(code[0:30])
    # code=re.sub(r'[^\S\t\f\v\r\n]+ ','',code)
    lenght_of_str=len(code)
    checkpoints=['{',':',';','}']
    for char in code:
        if any(i == char for i in checkpoints):
            remove_space=True
            new_str=new_str.rstrip() 
            #removing space between h1 above open curlly braces e.g "h1 {"
            # OR trailing whitespace when used doesn't add ';' after style (width: 10px  /* background-color: transparent;) */
            if char=='{':
                new_str+=char
            elif char == '}' and new_str[-1]=='{': 
                # Removes empty selectors
                index_of_last_closed_braces = new_str.rfind('}')
                if index_of_last_closed_braces != -1:
                    new_str=new_str[0:index_of_last_closed_braces+1]
                else:
                    new_str+=char
            else:
                new_str+=char
        elif (char == '/' and i+1 != lenght_of_str and code[i+1] == '*') or (char == '*' and i-1 != -1 and code[i-1] == '/'):#/*
            # print(char, code[i+1], code[i+2], code[i+3], code[i+4], code[i+5], code[i+6], code[i+7], code[i+8], code[i+9], code[i+10], code[i+11], code[i+12])
            new_str=new_str.rstrip()
            # Strip trailing whitespace when used doesn't add ';' after style (width: 10px  /* background-color: transparent;) */
            new_str+=char
            remove_space=True
        # elif (char == '*' and i+1 != len(code) and code[i+1] == '/'):
        elif (char == '*' and i+1 != lenght_of_str and code[i+1] == '/') or (char == '/' and i-1 != -1 and code[i-1] == '*'):
            new_str+=char
            remove_space=True
        elif char == ' ' and remove_space:
            pass
        else:# and found_style_start:
            # if new_str and any(new_str[-1] == i for i in ['{',';']):
            #     new_str+='\t'+char
            # else:
            remove_space=False
            new_str+=char
        i+=1
    return new_str
def removeComments(code:str):
    if '/*' not in code:
        return code
    new_str=''
    found_comment_end=True
    i = 0
    if code.count('/*') != code.count('*/'):

        ...
    for char in code:
        if char == '/' and i+1 != len(code) and code[i+1] == '*':
            found_comment_end = False
        elif (char == '*' and i+1 != len(code) and code[i+1] == '/') or (char == '/' and i-1 != -1 and code[i-1] == '*'):
            found_comment_end=True
        elif found_comment_end:
            new_str+=char
        i+=1
    list_for_empty_return=['/','*','{']
    if any(i.replace(' ','') == new_str for i in list_for_empty_return):
        return ''
    else:
        return new_str


import typing
from dataclasses import dataclass, field
folders_to_ignore = ['node_modules', '.git','venv','myvenv','env']

class GroupFormat:
    """
    A template class demonstrating key Python class features.

    Attributes:
        attribute1 (type): Description of attribute1
        attribute2 (type): Description of attribute2
    """

    def __init__(self, main_folder='./'):
        """
        Initialize the class instance.

        Args:
            attribute1 (type, optional): Description. Defaults to None.
        """
        
        self.main_folder=failSafeRootPath(main_folder)
        self.errors_count=0
        self.errors=[]
        self.folders=[]
        # self.task_progress = new Progress()
        self.number_of_scanned_folders=0
        self.number_of_moved_files=0
        
        self._private_attribute = None  # Convention for private attributes
        self.__very_private_attribute = None  # Name mangling for stronger privacy
    def updateErrorInfo(self,error_obj,absolute_path):
        ...
    def getEndLog(self):
        return {
            "Number of scanned folders":self.number_of_scanned_folders,
            "Number of Moved Files":self.number_of_moved_files,
            'Errors':self.errors
        }
        
    def verifyPath(self):
        """Checks if folder exists, can read folder's content, can move files, 
        displays warning if folder directly in root path and can still can read and write

        Returns:
            boolean: If you can go ahead to scan Recursively
        """
        if os.path.exists(self.main_folder) and os.path.isdir(self.main_folder):
            
            folder_absolute_path = os.path.abspath(self.main_folder)
            if canReadandWritePermission(folder_absolute_path):
                drive_absolute_path = os.path.abspath(os.sep)
                folder_name=os.path.basename(self.main_folder)
                message = folder_absolute_path+' - Warning this is in Your storage Root' if os.path.join(drive_absolute_path,folder_name) == os.path.abspath(self.main_folder) else folder_absolute_path
                print(f"Root Folder: ${message}")
                return True
            else:
                print("Turbo doesn't have permission to Move Files in: "+folder_absolute_path)
                self.updateErrorInfo({},folder_absolute_path)
                return False
            
        else:
            print(f"{Colors.red_text(self.main_folder)} Folder does not exist.")
            self.updateErrorInfo({message:self.main_folder+" Folder does not exist"},self.main_folder)
            return False
        
        
    def addFolderToKeepLoop(self,current_path,folder_name):
        folder_not_empty = not isFolderEmpty(current_path)

        if folder_not_empty and folder_name not in folders_to_ignore:
            self.folders.append(current_path)
            # self.task_progress.updateTotal(1)
    
    def createGroupFolder(self,each):
        folder_name = os.path.join(self.main_folder,f"group {os.path.splitext(each)[1]}".strip())
        if not os.path.exists(folder_name):
            print(folder_name,'created')
            os.mkdir(folder_name)
        
        return folder_name
    
    def start(self):
        verified= self.verifyPath()
        if not verified:
            return

        user_input = input('Enter "y" to Proceed or "n" to Cancel: ').lower()
        if user_input != 'y':
            print("Operation cancelled GoodBye!!!")
            return
        
        self.folders = [self.main_folder]
        self.number_of_scanned_folders=0
        # print(self.folders,'||',current_folder,'||',list_of_filesNdFolders)
        
        for current_folder in self.folders:
            # print(current_folder)
            list_of_filesNdFolders = os.listdir(current_folder)
            self.number_of_scanned_folders+=1
            
            for each in list_of_filesNdFolders:
                current_path = os.path.abspath(os.path.join(current_folder, each))
                
                if os.path.isdir(current_path):
                    self.addFolderToKeepLoop(current_path,each)
                else:
                    folder_name = self.createGroupFolder(each)
                    print(current_path)
                    # moveFile(current_path,folder_name)
            
    def _protected_method(self):
        """
        A protected method (by convention, not strictly enforced).
        """
        pass

    @classmethod
    def class_method(cls, parameter):
        """
        A class method that can access and modify class state.

        Args:
            parameter (type): Description of parameter

        Returns:
            type: Description of return value
        """
        return None

    @staticmethod
    def static_method():
        """
        A static method that doesn't access instance or class state.
        """
        pass

    def __str__(self):
        """
        String representation of the object.

        Returns:
            str: A string describing the object
        """
        return f"MyClass(attribute1={self.attribute1}, attribute2={self.attribute2})"

    def __repr__(self):
        """
        Detailed string representation for debugging.

        Returns:
            str: A detailed string representation
        """
        return f"MyClass(attribute1={repr(self.attribute1)}, attribute2={repr(self.attribute2)})"
    
    