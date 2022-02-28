import time
from selenium import webdriver
url="https://card-search.naver.com/list?sortMethod=ri&where=nexearch&query=%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C%EB%B0%9C%EA%B8%89%EC%A1%B0%EA%B1%B4&bizType=CPC"
drive=webdriver.Edge(r'C:/Users/user/Desktop/edgedriver_win64ver/msedgedriver.exe')
drive.implicitly_wait(0.3)
drive.get(url)
cardcnt=int(drive.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/button[1]/span/i').text)

while True:
    if drive.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/button/i').text[0:3] == '360':
        drive.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/button').click()
        time.sleep(0.3)
        break
    drive.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/button').click()
    time.sleep(0.3)
cardurl=[]
for i in range(1,cardcnt+1):
    imagenum=drive.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/ul/li['+str(i)+']/div[1]/a[1]/figure/img')
    cardnum=str(imagenum.get_attribute('src')).split('/')[6]
    cardurl.append('https://card-search.naver.com/item?cardAdId='+cardnum)
fs=open('cardurl.txt','w')
for i in cardurl:
    fs.write(i)
    fs.write('\n')

