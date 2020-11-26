#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import ArticutAPID

def json File Writer(jsonDICT, jsonFileName):
    with open (jsonFileName, mode = "w") as f:
        json.dump(jsonDICT, f, ensure_ascii = False)

def charCounter(inputSTR):
    charDICT={}
    for i in inputSTR:
        if i in charDICT:
            pass
        else:
            charDICT[i] = inputSTR.count(i)
     charCountList=[]
     for i in charDICT.items():
         charCountList.append(i)
    charCountList.sort(key=lambda c:c[1], reverse=True)
    return charCountList

def wordPlusPosCounter(inputSTR):
    inputSTR=inputSTR.replace('><','>MY_SPLITTER<')
    inputLIST=inputSTR.split('>MY_SPLITTER<')
    wordDICT={}
    for w in wordDICT:
        if w in wordDICT:
          pass
        else:
            wordDICT[w]=inputLIST.count(w)
    wordCountLIST=[]
    for i in wordDICT.items():
        wordCountLIST.append(i)
    wordCountLIST.sort(key=lambda c:c[1], reverse=True)
    return wordCountLIST
    

if __name__=="__main__":
    with open ("dbp.txt", encoding="utf-8")as f:
        dbpSTR = f.read()
    with open ("pbd.txt", encoding="utf-8")as f:
        pbdSTR = f.read()
    
    charCount_dbp = charCounter(dbpSTR)
    charCount_pbd = charCounter(pbdSTR)

    articut=ArticutAPI.Articut()
    segTextSTR=''
    for i in range(1,len(dbpSTR),2000):
        resultDICT=articut.parse(dbpSTR[i:i+2000])
        segdbpSTR=segTextSTR+resultDICT['result_segmentation']
    wordCount_dbp = wordCounter(segdbpSTR)

    for i in range(1,len(pbdSTR),2000):
        resultDICT=articut.parse(pbdSTR[i:i+2000])
        segpbdSTR=segTextSTR+resultDICT['result_segmentation']
    wordCount_pbd = wordCounter(segpbdSTR)
