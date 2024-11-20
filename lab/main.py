unique_char_4_space="defiohf;qebio;gofhwe9-fpweffopefo"
with open('input/small.css', mode='r') as data:
    file_code=data.read()
    CODE=file_code
def noOfLines():
    return CODE.count('\n')
def replaceAllFromList(input:str,list_:list,char_to_replace_with:str):
    if input == '' or input == unique_char_4_space:
        return ''
    output=unique_char_4_space
    for each in list_:
        # output = unique_char_4_space 
        if(output==unique_char_4_space):
            output=input.replace(each,char_to_replace_with)
        else:
            output=output.replace(each,char_to_replace_with)
    return output

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
def writeInFile(str_=''):
    with open('ouput/without_whitespace/style.css',mode='w')as file:
        file.write(str_)
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

def noWhiteSpaces(code,return_=False,comments=False):
    no_comments=code
    if not comments:
        no_comments=removeComments(CODE)    # Doesn't make sense to have comments when no whitespaces it won't be visible
    no_whitespaces=myStrip(no_comments)
    if return_:
        return no_whitespaces
    with open('ouput/without_whitespace/style.css','w')as file:
        file.write(no_whitespaces)

def stylesToObject(code:str):
    """Code Works when semi-column added to last style when a selector has another selector within."""
    code_=myStrip(code)
    # code_=removeComments(code_)
    
    list_of_selectors=[]
    styles={}
    found_selector_name_end=False # found end of selector e.g "hr","h1","div", ".class-name","#id"
    found_a_style_name_start=False
    found_a_style_name_end=False # i.e ":"
    selector=''
    style_des_name='' #'background-color'
    style_des_value='' #'#FF0AAA'
    new_selector=''
    found_a_style_value_start=False
    i=0
    rin=0
    # print(code_)
    def inCommentStart(char='',i=0):
        """Check if is any of the char(s) that Starts the comment"""
        if char not in ['/','*']:
            return False
        elif (char == '/' and i+1 != len(code_) and code_[i+1] == '*')  or (char == '*' and i-1 != -1 and code_[i-1] == '/'):
            return True
        else:
            return False
    def isCommentEnd(char='',i=''):
        """Check if is the last char that Ends the comment"""
        if char != '/':
            return False
        elif char == '/' and i-1 != 0 and code_[i-1] == '*':
            return True
        else:
            return False
    def closeASelector():
        nonlocal new_selector,found_selector_name_end,selector,style_des_name,style_des_value
        if new_selector:
                new_selector=''
        else:    
            found_selector_name_end=False
            selector=''
        style_des_name=style_des_value=''
    print('hhhhhhhhhhhhh')
    inComment=False     #This var will be true at comment start till it sees comment end.
    # counter_for_first_two_comment_chars=0# to avoid adding first two '/' and '*' and add others in the comment e.g --> /* /* */
    children_selectors_and_their_childern=[]#a ordered list of nested selectors
    current = {} # key

    for char in code_:
        # print(char)
        # Using this if and elif statement cause it needs to stay at true till it hits the end of the comment
        if inCommentStart(char,i):
            inComment=True
            if style_des_name:
                #according to tests if style_des_name var is not empty that means the style isn't close before the comment in next line
                # i.e p{color:red\n /*comment*/}
                found_a_style_name_end=False
                if new_selector:    # for animations and selctor with parent selector
                    #ADD (maybe a While loop) feature for a recuring loop of sub child selectors
                    styles[selector][new_selector][style_des_name]=style_des_value
                else:
                    styles[selector][style_des_name]=style_des_value
                style_des_name= style_des_value=''
                # closeASelector() Don't close selector because it's about to add comment that belongs in the selector.
        elif isCommentEnd(char,i):
            inComment=False
        
        # print(inComment,char,'||||',i)
        # print(inCommentStart(char,i),char,'||||',i)
        # print(style_des_value,'|||',style_des_name,'<----')
        
        if inComment:
            style_des_value+=char
            # if counter_for_first_two_comment_chars 
            # print('IN COMMENT',char)
        elif isCommentEnd(char,i):
            # print(style_des_value,'|||',style_des_name,'<----')
            unique_comment_name='comment'+unique_char_4_space+str(i)
            if new_selector:
                #ADD loop mechanism for a selector with a child that has it's own children and on and on..
                styles[selector][new_selector][unique_comment_name]=style_des_value+'/'
                # Don't clear new_selector
            else:
                if selector=='':# for if comment is not inside a selector
                    styles[unique_comment_name]=style_des_value+'/'
                elif selector:
                    styles[selector][unique_comment_name]=style_des_value+'/'
            style_des_name=style_des_value=''
        elif not found_selector_name_end and char !='{':
            selector+=char
        elif not found_selector_name_end and char == '{':
            # print(22222,styles)
            styles[selector]={}
            current = styles[selector]
            # print(1111,current)
            # print(333333,styles)
            found_selector_name_end=True
        elif char == '{' and found_selector_name_end:    # for animations and selctor with parent selector
            #FIX Fails to add children selectors properly when ';' is added to last style
            # found_styles=';'.join(style_des_name.split(';')[0:-1])  #returns -->> e.g color: red; display: flex; and takes out h1
            # styles[selector][style_des_name]=found_styles
            #ADD a way to if fallback user those not close with semi-colomun before child selector
            print(2222,current,'||||',styles)
            print(style_des_name)
            new_selector=style_des_name
            # styles[selector][new_selector]={}
            # children_selectors_and_their_childern.append(new_selector)
            current[new_selector]={}
            # print(555555555,'||||',styles)

            # current = current[new_selector]
            # styles[selector] = current

            # print(styles)
            style_des_value=''
            style_des_name=''
            found_a_style_name_end=False
            print(3333,current,'----',styles)

        elif found_selector_name_end and not found_a_style_name_end and char not in [':','}']: # added (and each != ':') to move (elif found_a_style_name_start and each == ':':) section after this elif statement:
            style_des_name+=char
            found_a_style_name_start=True  
        elif found_a_style_name_start and char == ':':
            found_a_style_name_end=True
        elif found_a_style_name_end and (char != ';' and char != '}'):
            style_des_value+=char
            found_a_style_value_start=True            
        elif style_des_value and found_a_style_name_end and found_a_style_value_start and (char == ';' or char == '}'):
            found_a_style_name_end=False
            if new_selector:    # for animations and selctor with parent selector
                #ADD (maybe a While loop) feature for a recuring loop of sub child selectors
                # styles[selector][new_selector][style_des_name]=
                # styles[selector][new_selector][style_des_name]=style_des_value
                # for sub_selector in children_selectors_and_their_childern:
                    # styles[selector][sub_selector]
                print('suppose to assigns style value to subs here',style_des_name,'|||||',style_des_value)
                print('stuffffff',current,selector,new_selector)
                # current=style_des_value
                current[new_selector][style_des_name]=style_des_value
            else:
                print(777,styles)
                styles[selector][style_des_name]=style_des_value
                print(888,styles)
            style_des_name= style_des_value=''
            if char=='}':
                # print(111111,styles)
                closeASelector()
        elif found_selector_name_end and char == '}': 
            # print(styles)
            # if statement so it can come here if last written style does not have ";" and it's captured by `(char == ';' or (char == '}'))`
            # New comment i understand it's coming here to clear value of current selector i'm done with them.
            closeASelector()
        else:
            print(f'--------------PROBLEM with {char}------------') # Because are characters should be caught
        i+=1
    # print(styles)
    # print(styles['.search-box:has(input:focus)'].keys())
    for e in styles.keys():
          print(e)
    print('\n',styles['.search-box:has(input:focus)'].keys())
    return styles
