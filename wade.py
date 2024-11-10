#deactivate start button when function starts
# prompt to run as admin when special parts added
import os
import asyncio
USER_HOME_PATH=os.getenv('HOMEPATH')  # Can also be editable to downloads path or something else
paths_to_ignore=[os.path.join(USER_HOME_PATH,'AppData')]
folders_to_ignore=['node_modules']
formats_to_move=['.mp3','.pdf']
format_='.mp3'
WALKING_FOLDERS_PATHS=[]


async def getRootFolders__NdMoveChoosenFiles():
  found_folders=[]
  for each_path in os.listdir(USER_HOME_PATH):
    current_path = os.path.join(USER_HOME_PATH,each_path)
    if current_path not in paths_to_ignore and each_path not in folders_to_ignore:
      if os.path.isdir(current_path):
        found_folders.append(current_path)
      elif each_path.lower().endswith(format_):
        await move_file(current_path,'last frontier')
        # Moving file to requried folder needed
        ...
  return found_folders

# returns [[],[],[]] list of arrays last might not be of equal size to others
def splitArrayIntoChunks(arr, chunk_size):
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]
    return chunks

    
# for getting moving of certain file types and for getting all main subfolders in a certain path 
async def move_file(src, dst):
    # will be displayed in logs not printed out
    print(f"Moving {src} to {dst}...")
#     shutil.move(src, dst)
    # will be displayed in logs not printed out
    print(f"Moved {src} to {dst}")


async def getFoldersPaths__NdMoveChoosenFiles(folder_paths):  
  #results= ['path/folder 1','path/folder 2'] || []
  gotten_folder_paths=[]
  for each_folder_path in folder_paths:
    try:
      all_paths = os.listdir(each_folder_path)
      for each_path in all_paths:
        folder_name=each_path
        each_path=os.path.join(each_folder_path,each_path)
        if os.path.isdir(each_path) and folder_name not in folders_to_ignore:
          gotten_folder_paths.append(each_path)
        elif each_path.lower().endswith(format_):
          await move_file(os.path.join(each_folder_path,each_path),'space')#data_frm_appData[format_])
          ...
    except Exception as e:
      # print(e) # Display Error in Log Screen "As is" i mean in the same format it's printed out in console (Will Probably only get error if Access Denied or Folder Moved)
      ...
  return gotten_folder_paths


#{file_format:str,folder_path:str}
async def moveFormatsToTheirFolders(obj):
  # global WALKING_FOLDERS_PATHS
  WALKING_FOLDERS_PATHS = await getRootFolders__NdMoveChoosenFiles()
  fail_safe=0
  while len(WALKING_FOLDERS_PATHS) and fail_safe < 20:
    # print('walking ',WALKING_FOLDERS_PATHS[0])
    fail_safe+=1
    list_of_async_funcs=[]
    chunks = splitArrayIntoChunks(WALKING_FOLDERS_PATHS,int(len(WALKING_FOLDERS_PATHS)**(1/2)))
    # print(int(len(WALKING_FOLDERS_PATHS)**(1/2)))
    #getting list of asynchronous functions
    for chunk in chunks:
      list_of_async_funcs.append(getFoldersPaths__NdMoveChoosenFiles(chunk))

    # results will be list of folders
    lists_folder_paths = await asyncio.gather(*list_of_async_funcs)

    WALKING_FOLDERS_PATHS=sum(lists_folder_paths,[])
    # WALKING_FOLDERS_PATHS=[*list_of_lists_folder_paths]
  print('Done walking',fail_safe,WALKING_FOLDERS_PATHS)

asyncio.run(moveFormatsToTheirFolders({'.mp3':'blah/blah/music'}))
