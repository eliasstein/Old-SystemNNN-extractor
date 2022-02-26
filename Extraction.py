import glob,os
from time import sleep
import shutil

def extraction():
    for x in glob.glob("spt_patch/*.spt"):
        os.system("tool\gsspt.exe "+x+" "+x[:-3]+"txt")


    for x in glob.glob("spt_patch/*.txt"):
        fread=open(x,"r",encoding="utf-8")
        buffer=[]
        buffer=fread.readlines()

        for y in range(0,len(buffer)):
            if buffer[y].__contains__("###"):
                for char in range(0,len(buffer[y])):
                    if buffer[y][char]=="#" and buffer[y][char+1]=="#" and buffer[y][char+2]=="#" and buffer[y][char-1]!="\n":
                        buffer[y]=buffer[y][:char]+"\n"+buffer[y][char:]

        fwrite=open("Text_patched"+x[9:],"w",encoding="utf-8")
        for y in range(0,len(buffer)):
            fwrite.write(buffer[y])
    for x in glob.glob("spt_patch/*.txt"):
        fwrite.close()
        fread.close()
        os.remove(x)
    menu()

def insert():
    file_name=[]
    for x in glob.glob("Text_patched/*.txt"):
        shutil.copy(x, "./insertion")
    for x in glob.glob("spt_patch/*.spt"):
        shutil.copy(x, "./insertion")
    
    for x in glob.glob("insertion/*.*"):
        
        if x[len(x)-4:]==".txt":
            file_name.append(x)
    
    for x in range(0,len(file_name)):
        os.system("tool\gsspt.exe "+file_name[x]+" "+file_name[x][:-3]+"spt")
        os.remove(file_name[x])


def menu():
    print("1 Extract text in Text_parched")
    print("2 Insert text")
    option=int(input())
    if option==1:
        extraction()
    if option==2:
        insert()


menu()
    