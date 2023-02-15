import os
import sys
from pathlib import Path
import pandas
import shutil
import csv
import time

def fol_prep(path):
    print("#"*30, "SetUp", "#"*30)
    # time.sleep(0.1)
    if os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=False, onerror=None)
        print("Tree deleted", end="\t")
    os.mkdir(path)
    print(os.path.abspath(path))
    print("#"*30, "SetUpDone", "#"*30)
    
def debug():
    debug= "debug"  
    fol_prep(debug)
    
    de_f_path= Path(debug)
    base_path = Path()
    cmd_cwd= os.getcwd()
    de=list()

    if True:
        for fd_path, sf_fol, sf_f in os.walk(os.getcwd()):
            de.append(str(fd_path))
            for i in sf_f:#フォルダ(サブなし)のファイル一覧
                de.append("\t , "+i)
            de.append("\n")
    with open(debug+"/debug.csv", "w") as f:
        for i in de:
            f.write(i)

def Fele(nf="FixedData", rd="RawData", globf="**/*-*.csv"):
    fol_prep(nf)
    for root, dirs, files in os.walk(Path("RawData")):
        absp=os.path.abspath(root) #ファイルパス(絶対)

        sp= absp.split(os.sep) #パスリストにバラす
        for i in range(len(sp)): #ファイル名パスを Raw から Fix に修正
            if sp[0]==rd:
                sp[0]=nf
                break
            sp.pop(0)
        print(sp)
        
        p=0
        for i in Path(absp).glob(globf): #RawData から File 読み込み
            with open(i, "r") as f:
                if not os.path.exists(os.path.join(*sp)):
                    os.makedirs(os.path.join(*sp))
                    
                with open(os.path.join(os.path.join(*sp)+"_Fixed.csv"), "a") as o:
                    re=csv.reader(f)
                    l=0
                    for j in re:
                        if j[0]== "0": continue
                        if j[3]== "1": j.pop(3) 
                        if l==0:k=j
                        o.write(','.join(j)+"\n")
                        o.flush()
                        k=j
                        l+=1
                        
                p+=1
        print("EOF")
        
def Fele2(nf="FixedData", rd="RawData", globf="**/*-*.csv"):
    fol_prep(nf)
    for root, dirs, files in os.walk(Path("RawData")):
        absp=os.path.abspath(root) #ファイルパス(絶対)

        sp= absp.split(os.sep) #パスリストにバラす
        for i in range(len(sp)): #ファイル名パスを Raw から Fix に修正
            if sp[0]==rd:
                sp[0]=nf
                break
            sp.pop(0)
        print(sp)
        
        p=0
        en=0 #enemy num count
        for i in Path(absp).glob(globf):
            with open(i, "r") as f:
                if not os.path.exists(os.path.join(*sp)):
                    os.makedirs(os.path.join(*sp))
                    
                with open(os.path.join(os.path.join(*sp)+"_Fixed.csv"), "a") as o:
                    re=csv.reader(f)
                    b=0
                    for j in re:
                        if j[0]== "0": continue
                        if j[3]== "1": j.pop(3) 
                        if not b == int(j[0]):
                            b=int(j[0])
                            en+=1
                            # print(en)
                        j[0]=str(en)
                       
                        o.write(','.join(j)+"\n")
                        o.flush()
        print("EOF")
Fele2()
               