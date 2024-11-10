import sys
import os
import subprocess
import time
import shutil
import string as STR
import  random
from myModules import groupFiles
listOfFilesInDir=[]

def delEmptyAll(path:str='.'):
    for folder,sub,files in os.walk(path):
        if len(folder) > 2 and len(files) < 1 and folder != os.path.join(path,'System Volume Information'): # if path not '.'
            try:
                os.rmdir(folder)
            except Exception as e:
                # print('del error')
                pass
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
def rename1(currentName: str):
    """
    when a name is passed in it checks if it needs to be renamed to safe time,
    then the pattern is it adds ' - Copy' then checks and try to return else,

    :param currentName:
    :return:
    """
    listOfFilesInDir.sort()
    listOfFilesInDirLower = [each.lower() for each in listOfFilesInDir]
    if not (currentName.lower() in listOfFilesInDirLower):
        return currentName
    copyWord = ' - Copy'

    if '.' in currentName:
        indexOfDot = currentName.rfind('.')
        newName = currentName[:indexOfDot] + ' - Copy' + currentName[indexOfDot:]
        if not (newName.lower() in listOfFilesInDirLower):
            return newName
        else:
            newName = currentName[:indexOfDot] + ' - Copy (1)' + currentName[indexOfDot:]
            if not (newName.lower() in listOfFilesInDirLower):
                return newName


        i = 0
        while newName.lower() in listOfFilesInDirLower and i < len(listOfFilesInDirLower):
            each = listOfFilesInDirLower[i]
            keepingFormat = listOfFilesInDir[i]
            
            if newName.lower() in listOfFilesInDirLower and each == newName.lower():
                # print(newName)
                # print(each,'each')
                word_before_last_dot = keepingFormat[:each.rfind('.')]
                # print(word_before_last_dot)
                copy_word_and_number_btw = word_before_last_dot[word_before_last_dot.lower().rfind(' - copy ('):]
                # print(copy_word_and_number_btw)
                current_copy_no = parseInt(copy_word_and_number_btw)
                newName = f"{keepingFormat[:each.rfind(' - copy (') ]} - Copy ({current_copy_no+1}){keepingFormat[each.rfind('.'):]}"

            if newName.lower() not in listOfFilesInDirLower:
                return newName
            i += 1
    else:
        # print('no dot')
        newName = currentName + copyWord
        if not (newName.lower() in listOfFilesInDirLower):
            return newName
        i = 0

        while newName.lower() in listOfFilesInDirLower and i < len(listOfFilesInDirLower):
            if i < len(listOfFilesInDirLower):
                each = listOfFilesInDirLower[i]
                keepingFormat = listOfFilesInDir[i]

            else:
                each = newName
                keepingFormat = newName

            if each.lower() == newName.lower():

                alreadycopiedWord = 'Copy'
                alreadycopiedMoreThanOnceWord = ' - Copy ('

                index = newName.rfind(alreadycopiedWord)
                # ind_frmEach = keepingFormat.rfind(alreadycopiedWord)
                # print(keepingFormat,index,'||',ind_frmEach)

                index1 = newName.rfind(alreadycopiedMoreThanOnceWord)
                # print(index1,'{{',ind_frmEach1)
                # print(index, index1)
                # print(keepingFormat, '||', newName)
                # print(newName.endswith('Copy'),newName)
                if newName.endswith('Copy'):  # alreadycopiedWord cause no Dot (.) not file format
                    index = newName.rfind(copyWord) + len(copyWord)
                    newName = newName[:index] + f' (1)'
                else:
                    ind_frmEach1 = keepingFormat.rfind(alreadycopiedMoreThanOnceWord)
                    num_frmEach = parseInt(keepingFormat[ind_frmEach1:])  # .rsplit('.')[0])
                    if newName[index:] =='':
                        suffix=''
                    else:
                        suffix=' - '+newName[index:]
                    newName = newName[:index1] + f' - Copy ({num_frmEach + 1})' #+ suffix#.rsplit('.')[-1]
                    # print(newName[index1:],'piwsw')

            i += 1

    # To Be Safe
    if newName.lower() in listOfFilesInDirLower:
        if '.' in newName:
            newName=newName.split('.')[0] +randomName() +'.' +newName.split('.')[-1]
        else:
            newName=newName+randomName()
    return newName

