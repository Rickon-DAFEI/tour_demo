import requests
import io
import sys
from bs4 import BeautifulSoup
from PIL import Image
import urllib3
import os
import codecs
#from sshtunnel import SSHTunnelForwarder
from pymysql import *
import datetime
import time
session  = None

ssh_host = "106.13.164.235"  # 堡垒机ip地址或主机名
ssh_port = 22  # 堡垒机连接mysql服务器的端口号，一般都是22，必须是数字
ssh_user = "root"  # 这是你在堡垒机上的用户名
ssh_password = "wy@58265208"  # 这是你在堡垒机上的用户密码
mysql_host = "localhost"  # 这是你mysql服务器的主机名或ip地址
mysql_port = 3306  # 这是你mysql服务器上的端口，3306，mysql就是3306，必须是数字
mysql_user = "root"  # 这是你mysql数据库上的用户名
mysql_password = "mysql"  # 这是你mysql数据库的密码
mysql_db = "guide"  # mysql服务器上的数据库名

'''
with SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_password=ssh_password,
        remote_bind_address=(mysql_host, mysql_port)) as server:
    con = connect(host=mysql_host,
                           port=server.local_bind_port,
                           user=mysql_user,
                           passwd=mysql_password,
                           db=mysql_db)
    cs = con.cursor()
'''

res = requests.Session()
rqs = requests.session()

Origin_url = "http://jwxt.zjyc.edu.cn/"
login_url = "http://jwxt.zjyc.edu.cn//default2.aspx"

check_codeUrl = Origin_url+"CheckCode.aspx"

headers = {
"Origin": "https://piao.ctrip.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
}
post_data = {'Textbox1':'none',"Button1":"","lbLanguage":"","hidPdrs":"","hidsc":""}
user_name = '20070035'  
user_password = '123.com'
xm = user_name
con = connect(host = 'localhost',port = 3306,user = 'root',password = 'mysql',database = 'guide',charset = 'utf8')
url = ""
#con = connect(host = ssh_host,port = 3306,user = 'root',password = '58265208',database = 'class',charset = 'utf8')
cs = con.cursor()
try:
    sql = 'drop table ClassList;'
    cs.execute(sql)
except:
    pass
# sql = 'create table if not exists ClassList(序号 int unsigned auto_increment primary key, 教师 varchar(100),编码 varchar(100),课程 varchar(100),日期 varchar(100),教室 varchar(100))DEFAULT CHARACTER SET = utf8;'
# cs.execute(sql)
def login():
    loginPage = rqs.get(login_url)
    loginPage = str(loginPage.content.decode('gbk'))
    VIEW= BeautifulSoup(loginPage,"html.parser")
    __VIEWSTATE= VIEW.find('input', attrs={'name': '__VIEWSTATE'})['value']
    post_data = {
            '__VIEWSTATE': __VIEWSTATE,
            'txtUserName': user_name,
            'TextBox2': user_password,
            'txtSecretCode': get_photo(),
            'RadioButtonList1': ("教师").encode('gb2312'),
            'Button1': '',
            'lbLanguage': '',
            'hidPdrs': '',
            'hidsc': '',
        }
    head['Referer'] = login_url
    homePage = res.post(login_url, data=post_data, headers=head) 
    cookies = homePage.cookies	
    homePage = str(homePage.content.decode('gbk'))
    bs = BeautifulSoup(homePage,"html.parser")
    try:
        xm= bs.find('span',id="xhxm").text
        xm=xm[:-2]
        print("教师："+xm+"登陆成功")
    except:
        print("验证码输入错误!")
        login()
    xmcode = xm_Code(xm)
    teacherName = xm
    get_classList(teacherName)

