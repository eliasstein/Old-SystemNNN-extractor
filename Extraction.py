import glob,os
from time import sleep
import shutil

def extraction():
    for x in glob.glob("spt_files/*.spt"):
        print(x)
        os.system("tool\gsspt.exe "+x+" "+x[:-3]+"txt")
    

    for x in glob.glob("spt_files/*.txt"):
        fread=open(x,"r",encoding="utf-8")
        buffer=[]
        buffer=fread.readlines()

        for y in range(0,len(buffer)):
            if buffer[y].__contains__("###"):
                for char in range(0,len(buffer[y])):
                    if buffer[y][char]=="#" and buffer[y][char+1]=="#" and buffer[y][char+2]=="#" and buffer[y][char-1]!="\n":
                        buffer[y]=buffer[y][:char]+"\n"+buffer[y][char:]
        fwrite=open("scripts_repaired"+x[9:],"w",encoding="utf-8")
        for y in range(0,len(buffer)):
            fwrite.write(buffer[y])
    for x in glob.glob("spt_files/*.txt"):
        fwrite.close()
        fread.close()
        os.remove(x)
    menu()

def insert():
    file_name=[]
    for x in glob.glob("scripts_repaired/*.txt"):
        shutil.copy(x, "./patch")
    for x in glob.glob("spt_files/*.spt"):
        shutil.copy(x, "./patch")
    
    for x in glob.glob("patch/*.*"):
        
        if x[len(x)-4:]==".txt":
            file_name.append(x)
    
    for x in range(0,len(file_name)):
        os.system("tool\gsspt.exe "+file_name[x]+" "+file_name[x][:-3]+"spt")
        os.remove(file_name[x])


def menu():
    print("1 Extract text in Text_parched")
    print("2 Insert text")
    if not os.path.exists('patch'):
        os.makedirs('patch')
    if not os.path.exists('scripts_repaired'):
        os.makedirs('scripts_repaired')
    if not os.path.exists('spt_files'):
        os.makedirs('spt_files')

    option=int(input())
    if option==1:
        extraction()
    if option==2:
        insert()


menu()
    