def sort():
    global listOfFilesInDir #Important
    folders=['.']
    while len(folders):
        pathQ=folders[0]

        list_of_filesNdFolders=os.listdir(pathQ)
        for each in list_of_filesNdFolders:
            currentPath= os.path.join(pathQ ,each)
            if os.path.isdir(currentPath):
            
                bool=0
                try:
                    bool = len(os.listdir(currentPath))
                except:
                    bool=0
                # let pathInList =skipFolders.includes(each)||skipFolders.includes(filePath)// filePath is folder path here
                group_in_name= 'group' in currentPath.lower()
                if bool and not group_in_name:
                    folders.append(currentPath)
            else:
                folder_name = f'group {each[each.rfind('.'):]}'.strip()
                
                if folder_name and (not os.path.exists(folder_name)):
                    os.mkdir(folder_name)
                listOfFilesInDir=os.listdir(folder_name)
                
                if os.path.exists(os.path.join(folder_name,each)):
                    try:
                        # print(type(err).__name__)# try this when there data
                        # In would get error type
                        # print(f"Destination path '{os.path.join(folder_name,each)}' already exists"==err)
                        # print(f"Destination path '{os.path.join(folder_name,each)}' already exists",err)
                        new_file_name = os.path.join(folder_name,rename1(str(each)))
                        os.rename(currentPath,new_file_name)
                        shutil.move(new_file_name,folder_name)
                    except:...
                else:
                    try:
                        shutil.move(currentPath, folder_name)
                    except Exception as err:
                        ...                        
        folders=folders[1:]
        delEmptyAll(pathQ)
        
        
possible_points=['_-_']
by_season=False

def buildPossible(if_by_season):
    def bySeason():
        possible_points.extend(['s'+str(each) for each in list(range(1, 25))])
        possible_points.extend(['s '+str(each) for each in list(range(1, 25))])

        possible_points.extend(['s'+str(each).zfill(2) for each in list(range(1, 25))])
        possible_points.extend(['s '+str(each).zfill(2) for each in list(range(1, 25))])
        
        possible_points.extend(['season '+str(each) for each in list(range(1, 25))])
        possible_points.extend(['season'+str(each) for each in list(range(1, 25))])

        possible_points.extend(['season '+str(each).zfill(2) for each in list(range(1, 25))])
        possible_points.extend(['season'+str(each).zfill(2) for each in list(range(1, 25))])
    if if_by_season == False:
        bySeason()
    else:
        global by_season
        by_season=True
        possible_points.pop()
        possible_points.extend(['episode'+str(each).zfill(2) for each in list(range(1, 25))])
        possible_points.extend(['episode '+str(each).zfill(2) for each in list(range(1, 25))])
        
        possible_points.extend(['episode '+str(each) for each in list(range(1, 25))])
        possible_points.extend(['episode'+str(each) for each in list(range(1, 25))])

        possible_points.extend(['episode-'+str(each) for each in list(range(1, 25))])

        possible_points.extend(['e'+str(each) for each in list(range(1, 25))])
        possible_points.extend(['e '+str(each) for each in list(range(1, 25))])

        possible_points.extend(['e'+str(each).zfill(2) for each in list(range(1, 25))])
        possible_points.extend(['e '+str(each).zfill(2) for each in list(range(1, 25))])

        
        bySeason()
        
def tryFind(string:str):
    found_point=None
    char=None
    forSeason__=False

    for each in possible_points:
        if type(found_point)==int and found_point != -1:
            break
        found_point = string.rfind(each)
        if found_point != -1:
            char = each
            if 's' in each and 'ep' not in each and by_season:
                forSeason__=True
                found_point+=len(each)
            # found_point+=len(each)
            # print(each,found_point)


    if type(found_point)!=int or found_point == -1:
        found_point = None
        char = None
    return {'num':found_point,'chr':char,'forSeasonWrk':forSeason__}

def folderLaw(name__:str):
    name__=name__.replace('_',' ').strip().title()
    if name__[-1]=='.':
        name__=name__[:-1].strip()
    return alikeNames(name__)
alikeList=[]
def alikeNames(name__:str):
    oldName=name__
    name__=name__.replace(' ','').replace('.','').replace('-','').replace('_','').lower().strip()
    for eachList in alikeList:
        count=0
        score=0
        for eachLetter in name__: # for eachLetter in ['realname', 'Real Name'][0]:
            try:
                if eachLetter == eachList[0][count]:
                    score+=1
            except IndexError:
                pass
            count+=1

        if score == len(name__):# or score - 1 == len(name__) or score - 2 == len(name__):
            return eachList[1]

    alikeList.append([name__,oldName])
    return oldName

