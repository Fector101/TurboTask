#deactivate start button when function starts
# prompt to run as admin when special parts added
# TODO Check if user has permission to file before checking
import os
import time
import asyncio
import shutil
# Windows
USER_HOME_PATH=os.getenv('HOMEPATH')  # Can also be editable to downloads path or something else
if(USER_HOME_PATH == None):
  USER_HOME_PATH=os.getenv('HOME')
  
paths_to_ignore=[os.path.join(USER_HOME_PATH,'AppData')]
folders_to_ignore=['node_modules']
formats_to_move=['.mp3','.pdf']
format_='.mp3'
WALKING_FOLDERS_PATHS=[]
# print(os.environ)

files_scanned=0
def endsWithAny(str_,list_):
  global files_scanned
  files_scanned+=1
  for each in list_:
    if str_.endswith(each):
      return each
  return ''

# returns [[],[],[]] list of arrays last might not be of equal size to others
def splitArrayIntoChunks(arr, chunk_size):
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    return chunks

    
# for getting moving of certain file types and for getting all main subfolders in a certain path 
async def move_file(src, dst):
    # will be displayed in logs not printed out
    print(f"Moving {src} to {dst}...")
    # try:
    #   shutil.move(src, dst)
    # except Exception as e:
      # print(e)
    # will be displayed in logs not printed out
    # print(f"Moved {src} to {dst}")
    ...

folders_scanned=0
async def getFoldersPaths__NdMoveChoosenFiles(folder_paths,obj_for_where_to_move):  
  #results= ['path/folder 1','path/folder 2'] || []
  gotten_folder_paths=[]
  global folders_scanned
  for each_folder_path in folder_paths:
    try:
      all_paths = os.listdir(each_folder_path)
      for folder_or_file_name in all_paths:
        found_path=os.path.join(each_folder_path,folder_or_file_name)
        if found_path not in paths_to_ignore and folder_or_file_name not in folders_to_ignore and os.path.isdir(found_path):
          gotten_folder_paths.append(found_path)
          folders_scanned+=1
        else:
          found_format=endsWithAny(folder_or_file_name,obj_for_where_to_move.keys())
          if found_format:
            # print(obj_for_where_to_move,found_format)
            await move_file(found_path,obj_for_where_to_move[found_format])#data_frm_appData[format_])
            ...
    except Exception as e:
      # print(e) # Display Error in Log Screen "As is" i mean in the same format it's printed out in console (Will Probably only get error if Access Denied or Folder Moved)
      ...
  return gotten_folder_paths


#{file_format:str,folder_path:str}
async_funcs_count=0
async def moveFormatsToTheirFolders(obj_for_where_to_move):

  global async_funcs_count
  start_time=time.time()
  WALKING_FOLDERS_PATHS = await getFoldersPaths__NdMoveChoosenFiles([USER_HOME_PATH],obj_for_where_to_move)
  fail_safe=0
  while len(WALKING_FOLDERS_PATHS) and fail_safe < 20:
    # print('walking ',WALKING_FOLDERS_PATHS[0])
    fail_safe+=1
    list_of_async_funcs=[]
    chunks = splitArrayIntoChunks(WALKING_FOLDERS_PATHS,int(len(WALKING_FOLDERS_PATHS)**(1/2)))
    #getting list of asynchronous functions
    list_of_async_funcs = [getFoldersPaths__NdMoveChoosenFiles(chunk,obj_for_where_to_move) for chunk in chunks]
    async_funcs_count += len(list_of_async_funcs)
    # results will be a list of list of folders
    lists_folder_paths = await asyncio.gather(*list_of_async_funcs)

    WALKING_FOLDERS_PATHS=sum(lists_folder_paths,[])
    # WALKING_FOLDERS_PATHS=[*list_of_lists_folder_paths]
  end_time=time.time() - start_time

  print(f"""
 _________________________________
| <Dev>                           |
|                                 |
| Elapsed time: {round(end_time,5)} seconds   |
|  * Entered While loop {fail_safe} times.  |
|  * Created {async_funcs_count} Async Functions.  |
|  * Scanned {folders_scanned} Folders.         |
|  * Scanned {files_scanned} Files.          |
|_________________________________|
""")
  
asyncio.run(moveFormatsToTheirFolders({'.mp4':r'C:\Users\hp\Desktop\My Music'}))
def getNewFileName(file_name,names_in_folder):
  file_name_before_dot = file_name.split('.')[0]#file_name_without_format
  print(file_name_before_dot)

# getNewFileName('filemp1',[])
