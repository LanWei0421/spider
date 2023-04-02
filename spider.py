#导入模块,第三方库
import urllib.request #自带模块
import re
import xlwt #


#1.获取HTML源代码  内置函数 
def getdate():#自定义函数 分装代码，减少代码冗余  函数体
    for i in range (1308,1340):
        print (i)
        url='http://www.shougolf.com/driving/'+str(i)
        print(url)
        html=urllib.request.urlopen(url).read().decode('utf-8')#urlopen打开网址 read获取所有源代码
        #print (html)#bytes字节类型 decode解码--string字符串类型 utf-8网页字符转码的标准（charset='utf-8')
#2从源代码解析数据，获取数据 .*? ()匹配同时取出
        page_list=re.findall( '<li><span>.*</span>.*</li>',html)
        print(page_list)       
#自定义函数必须要调用，否则没有结果出现
#items=getdate()

getdate()
#<li><em>2016-01-16 20:59</em><a href="/driving/1318" title="顺德新天地高尔夫运动广场" target="_blank">顺德新天地高尔夫运动广场</a> <label class="tag">打位48



#导入模块,第三方库
import urllib.request #自带模块
import re
import xlwt #


#1.获取HTML源代码  内置函数 
def getdate():#自定义函数 分装代码，减少代码冗余  函数体
    url_list=[]
    for i in range (1308,1340):
        print (i)
        url='http://www.shougolf.com/driving/'+str(i)
        print(url)
        html=urllib.request.urlopen(url).read().decode('utf-8')#urlopen打开网址 read获取所有源代码
        #print (html)#bytes字节类型 decode解码--string字符串类型 utf-8网页字符转码的标准（charset='utf-8')
#2从源代码解析数据，获取数据 .*? ()匹配同时取出
        page_list=re.findall( '<li><span>.*</span>.*</li>',html)
        print(page_list)
        url_list.append(page_list)
#自定义函数必须要调用，否则没有结果出现
#items=getdate()
    return url_list
getdate()
        
#3.自动化数据处理下载--excel表格
#创建excel文件，存储表头→将爬虫抓到内容存储到excel
items=getdate()
excel_write(items)
def excel_write(items):
    newTable='0709抓取'#文件名字
    wb=xlwt.workbook(encoding='utf-8')#创建excel 设置编码
    ws=wb.add_sheet('0709')#创建表
   
    #存储表头
    headData=['开业时间','开业时间','营业时间','打位个数','包厢个数','推杆果岭','练习沙坑','场地类型','球道长度']
    for column in range(0,9):#9个列，列名如headdata
        ws.write(0,colnum,headData[colnum]) #第0行数，列数，数据
#将爬虫抓取的内容存储到excel
    index=1    #初始化默认值 python第一行=excel第二行
    for j in range(0.32):
        for i in range(0.9): #9个表头标题
            ws.wrtite(index,i,items[j][i])
        index+=1
wb.save(nweTable)#保存


import urllib.request
import re
import xlwt
def getdate():
        url='http://www.shougolf.com/drivingmore?cityid=19/'
        html=urllib.request.urlopen(url).read().decode('utf-8')
        print(url)
        open_list=('<em>(.*)<em>',html)
        print(open_list)
getdate()

excel_write(items)