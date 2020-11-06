#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import jieba,os,json

#讀取 json 檔案，並以 jieba 斷詞處理其內容中 "BODY" 欄位的程式
#[註] 上週才寫過「讀取 json 的檔案，其實可以把它複製過來使用哦！
#這麼一來， "讀取 json" 的功能就不用重寫了。只要把檔案丟給上週的
#程式，取得回傳的值，再接著寫就好了。
def text2cws(jsonFilePath):
    with open(jsonFilePath, 'r', encoding = 'utf8') as f:
        jsonContent = json.load(f)
    BodyStr = jsonContent["BODY"]
    for i in ("，","。","「","」","、","(",")","（","）","/","／","；",'【','】'):
        BodyStr = BodyStr.replace(i,'<MyCuttingMark>')
    for i in ('...','…'):
        BodyStr = BodyStr.replace(i,'')
    for i in range(len(BodyStr)):
        if BodyStr[i]==',' and BodyStr[i-1] not in ['1','2','3','4','5','6','7','8','9','0']:
            BodyStr = BodyStr[0:i] + '<MyCuttingMark>' + BodyStr[i+1:]
    BodyList = BodyStr.split('<MyCuttingMark>')
    while '' in BodyList:
        BodyList.remove('')
    seg_list = []
    for i in BodyList:
        seg_list.extend(list(jieba.cut(i)))
    return seg_list


#設計一個名為 termFreq() 的程式，承接 text2cws() 的回傳值，並
#建立一個 resultDICT{}。內容是 resultDICT = {"某個字/詞", 5,
#"另一個字/詞", 8} 的格式。其中的數字是那個字/詞在 10 篇文章中總
#共出現的次數。

#e.g., 文章01 = "斷詞不要結巴"。文章02 = "斷詞不要結結巴巴"，則
#resultDICT = {"斷詞": 2, "不要": 2, "結巴": 1, "結結巴巴": 1}

def termFreq(seg_list):
    resultDICT = {}
    for i in seg_list:
        for i in resultDICT:
            resultDICT[i]=resultDICT[i]+1
        else:
            resultDICT[i]=1
    return resultDICT


#設計一程式進入點，讀取 example/health/ 中所有檔案，然後將檔案路徑
#傳給 text2cws()，取得內容後，再傳給 termFreq()。
#完成後，對 example/finance/ 中的所有檔案做一樣的操作。

if __name__=="__main__":
    jsonFilePath = ('./example/health', './example/finance')
    for i in jsonFilePath:
        for file in os.listdir(i):
            path = i + '/' + file
            print(termFreq(text2cws(path)))
