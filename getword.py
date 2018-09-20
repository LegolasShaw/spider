# -*- coding: utf-8 -*-
import sys
import os

from bs4 import BeautifulSoup


from urllib import request
from urllib import parse
from urllib import error

if __name__ == "__main__":
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Cookie': 'acw_tc=76b20f6915374526092361619e40058b7636d3c7a1dada419ec3e92dba2a45; r5qs_2132_saltkey=RWwt0gT9; r5qs_2132_lastvisit=1537449009; r5qs_2132_sid=QyH9w3; PHPSESSID=rmds5tjphnu2gcbqrju95rchn5; r5qs_2132_pc_size_c=0; pgv_pvi=1504000440; pgv_info=ssi=s9367727272; _trs_uv=4b9v_15_jmanl6ct; _trs_ua_s_1=3b9p_15_jmanl6ct; UM_distinctid=165f75112cc3bb-07d2098df4865f-346a7809-13c680-165f75112cd89a; CNZZDATA1000388759=1801767827-1537450728-%7C1537450728; _fmdata=2GrXe4EFBliBndSeM39qMPpUc0ItPowxXillNhedPI883ObzDJvCyqnyqPjnfWor%2BhtJB3QOjDlw6NvSCrX3MOps4Phg0fGGqS%2BCS%2FBMbzo%3D; r5qs_2132_lastact=1537452858%09connect.php%09check',
               'Host': 'www.cqdsrb.com.cn',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
                              }
    requests = request.Request(url='http://www.cqdsrb.com.cn/portal.php?mod=list&catid=10',
                               headers=headers)

    response = request.urlopen(requests)

    html = response.read()

    soup = BeautifulSoup(html)
    target_a = soup.find_all("a", class_='xi2', target="_blank")

    for a in target_a:
        url = a.attrs['href']
        requests = request.Request(url=url)
        response = request.urlopen(requests)
        html = response.read()
        soup = BeautifulSoup(html)
        td = soup.find("td", id="article_content")
        p_arr = td.find_all("p")
        for p in p_arr:
            print(p.string)