def myShowNameDecoded(name:str):
    name=name.lower()
    newName=''

    
    if by_season and '_-_'in name:
        name=name[:name.rfind('_-_')]
        sliceFrm=tryFind(name)

        if sliceFrm['forSeasonWrk']:
            return folderLaw(name[:sliceFrm['num'] ])
        return folderLaw(name[:sliceFrm['num'] ])

    elif by_season and '_-_' not in name:
        sliceFrm=tryFind(name)
        if sliceFrm['num'] != None:
            newName= folderLaw(name[:sliceFrm['num'] ])
            return newName
        else:
            return None

    if '_-_'in name:
        return folderLaw(name[:name.find('_-_')])

    sliceFrm=tryFind(name)
    if sliceFrm['num'] != None:
        
        return folderLaw(name[:sliceFrm['num'] ])
    else:
        return None #name



def randomName():
    def r():
        return random.choice(STR.ascii_letters.replace('.',''))
    return r()+r()+r()+r()+r()+r()+r()+r()+r()+'BLOCK'

def sortSeason():
    if len(sys.argv) > 1 and sys.argv[1].lower() == 's':
        # print(len(sys.argv),sys.argv)
        # if sys.argv[1].lower() == 's':
        buildPossible('s')
    else:
        buildPossible(False)
    count=1
    
    # current_directory=os.getcwd()
    # folx='D:\group .mp4\group .mp4'
    global listOfFilesInDir
    OMEGA=r'.\GROUP __ '+randomName()
    myFolders = [r'.\System Volume Information',]
    if not os.path.isdir(OMEGA):
        os.mkdir(OMEGA)
    OMEGA_with_Slash=f'{OMEGA}/'
    for folder,sub,files in os.walk('.'):
        if len(files) > 0 and OMEGA not in folder:#folder not in myFolders:# and 'group' not in folder:
            # print(myFolders,'||',folder)
            for each in files:
                # listOfFilesInDir.append(f"{each}")
                folder_name = 'group ' + each[each.rfind('.'):]
                folder_name = OMEGA_with_Slash+ folderLaw(folder_name)
                # print(folder,folder_name,os.path.isdir(folder_name))
                try:
                    if not os.path.isdir(folder_name):
                        os.mkdir(folder_name)
                        myFolders.append(folder)
                    if folder not in myFolders:
                        myFolders.append(folder)
                except Exception as e:
                    # print(folder,'folder var')
                    # print(os.getcwd(),'cwd var')
                    print('error',e)
                    pass
                currentFilesList = os.listdir(folder_name)

                show_name = myShowNameDecoded(each)
                # print(show_name)
                if show_name != None:
                    show_name=OMEGA_with_Slash+show_name
                    # print('show name')
                    if not os.path.isdir(show_name):
                        # print('made')
                        myFolders.append(folder)
                        try:
                            os.mkdir(show_name)
                        except Exception as e:
                            # print(e)
                            # print(show_name, '<---show_name1')

                            pass
                    if f'./{show_name}' not in myFolders:
                        myFolders.append(f'./{show_name}')
                        print(show_name)
                    # currentFilesList=os.listdir(show_name)
                # print(show_name,folder_name,folder)
                # print(currentFilesList,folder)
                if '.nomedia' not in each:# and each not in currentFilesList:


                        # if not os.path.exists(show_name+'/'+each):
                        # print(show_name)
                    if show_name:
                        listOfFilesInDir = os.listdir(show_name) # For rename1 function needs list of current dir your'e moving too
                        try:
                            # +'/'+folder
                            shutil.move(f"{folder}/{each}", show_name)
                        except Exception as e:
                            # print(e)
                            # print(show_name,'<---show_name2')
                            new_file_name = f"{folder}/" + rename1(f"{each}")
                            # print(new_file_name,'HAND',folder+'/'+each)

                            # new_file_name = f"{folder}/ {each[0: each.rfind('.')]} copy{count} {each[each.rfind('.'):]}"

                            # print(new_file_name,'new',err)
                            # print(f"{folder}/{each}", '||', new_file_name)
                            # print('Already1')

                            os.rename(f"{folder}/{each}", new_file_name)
                            shutil.move(new_file_name, show_name)
                            # print(e,folder,'cwd')
                            # print(os.path.exists(current_directory+'/'+folder))
                    if show_name==None:
                        listOfFilesInDir = os.listdir(folder_name) # For rename1 function needs list of current dir your'e moving too
                        try:
                            # if not os.path.exists(folder_name+'/'+each):
                            shutil.move(f"{folder}/{each}", folder_name)
                        except Exception as err:

                            new_file_name = f"{folder}/"+rename1(f"{each}")
                            # new_file_name = f"{folder}/ {each[0: each.rfind('.')]} copy{count} {each[each.rfind('.'):]}"
                            # print(new_file_name,'HAND',folder+'/'+each)
                            try:
                                os.rename(f"{folder}/{each}",new_file_name)
                                shutil.move(new_file_name, folder_name)
                            except:
                                pass


    print('Hi i\'m sort1') 
    delEmptyAll()
