from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import wget
import json
import time

driver = webdriver.Edge()
# driver.get('https://media.taiwan.net.tw/zh-tw/portal/media?DocType=100&DocClass=&Selections=&Keyword=&Size=&County=&YearStart=&YearEnd=&CreationYearStart=&CreationYearEnd=&DocId=') 
driver.get('https://media.taiwan.net.tw/zh-tw/portal/media?DocType=100&DocClass=&Selections=&Keyword=&Size=&County=&YearStart=&YearEnd=&CreationYearStart=&CreationYearEnd=&DocId=&page=75') 

def getImageInfo(element):
    img_info = {}
    img_info["src"] = element.get_attribute('src')
    img_info["alt"] = element.get_attribute('alt')
    element.click()
    img_info["id"] = driver.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "i").get_attribute("textContent")[4:]
    img_info["introduction"] = driver.find_element(By.TAG_NAME, "p").get_attribute("textContent")

    print(img_info)
    return img_info

def downloadImg(imgDict:dict):
    for i in imgDict.values():
        img_save_as = os.path.join("image", f"ID{i['id']}.jpg")
        wget.download(i["src"], img_save_as)

# 建立放置圖片的資料夾
# path = os.path.join("image2")
# os.mkdir(path)

def main():
    AllImgInfo = {}
    page = 1
    try:
        for i in range(page):
            for i in range(12):
                img = driver.find_elements(By.CLASS_NAME, "card-img-top")[i]
                Dict = getImageInfo(img)
                driver.back()
                AllImgInfo[f"ID{Dict['id']}"] = Dict
            next_page = driver.find_element(By.CLASS_NAME, "fa-angle-right")
            next_page.click()
    except:
        pass
            
    downloadImg(AllImgInfo)
    
    with open("ann.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(AllImgInfo, indent=4, ensure_ascii=False))

main()