#coding:utf-8
import os

typename = "depth"
def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname=os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    formername = os.path.splitext(name)[0]
                    file.write(formername +" " + typename + "/" + name + "\n")
                    break

def Test():
    dir="/home/zhouhao/GraduationProject/data/test1dachen/" + typename     #文件路径
    outfile=typename + "1.txt"                     #写入的txt文件名
    wildcard = ".jpg .txt .exe .dll .lib .png"      #要读取的文件类型；

    file = open(outfile,"w")
    if not file:
        print ("cannot open the file %s for writing" % outfile)

    ListFilesToTxt(dir,file,wildcard, 1)

    file.close()

if __name__ == "__main__":
    Test()