def get_classList(teacherName):
    res.headers['Referer'] ="http://jwxt.zjyc.edu.cn/js_main.aspx?xh="+user_name
    url = Origin_url+"/js_xkqk_gcxy.aspx?zgh="+user_name+"&xm="+xm+"&gnmkdm=N122304"   
    response = res.get(url, allow_redirects=False)
    #with open('课表.html','wb')as f:
     #   f.write(response.content)
    response = str(response.content.decode('gbk'))
    classSoup = BeautifulSoup(response,"html.parser")
    studentList__VIEWSTATE = classSoup.find('input', attrs={'name': '__VIEWSTATE'})['value']
    xn = classSoup.find(id = 'xn').find_all('option')
    xq = classSoup.find(id = 'xq').find_all('option')
    for each in xn:
        try:
            str(each).index('selected')
            xn = each['value']
            break
        except:
            continue
    for each in xq:
        try:
            str(each).index('selected')
            xq = each['value']
            break
        except:
            continue
    res.headers['Referer'] = url
    a_list =classSoup.find(id="kcmc")
    for i in a_list.find_all('option'):
        v = i['value']
        text = i.text
        cls = {
        'code':v,
        'name':'',
        'date':'',
        'room':'',
        }
        analys(text,cls)
        data = [teacherName,cls['code'],cls['name'],cls['date'],cls['room']]
        cs.execute("insert into ClassList(教师,编码,课程,日期,教室) values(%s,%s,%s,%s,%s);",data)
        fromdata = {
            '__EVENTTARGET':'kcmc',
            '__EVENTARGUMENT':'',
            '__VIEWSTATE':studentList__VIEWSTATE,
            'xn':xn,
            'xq':xq,
            'jfz':0,
            'kcmc':v,
            'ddlbj':' '
            }
        response = res.post(url, allow_redirects=False,data = fromdata)
        response = str(response.content.decode('gbk'))
        List = BeautifulSoup(response,"html.parser")
        stdList = List.find('div',attrs={'class':'formbox'})
        st = stdList.find_all('tr')
        try:
            sql = 'drop table %s;'
            cs.execute(sql%cls['name'])
        except:
            pass
        sql = 'create table if not exists  %s(学号 varchar(25) primary key , 姓名 varchar(100),专业名称 varchar(100),班级名称 varchar(100),成绩 decimal(5,2), 学分 decimal(5,2), 绩点 decimal(5,2), 备注 varchar(30))'
        cs.execute(sql%cls['name'])
        con.commit()
        flag = 1
        for each in st:
            if (flag):
                flag = 0
                continue;
            td = each.find_all('td')
            stMas = []
            for i in td:
                stMas.append(i.text)
            sql = "insert into "+cls['name']+"(学号,姓名,专业名称,班级名称,成绩,学分,绩点,备注) values(%s,%s,%s,%s,%s,%s,%s,%s);"
            cs.execute(sql,stMas)
def analys(t,c):
    a = t.index('【')

    b = t.index('】')

    e = t.index('/')

    c['name'] = t[:a]
    c['date'] = t[a+1:e]
    c['room'] = t[e+1:b]

def get_photo():
    checkcode = res.get(check_codeUrl, headers=head)
    with open('code.gif', 'wb') as fp:
         fp.write(checkcode.content)
    image = Image.open('code.gif'.format(os.getcwd()))
    image.show()
    imageCode = input("请输入图片中的验证码: ") 
    return imageCode

def xm_Code(xmcode):
    heads = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    code_data = {'content': xmcode,'charsetSelect': 'gb2312','en': 'UrlEncode编码'}
    code_url = 'http://tool.chinaz.com/tools/urlencode.aspx'
    coding_site = rqs.post(code_url,headers =heads,data = code_data)
    s = coding_site.content
    coding_site=str(s)
    code_bs = BeautifulSoup(coding_site,"html.parser")
    xm_str = code_bs.find('textarea',id = "content").text
    return xm_str

def class_table(table_html):
      pass 

# def main(h=4,m=0):
# 	'''
#     while True:
#         now = datetime.datetime.now()
# # print(now.hour, now.minute)
#         if now.hour == h and now.minute == m:
#             break
# # 每隔60秒检测一次
#     time.sleep(60)
# 	'''
# 	login()
#     	con.commit()
#     	cs.close()
#     	con.close()
# print("Finished")

def main():
    guide_url = "https://vacations.ctrip.com/list/whole/sc2.html?from=do&st="
    place_name = "诸暨"+"&startcity=2"
    place_homesite = rqs.get(guide_url+place_name)
    with open("1.html",'wb+') as f:
        f.write(place_homesite.content)


if __name__ == "__main__":
    main() 
