# -*- coding: UTF-8 -*-
import requests
from urllib.request import urlopen
import urllib3
from multiprocessing import Pool
import time
file=open('C:/Users/asdfg/Desktop/pubmed_pmid_1000.txt')
pmid=file.readlines()

def get_url():
    url_list=[]
    for i in pmid:
        url='https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids='+str(i)
        url_list.append(url)
    return url_list

def get_data(url):
    http=urllib3.PoolManager()
    data_list=[]
    res=http.request('GET',url)
    #global data
    data=str(res.data,encoding='utf-8')
    data_list.append(data)
    time.sleep(6)
    return data_list
    
   
if __name__=='__main__':
    urls=get_url()
    file=open('D:/test2.txt','w+',encoding='utf-8')
    time1=time.time()
    pool=Pool(processes=8)#设置进程数目
    result=pool.map(get_data,urls)
    pool.close()
    pool.join()
    #get_data(urls)
    time2=time.time()
    time=time2-time1
    print('time:',time)
    for i in result:
        mystr=str(i)
        file.write(mystr.strip("['b']"))
    file.close()
    print('done')
    
