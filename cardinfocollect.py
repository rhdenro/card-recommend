import time
from selenium import webdriver
import pran
import exchange
from selenium.webdriver.common.action_chains import ActionChains

drive = webdriver.Edge(r'C:/Users/user/Desktop/edgedriver_win64/msedgedriver.exe')
cardinfo = {}
fs = open('cardurl.txt', 'r')
cardurl = fs.read().split('\n')
fs.close()
keylist = ['telecom', 'convenience', 'movie','transit']
for i in cardurl:
    cardinfotmp = {}
    benefitcnt = 0
    try:
        drive.get(i)
        cardname = drive.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/b').text
        if '마일리지' in cardname or cardname == 'KB국민 아시아나 올림카드':
            continue
    except:
        continue
    if drive.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/dl/dt[1]').text == '공지':
        cardcost = drive.find_element_by_xpath('// *[ @ id = "app"]/div/div[1]/div/div[3]/dl/dd[2]/span').text.split(
            ' ')
        if len(cardcost) == 1:
            cardinfotmp['cardcost'] = cardcost[0]
        else:
            cardinfotmp['cardcost'] = cardcost[1].split(',')[0]

        cardreq = drive.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/dl/dd[3]').text.split(' ')
        if len(cardreq) == 1:
            cardinfotmp["cardreq"] = cardreq[0]
        else:
            cardinfotmp["cardreq"] = cardreq[3]
    else:
        cardcost = drive.find_element_by_xpath('// *[ @ id = "app"]/div/div[1]/div/div[3]/dl/dd[1]/span').text.split(
            ' ')
        if len(cardcost) == 1:
            cardinfotmp['cardcost'] = cardcost[0]
        else:
            cardinfotmp['cardcost'] = cardcost[1].split(',')[0]
        cardreq = drive.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/dl/dd[2]').text.split(' ')
        if len(cardreq) == 1:
            cardinfotmp["cardreq"] = cardreq[0]
        else:
            for i in cardreq:
                if '만원' in i:
                    cardinfotmp["cardreq"] = i

    action = ActionChains(drive)
    action.reset_actions()
    count=1
    while True:
        try:
            count+=1
            action.move_to_element(drive.find_element_by_css_selector
                                   ('#app > div.cardItem > div.Benefits > div > details:nth-child('+
                                    str(count+1) + ') > summary > h5'))\
                .move_to_element(drive.find_element_by_css_selector
                                             ('#app > div.cardItem >'''
                                              ' div.Benefits > div > details:nth-child('+
                                              str(count) + ') > summary > h5')).click()
        except Exception as ex:
            action.move_to_element(drive.find_element_by_css_selector
                                   ('#app > div.cardItem > div.Others')) \
                .move_to_element(drive.find_element_by_css_selector
                                 ('#app > div.cardItem >'''
                                  ' div.Benefits > div > details:nth-child(' +
                                  str(count) + ') > summary > h5')).click()
            action.perform()
            break
    details_count = 1
    while True:
        try:
            benefit = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details[' +
                                                  str(details_count) + '] /summary/h5/b').text
            print(benefit)
            if benefit == '통신':
                tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                       + str(details_count) + ']/div/dl/dt').text
                if not '%' in tmp_list and not '원' in tmp_list:
                    tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                           + str(details_count) + ']/div/dl/dd[1]').text
                tmp_list = tmp_list.split(' ')
                tmp_cost = None
                for i in tmp_list:
                    if any(k.isdigit() for k in i):
                        if '%' in i:
                            tmp_cost = i[0:i.find('%') + 1]
                            cardinfotmp['telecom'] = tmp_cost
                        else:
                            if '연' in tmp_list:
                                tmp_cost = exchange.exchange(i, date=12)
                                cardinfotmp['telecom'] = tmp_cost
                            else:
                                tmp_cost = exchange.exchange(i)
                                cardinfotmp['telecom'] = tmp_cost

                        break
                details_count += 1
            elif benefit == '대중교통':
                tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                       + str(details_count) + ']/div/dl/dt').text
                if not '%' in tmp_list and not '원' in tmp_list:
                    tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                           + str(details_count) + ']/div/dl/dd[1]').text
                tmp_list = tmp_list.split(' ')
                tmp_cost = None
                for i in tmp_list:
                    if any(k.isdigit() for k in i):
                        if '%' in i:
                            tmp_cost = i[0:i.find('%') + 1]
                            cardinfotmp['transit'] = tmp_cost
                        else:
                            if '연' in tmp_list:
                                tmp_cost = exchange.exchange(i, date=12)
                                cardinfotmp['transit'] = tmp_cost
                            else:
                                tmp_cost = exchange.exchange(i)
                                cardinfotmp['transit'] = tmp_cost
                        details_count += 1
                        break
            elif benefit == '영화':
                tmp_cost = None
                tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                       + str(details_count) + ']/div/dl/dt').text
                if not '%' in tmp_list and not '원' in tmp_list:
                    tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                           + str(details_count) + ']/div/dl/dd[1]').text
                if not '%' in tmp_list and not '원' in tmp_list:
                    tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                           + str(details_count) + ']/ div / dl / dd[1]').text
                if not '%' in tmp_list and not '원' in tmp_list:
                    tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                           + str(details_count) + ']/ div / dl / dd[2]').text
                tmp_list = tmp_list.split(' ')
                flag = False
                for i in tmp_list:
                    if '적립' in i:
                        flag = True

                if flag == True:
                    details_count += 1
                else:
                    for i in tmp_list:
                        if '%' in i:
                            tmp_cost = i[0:i.find('%') + 1]
                        elif '원' in i:
                            if '연' in tmp_list:
                                tmp_cost = exchange.exchange(i, date=12)
                            else:
                                tmp_cost = exchange.exchange(i)
                    tmp_cost = exchange.movie_dict_fenc(tmp_list, tmp_cost)
                    cardinfotmp['movie'] = tmp_cost
                    details_count+=1
            elif benefit == '편의점':
                tmp_cost = None
                tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                       + str(details_count) + ']/div/dl/dt').text
                if not '%' in tmp_list and not '원' in tmp_list:
                    tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                           + str(details_count) + ']/div/dl/dd[1]').text
                if not '%' in tmp_list and not '원' in tmp_list:
                    tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                           + str(details_count) + ']/ div / dl / dd[1]').text
                if not '%' in tmp_list and not '원' in tmp_list:
                    tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                           + str(details_count) + ']/ div / dl / dd[2]').text
                tmp_list = tmp_list.split(' ')
                flag = False
                for i in tmp_list:
                    if '적립' in i:
                        flag = True

                if flag == True:
                    details_count += 1
                else:
                    for i in tmp_list:
                        if '%' in i:
                            tmp_cost = i[0:i.find('%') + 1]
                        elif '원' in i:
                            if '연' in tmp_list:
                                tmp_cost = exchange.exchange(i, date=12)
                            else:
                                tmp_cost = exchange.exchange(i)
                    tmp_cost = exchange.convenience_dict_fenc(tmp_list, tmp_cost)
                    cardinfotmp['convenience'] = tmp_cost
                    details_count+=1
            elif benefit == '주유':
                tmp_cost = None
                tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                       + str(details_count) + ']/div/dl/dt').text
                if not '%' in tmp_list and not '원' in tmp_list:
                    tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                           + str(details_count) + ']/div/dl/dd[1]').text
                if not '%' in tmp_list and not '원' in tmp_list:
                    tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                           + str(details_count) + ']/ div / dl / dd[1]').text
                if not '%' in tmp_list and not '원' in tmp_list:
                    tmp_list = drive.find_element_by_xpath('// *[ @ id = "app"] / div[1] / div[4] / div / details['
                                                           + str(details_count) + ']/ div / dl / dd[2]').text
                print(tmp_list)
                details_count+=1
            else:
                details_count += 1
        except Exception as e:
            for i in keylist:
                if i not in cardinfotmp.keys():
                    cardinfotmp[i] = pran.defalt_dict[i]
            break
    cardinfo[cardname] = cardinfotmp
    print(cardinfo[cardname], cardname)
print(cardinfo)
