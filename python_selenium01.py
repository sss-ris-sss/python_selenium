# python_selenium01.py

print ("Hello, Python")

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome("./driver/chromedriver.exe")

location = input("Enterで検索開始")
searchword = ["black tea", "assam tea", "darjeeling tea"]

for i, tea in enumerate(searchword):
    if i > 0:
        # 新しいタブ
        chrome.execute_script("window.open('','_blank');")
        chrome.switch_to.window(chrome.window_handles[i])

    # Googleを開く
    chrome.get("https://www.google.co.jp")

    # 検索語を入力
    search_box = chrome.find_element_by_name("q")
    search_words = location, tea
    search_box.send_keys(" ".join(search_words))

    # 検索実行
    search_box.send_keys(Keys.RETURN)
    print(chrome.title)

# 先頭のタブに戻る
chrome.switch_to.window(chrome.window_handles[0])