#deactivate start button when function starts
# prompt to run as admin when special parts added
import os
import asyncio
USER_HOME_PATH=os.getenv('HOMEPATH')
paths_to_ignore=[os.path.join(USER_HOME_PATH,'AppData')]
folders_to_ignore=['node_modules']
# print(os.environ)
# print(os.getenv('Appdata'))
format_='.mkv'
WALKING_FOLDERS_PATHS=[]
def getRootFolders():
  for each_path in os.listdir(USER_HOME_PATH):
    current_path = os.path.join(USER_HOME_PATH,each_path)
    if current_path not in paths_to_ignore and each_path not in folders_to_ignore:
      if os.path.isdir(current_path):
        WALKING_FOLDERS_PATHS.append(current_path)
      else:
        # Moving file to requried folder needed
        ...


getRootFolders()
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


async def getFoldersPaths(folder_paths):  
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


def assignFoldersToArray(list_of_arrays): 
  #input type[ [] , []]
  # WALKING_FOLDERS_PATHS=[]
  global WALKING_FOLDERS_PATHS
  WALKING_FOLDERS_PATHS=sum(list_of_arrays,[])
  
    
async def walking():
  global WALKING_FOLDERS_PATHS
  i=0
  while len(WALKING_FOLDERS_PATHS) and i < 20:
    # print('walking ',WALKING_FOLDERS_PATHS[0])
    i+=1
    list_of_async_funcs=[]
    chunks = splitArrayIntoChunks(WALKING_FOLDERS_PATHS,5)
    #getting list of asynchronous functions
    for chunk in chunks:
      list_of_async_funcs.append(getFoldersPaths(chunk))

    # results will be list of folders
    list_of_lists_folder_paths = await asyncio.gather(*list_of_async_funcs)
    assignFoldersToArray(list_of_lists_folder_paths)
    # WALKING_FOLDERS_PATHS=[*list_of_lists_folder_paths]
  print('Done walking',i,WALKING_FOLDERS_PATHS)
asyncio.run(walking())

# print(sum([[1,2],[3,4],[5]],[]))