stylesToObject(CODE)
runtime=300
def objectToStyle(code:dict):
    style=''
    styles_obj=code
    # i=0
    for selector, value in styles_obj.items():
        value__ = value
        # if type(value) == dict: 
        # print(selector)
        if 'comment' +unique_char_4_space in selector:
            # print(selector)
            # print(value)
            style+= value
        else:
            style+= selector + '{'
        # while type(value__) == dict and i<runtime:
        # if selector != 'comment' +unique_char_4_space:
            for a_style, value in value__.items():
                # print(a_style, value)
                value__=value
                if type(value) == str:
                    if 'comment' +unique_char_4_space in a_style:
                        style+=value
                    else:
                        style+= a_style + ':'+value+';'
                elif type(value) == dict: # it the value is a object then the key is a selector (i.e a_style var is a selector)
                        # style+='}'# incase there are stykes in the parent style before the child selector
                    style+=a_style+'{'
                    for sty, val in value__.items():
                        style+=sty+':'+val+';'
                    style+='}'
            style+='}'
            # i+=1
    writeInFile(style)
    return style
# objectToStyle(stylesToObject(CODE))


def formatNicely(code, strip=True):
    """Also removes empty selectors :) just a feature code runs 100% without it"""
    new_str=code
    if strip:
        new_str=myStrip(code)
    str_=''
    lenght_of_str = len(new_str)
    i=0
    for char in new_str:
        if (char == '*' and i+1 != lenght_of_str and new_str[i+1] == '/') or (char == '/' and i-1 != 0 and new_str[i-1] == '*'):# this identifies comments ending
            if char == '/':
                str_+=char+'\n\t'
                # in_comment =False
            else:
                str_+=char
                # in_comment=True
        elif char=='}':
            if i>2 and new_str[i-1]=='/' and new_str[i-2] =='*':    # checking if last written last closed comment
                # print(str_[-2])
                str_=str_[0:-2] +'\n'+char+'\n'
                # print(999)
                # str_+=char+'\n'
            else:
                str_+='\n'+char+'\n'
        elif str_ and any(str_[-1] == i for i in ['{',';']): #if last char before this was ; or }
            
            str_+='\n\t'+char
        else:
            str_+=char
        i+=1
    # print(amount_of_open_braces,amount_of_closed_braces)
    writeInFile(str_)#[1:-1]
# formatNicely(noWhiteSpaces(CODE,return_=True))
# formatNicely(objectToStyle(stylesToObject(CODE)),strip=0)
#FIX
