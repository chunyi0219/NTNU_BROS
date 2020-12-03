#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ArticutAPI import ArticutAPI

def jsonFileWriter(jsonDICT, jsonFileName):
    """convert jsonDICT into a jsonFile and save it as jsonFileName."""
    with open (jsonFileName, mode = "w") as f:
        #json.dump(要寫入的資料, 目標檔案, 是否要讓輸入值為ascii)
        json.dump(jsonDICT, f, ensure_ascii = False)

def TextReader(FilePath):
    with open(FilePath,"r",encoding="utf-8") as f:
        resultSTR = f.read()
    return resultSTR

def findEvent(inputSTR, nlptool):
    resultDICT = articut.parse(inputSTR, level="lv3")
    return resultDICT

def findVerb(inputSTR):
    resultLIST=articut.parse(inputSTR,level='lv2')
    verbLIST=articut.getVerbStemLIST(resultLIST)
    return verbLIST

if __name__== "__main__":

    textSTR = TextReader("../example/text.txt")
    text01STR = TextReader("../example/text01.txt")
    
    articut = ArticutAPI.Articut()
    
    textListEvent=findEvent(textSTR,articut)
    textListVerb=findVerb(textSTR)
    eventList=textListEvent['event']

    text01ListEvent=findEvent(textSTR,articut)
    text01ListVerb=findVerb(textSTR)
    event01List=text01ListEvent['event']

    jsonDICT = {
        "倉鼠":eventList,
        "皇帝企鵝":event01List
        }
    jsonFileName="week12_squad.json"
    jsonFileWriter(jsonDICT, jsonFileName)
    print(eventLIST,textListVerb)