start = None
def cal_files_duration():
    global start

    videos = []
    count = 1
    list_of_3_len_acceptable_formats = ['.mp4','.mp3', '.mkv', '.avi', '.mov', '.flv', '.vob', '.ogg', '.ogv','.drc','.mts','.wmv','.yuv','viv','.asf','.mpg','.mp2','.mpe','.mpv','.3gp','.3g2', '.mkv', '.flv', '.mov']
    list_of_4_len_acceptable_formats = ['.webm','.mpeg']
    for each_file in os.listdir('.'):
        # if '.mp4' in each_file:
        if any(each_file[-4:] in each for each in list_of_3_len_acceptable_formats) or any(each_file[-5:] in each for each in list_of_4_len_acceptable_formats):    
        # if any(each_file[-4:] in each for each in ['.mp4', '.mkv', '.avi', '.mov']) or '.webm' in each_file:    
            # print(each_file[-4:])        
        # if any(item in ['/', '*', '+', '-'] for item in [each for each in var]):            
            print(f"{count}: {each_file}")
            videos.append(each_file)
            count+=1
    if len(videos) == 0:
        print('No Video/Audio in folder')
        return
    print(f"There are {len(videos)} readable files")

    def cal():
        global start
        secs = 0
        end = len(videos)
        print('')
        print(f'Enter any number from 1 - {len(videos)} or <ctrl + c> to End')#, [each+1 for each in range(len(videos))])
        try:
            start = input('Start at what index: ')
        except KeyboardInterrupt:
            start = 'end'
            print('\nCtrl+C was pressed. Exiting...')
            return
        if start in [f'{each+1}' for each in range(len(videos))]:
            start = int(start) - 1
        elif '-' in start:
            cup=start
            start=int(cup.split('-')[0].strip())-1
            # if start==1:
                # start=0
            end=int(cup.split('-')[-1].strip())

        if start in [0, ''] and end==len(videos):
            if start == '':
                start = None
            print(f'Checking all... ({len(videos)}) Files.')
        elif start == max([each for each in range(len(videos))]):
            print('Checking 1 File...')
        else:
            print(f'Checking {len([each for each in videos[start: end]])} Files..')
        for each in videos[start: end]:
            # if '.mp4' in each:
            # try:
            #     result1 = subprocess.check_output(cmd)
            # except:
            #     print(cmd)
            try:
                result = subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',each],
                                            stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                secs += float(result.stdout.decode('utf-8'))
            except:
                each = str(each).title()
                print(f'{each} doesn\'t have a Duration')
                pass

        print(secs,'secs')

        if secs >= 3600:
            h, remainder = divmod(int(secs),3600)
            m,s= divmod(remainder,60)
            if len(str(h)) < 2:
                h = '0'+str(int(h))
            if len(str(m)) < 2:
                m = '0'+str(int(m))
            if len(str(s)) < 2:
                s = '0'+str(s)
                
            print(f'{h}:{m}:{s} hrs')
        #    print(f'{int(h)}:{int(m)}:{int(s)}')
            # print(time_,'hrs')    
        elif secs < 3600:
            time_= time.strftime("%H:%M:%S",time.gmtime(secs))

            print(time_,'mins')        
        elif secs < 60:
            time_= time.strftime("%H:%M:%S",time.gmtime(secs))

            print(time_,'secs')
    while start != 'end':
        start = None
        cal()

