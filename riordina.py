import os
import shutil
import time

with_file_i_need_to_order: set = {"txt", "pdf", "jpg", "py", "c", "c++", "java", "png"}



def order(path: str):
    
    while True:
        all_file:list = os.listdir(path)

        if "riordina.py" in all_file: 
            all_file.remove("riordina.py")

        time.sleep(1)
        if all_file != []:
            for i in all_file:
                print(i)
        else:
            print("EMPTY")

        first_question:str = input("\nwith file do you want to order?, persent enter to order the corrent folder: ")
        last_folder_open = "/"+first_question
        if first_question == "":
            second_question = input(f"are you score you wnat to oreder {path} [y/n]: ")
            if second_question == "Y" \
                or second_question == "y":
                break
            else:
                print()
                continue

        elif first_question in all_file:
            path += "/"+first_question
        
        
        elif first_question == "back":
            new_path = path.split("/")
            new_path.pop()
            path = "/".join(new_path)

        else:
            print(f"{first_question} is not a folder")
        print()
        
    all_file:list = os.listdir(path)
    if "riordina.py" in all_file: 
            all_file.remove("riordina.py")
    try:
        os.mkdir(path+"/Non_classificabile")
    except  FileExistsError:
        pass
    
    for i in all_file:
        if i[0] in "._":
            continue
        point_index:int = i.find(".")
        if(point_index != -1):
            name_new_dir = i[point_index+1:]

            if(os.path.isdir(name_new_dir)):
                shutil.move(path+"/"+i, path+"/"+name_new_dir)

            else:
                os.mkdir(path+"/"+name_new_dir)
                shutil.move(path+"/"+i, path+"/"+name_new_dir)

        elif(os.path.isdir(i)):
            pass

        else:
            shutil.move(path+"/"+i, path+"/Non_classificabile")



if __name__ == "__main__":
    start:str = os.environ["HOMEPATH"]
    if "OneDrive" in os.listdir(start):
        start += "/OneDrive/Desktop"
    else:
        start = os.path.expanduser("~/Desktop")
    # start_test = "C:/Users/marco/OneDrive/Desktop/Progetti_python/Python riodonare/Desktop_di_prova/Folder1"
    order(start)
    

 