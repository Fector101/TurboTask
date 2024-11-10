import string as STR

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
