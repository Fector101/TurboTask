from ..helper import failSafeRootPath

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

class GroupFormat:
    """
    A template class demonstrating key Python class features.

    Attributes:
        attribute1 (type): Description of attribute1
        attribute2 (type): Description of attribute2
    """

    def __init__(self, Basedir='./'):
        """
        Initialize the class instance.

        Args:
            attribute1 (type, optional): Description. Defaults to None.
        """
        
        self.Basedir=failSafeRootPath(Basedir)
        print(self.Basedir)
        self.errors_count=0
        self.errors=[]
        self.folders=[]
        # self.task_progress = new Progress()
        self.number_of_scanned_folders=0
        self.number_of_moved_files=0
        
        self._private_attribute = None  # Convention for private attributes
        self.__very_private_attribute = None  # Name mangling for stronger privacy

    def start(self):
        """
        A public method demonstrating basic functionality.

        Args:
            param1 (type): Description of parameter

        Returns:
            type: Description of return value
        """
        # Method implementation
        return None

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
    
    