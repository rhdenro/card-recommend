import pran
import copy
def exchange(money,date=1):
    tmp_money=money
    tmpcost=0
    if ',' in tmp_money:
        tmp_money=tmp_money.replace(',', '')
    if '원' in tmp_money:
        tmp_money=tmp_money.replace('원','')
    if '만' in money:
        tmpcost += int(tmp_money[:money.find('만')]) * 10000
    if '천' in money:
       tmpcost+=int(tmp_money[money.find('천')-1])*1000
    if tmpcost==0:
        return tmp_money
    return str(tmpcost//date)
def movie_dict_fenc(cardinfotmp,cost):
    tmp_movie=copy.deepcopy(pran.movie_dict)
    flag=False
    count=0
    for i in cardinfotmp:
        if i.replace(',','')  in tmp_movie.keys():
            tmp_movie[i.replace(',','')]=cost
            count+=1
            flag=True
    if count == 2:
        tmp_movie['all'] = cost
        tmp_movie['롯데시네마'] = None
        tmp_movie['CGV'] = None
        return tmp_movie
    if flag == False:
        tmp_movie['all']=cost
    return tmp_movie

def convenience_dict_fenc(cardinfotmp,cost):
    tmp_convenience=copy.deepcopy(pran.convenience_dict)
    flag=False
    count=0
    for i in cardinfotmp:
        if i.replace(',','')  in tmp_convenience.keys():
            tmp_convenience[i.replace(',','')]=cost
            count+=1
            flag=True
    if count == 4:
        tmp_convenience['all'] = cost
        tmp_convenience['CU'] = None
        tmp_convenience['GS25'] = None
        tmp_convenience['세븐일레븐'] = None
        tmp_convenience['미니스톱'] = None
        return tmp_convenience
    if flag == False:
        tmp_convenience['all']=cost

    return tmp_convenience