def main_():
    ans = ''
    fun_names = ['create', 'create_dir']
    try:
        while ans.lower() not in ['create', 'create_dir', 'vids']:
            ans = input("--> Enter 'create' to create py file.\n--> Enter 'create_dir' to create py with folder or folders.\n--> Or 'durate' to check the duration of all videos in a folder.\n--> Enter Here: ")
            if ans.lower() == 'create':
                try:
                    file_name = input("Input file name #e.g(test.py): ")
                    with open(f"{file_name}", mode='w') as new_file:
                        print(f"Successfully created '{file_name}'.")
                except KeyboardInterrupt:
                    print('\nCtrl+C was pressed. Exiting...')
            elif ans.lower() == 'durate':
                cal_files_duration()
            elif ans.lower() == 'create_dir':
                create_with_specified_dir_()
            else:
                print(f'\n\n\n--> Enter {fun_names[0]}, {fun_names[1]} or (End or press ctrl+c) to quit.\n')

            if ans.title() == 'End':
                print('Goodbye.')
                break
    except KeyboardInterrupt:
        print('\nCtrl+C was pressed. Exiting...')
        print('Goodbye.')


def create():
    # if len(sys.argv) > 1:
    #     file_name = sys.argv[1]
    #     print(sys.argv)
    #     with open(f"{file_name}", mode='w') as new_file:
    #         print(f"{file_name} created.")
    # pass

    # if len(sys.argv) > 1:
    # print('st',sys.argv)
    # command = sys.argv[1]
    # if command == 'create':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        with open(f"{file_name}", mode='w') as new_file:
            print(f"Successfully created '{file_name}'.")
    else:
        try:
            file_name = input("Input file name #e.g(test.py): ")
            with open(f"{file_name}", mode='w') as new_file:
                print(f"Successfully created '{file_name}'.")
        except KeyboardInterrupt:
            print('\nCtrl+C was pressed. Exiting...')
    # elif command == 'create_ws_dir':#create_with_specific_dir
    #     if len(sys.argv) > 1:
    #         dir_nd_file_name = sys.argv[2]
    #         with open(f"{dir_nd_file_name}", mode='w') as new_file:
    #             print(f"{dir_nd_file_name} created.")
    #     else:
    #         try:
    #             file_name = input("Input file name #e.g(test.py): ")
    #             with open(f"{dir_nd_file_name}", mode='w') as new_file:
    #                 print(f"{dir_nd_file_name} created.")
    #         except KeyboardInterrupt:
    #             print('\nCtrl+C was pressed. Exiting...')


def create_with_specified_dir_():
    # given_dir = "parent_folder/child_folder/sub_folder/test.py"
    given_dir = input("input directory or directories and py file name (e.g parent_folder/test.py) or ("
                      "parent_folder/child_folder/sub_folder/test.py)\n-->Here: ")
    slash_index = given_dir.rfind('/')
    no_of_slash = given_dir.count('/')
    dir_length = len(given_dir) - 1

    def folders_file_name(g_dir):
        folds_dir_list = g_dir.split('/')[:-1]  # [start: end before]
        pyfile_name_ = g_dir.split('/')[-1]
        folders_dir = ''
        for each in folds_dir_list:
            folders_dir += f'{each}/'
        return folders_dir, pyfile_name_

    if no_of_slash > 1:
        if slash_index == dir_length:
            pass
        else:
            try:
                folds_dir = folders_file_name(given_dir)[0]
                pyfile_name = folders_file_name(given_dir)[1]

                os.makedirs(folds_dir)  # make folders
                with open(f"{folds_dir}{pyfile_name}", mode='w') as new_file:
                    print(f"{pyfile_name} Successfully created in {folds_dir} Nested folders.")

            except FileExistsError:
                folds_dir = folders_file_name(given_dir)[0]
                pyfile_name = folders_file_name(given_dir)[1]
                print(f"Folder '{folds_dir}' already exists.")
                with open(f"{folds_dir}{pyfile_name}", mode='w') as new_file:
                    print(f"'{pyfile_name}' created in {folds_dir}.")

            except Exception as e:
                print(f"Error creating folders: {e}")
    else:
        try:
            folder_dir = folders_file_name(given_dir)[0]
            pyfile_name = folders_file_name(given_dir)[1]

            os.mkdir(folder_dir)  # make folder
            with open(f"{folder_dir}{pyfile_name}", mode='w') as new_file:
                print(f"'{pyfile_name}' Successfully created in '{folder_dir}'.")
        except FileExistsError:
            folder_dir = folders_file_name(given_dir)[0]
            pyfile_name = folders_file_name(given_dir)[1]

            print(f"Folder '{folder_dir}' already exists.")
            with open(f"{folder_dir}{pyfile_name}", mode='w') as new_file:
                print(f"'{pyfile_name}' Successfully created in '{folder_dir}'.")
        except Exception as e:
            print(f"Error creating folder: {e}")


if __name__ == "__main__":
    # create()
    # cal_files_duration()
    print('Hello from Fabian!')
