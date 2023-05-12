import os
import shutil

with_file_i_need_to_order: set = {"txt", "pdf", "jpg", "py", "c", "c++", "java", "png"}



def order(path: str):

    all_file:list = os.listdir(os.getcwd())
    # all_file.remove("riordina.py")
    # all_file.remove("eseguibile.bat")
    
    try:
        os.mkdir(os.getcwd()+"/Non_classificabile")
    except  FileExistsError:
        pass
    
    for i in all_file:

        point_index:int = i.find(".")
        if(point_index != -1):
            name_new_dir = i[point_index+1:]

            if(os.path.isdir(name_new_dir)):
                shutil.move(os.getcwd()+"/"+i, os.getcwd()+"/"+name_new_dir)

            else:
                os.mkdir(os.getcwd()+"/"+name_new_dir)
                shutil.move(os.getcwd()+"/"+i, os.getcwd()+"/"+name_new_dir)

        elif(os.path.isdir(i)):
            pass

        else:
            shutil.move(os.getcwd()+"/"+i, os.getcwd()+"/Non_classificabile")


if __name__ == "__main__":
    pre_path = os.getcwd()
    i = len(pre_path)
    while pre_path[i] != "\\" and pre_path != "/":
        i-=1

    path = pre_path[:i] 
    lista = os.listdir(path)
    for i in lista:
        if(os.path.isdir(i)):
            print(os.path.basename(i))
    
    order(input("quale cartella ordinare?: "))
    

 