from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
import os
import requests
import csv
import time
from pymysql import *
import re
import random
driver =webdriver.Firefox()
con = connect(host = 'localhost',port = 3306,user = 'root',password = 'mysql',database = 'guide',charset = 'utf8')
url = ""
#con = connect(host = ssh_host,port = 3306,user = 'root',password = '58265208',database = 'class',charset = 'utf8')
cs = con.cursor()
#打开网页

#解析页面

#创建文件夹
res = requests.session()
# res = None
def get_citys():
    # city_lis = ["杭州","上城区","下城区","江干区","拱墅区","西湖区","滨江区","余杭区","萧山区","富阳区","临安区","建德市","桐庐县","淳安县","宁波","海曙区","江北区","北仑区","镇海区","鄞州区","奉化区","余姚市","慈溪市","象山县","宁海县","温州","鹿城区","龙湾区","瓯海区","洞头区","瑞安市","乐清市","永嘉县","平阳县","苍南县","文成县","泰顺县","绍兴","越城区","柯桥区","上虞区","诸暨市","嵊州市","新昌县","湖州","吴兴区","南浔区","德清县","长兴县","安吉县","嘉兴","南湖区","秀洲区","海宁市","平湖市","桐乡市","嘉善县","海盐县  ","金华","婺城区","金东区","兰溪市","东阳市","永康市","义乌市","武义县","浦江县","磐安县","衢州 ","柯城区","衢江区","江山市","常山县","开化县","龙游县","台州","椒江区","黄岩区","路桥区","临海市","温岭市","玉环市","三门县","天台县","仙居县  ","丽水","莲都区","龙泉市","青田县","缙云县","遂昌县","松阳县","云和县","庆元县","景宁畲族自治县 ","舟山","定海区","普陀区","岱山县","嵊泗县"]
    city_lis = ["河北省","山西省","辽宁省","吉林省","黑龙江省","江苏省","浙江省","安徽省","福建省","江西","山东省","河南省","湖北省","湖南省","广东省","海南省","四川省","贵州省","云南省","陕西省","甘肃省","青海省","台湾省","内蒙古自治区","广西壮族自治区","西藏自治区","宁夏回族自治区","新疆维吾尔自治区","香港特别行政区","澳门特别行政区","","北京市","上海市","重庆市","天津市"]
    for each in city_lis:
        insert_city(each)
def insert_city(city):
    url = 'https://vacations.ctrip.com/list/whole/sc2.html?from=do&st='
    # city = "诸暨"
    url = url+city+"&startcity=2"

    driver.set_page_load_timeout(30) #设置页面超时时间

    driver.get(url)
    # driver.implicitly_wait(30)
    # time.sleep(5)
    # print(img_mes.text)
    img_element = driver.find_elements_by_class_name("list_product_pic")
    for each in img_element[:5]:
        try:
            src_string = each.get_attribute("src")
            alt_string  = each.get_attribute("alt")
            spans = alt_string.split('·')[-3:]
            response = res.get(src_string)
            kk = re.compile(r'[A-Za-z0-9_-]+\.?[A-Za-z0-9]*')
            filename = re.findall(kk,src_string)[-1]
            with open("img/"+filename,'wb+') as file:
                file.write(response.content)
            # print(alt_string)
            # print(src_string)
            sql = "insert into hot_buy_ticket(city_name,money,detail,photo_url,span1,span2,span3,sell_num) values(%s,%s,%s,%s,%s,%s,%s,%s);"
            money = str(random.randint(200,1200))
            detail = str(alt_string[:16]+'...')
            file_path = "img/"+filename
            post_data = [city,money,detail,file_path,spans[0],spans[1],spans[2],'0']
            # for each in post_data:
            #     print(type(each))

            # print(post_data)
            cs.execute(sql,post_data)
            con.commit()
        except:
            print(city+"wrong")

    # print(img_element)
#主函数
def main():
    get_citys()
    # time.sleep(10000)

    return 
    save = make(place)
    html = gethtml(place)
    for i in checkpage(html):
        save(i)
        print(i)
    # for i in range(2,101): 
    i = 2
        
    html = changepage(i)
    for fil in checkpage(html):
        save(fil)
        print(fil)
    driver.quit() 

#执行程序
if __name__ == '__main__':
    main()