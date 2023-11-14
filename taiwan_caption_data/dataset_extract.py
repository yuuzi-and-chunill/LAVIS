import json
import os
import random

def deleteListFromData(data:list, deleteList:list):
    return list(set(data).difference(set(deleteList)))
    
def getRandomDataOfLen(data:list, len:int):
    dataOfLen = random.sample(data, len)
    return dataOfLen

def copyDataToDict(data:dict, copyDataKeys:list):
    copyData = {}
    for i in copyDataKeys:
        copyData[i] = data[i]
    return copyData

def writeJsonFile(mode:str, infoDict:dict):

    with open(mode+".json", "w+", encoding="utf-8") as file:
        file.write(json.dumps(infoDict, indent=4, ensure_ascii=False))
    
    
def main():
    with open("image_info.json", "r", encoding="utf-8") as file:
        allImgsInfo = json.load(file)
    lenAllImgs = len(allImgsInfo)

    
    keysOfAllImgs = list(allImgsInfo.keys())
    valDataKeys = getRandomDataOfLen(keysOfAllImgs, int(lenAllImgs/10))
    keysOfAllImgs = deleteListFromData(keysOfAllImgs, valDataKeys)
    testDataKeys = getRandomDataOfLen(keysOfAllImgs, int(lenAllImgs/10))
    keysOfAllImgs = deleteListFromData(keysOfAllImgs, testDataKeys)
    trainDataKeys = keysOfAllImgs

    print(len(testDataKeys))
    print(len(valDataKeys))
    print(len(trainDataKeys))

    writeJsonFile("train", copyDataToDict(allImgsInfo, trainDataKeys))
    writeJsonFile("val", copyDataToDict(allImgsInfo, valDataKeys))
    writeJsonFile("test", copyDataToDict(allImgsInfo, testDataKeys))

main()