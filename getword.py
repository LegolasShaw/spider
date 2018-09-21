# -*- coding: gbk -*-
import sys
import os

from bs4 import BeautifulSoup


from urllib import request
from urllib import parse
from urllib import error
import time

if __name__ == "__main__":
    try:
        file = open('text.txt', 'a' ,encoding='utf-8')

        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Cache-Control': 'max-age=0',
                   'Connection': 'keep-alive',
                   'Host': 'www.cqdsrb.com.cn',
                   'Upgrade-Insecure-Requests': '1',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
                   }

        article_num = 0
        for i in range(167, 355):
            requests = request.Request(url='http://www.cqdsrb.com.cn/portal.php?mod=list&catid=10&page=%d'%i,
                                       headers=headers)
            time.sleep(10)

            print("pages:" + str(i))
            response = request.urlopen(requests)

            html = response.read()

            soup = BeautifulSoup(html)
            target_a = soup.find_all("a", class_='xi2', target="_blank")

            for a in target_a:
                url = a.attrs['href']
                requests = request.Request(url=url, headers=headers)
                # time.sleep(1)
                response = request.urlopen(requests)
                html = response.read()
                soup = BeautifulSoup(html)
                td = soup.find("td", id="article_content")
                p_arr = td.find_all("p")
                content = ''
                for p in p_arr:
                    if p.string is not None:
                        content = content + p.string.strip().replace("\n","").replace("\r","")
                if content == '\n':
                    content.replace('\n', "")
                    print(content)

                if content.strip() != '':
                    print(content)
                    article_num += 1
                    print("articlenum:" + str(article_num))
                    file.write(content + '\n')
        file.close()
    except:
        file.close()



# class SpiderGetcqdsrbArticle():
#     def __init__(self):
#         self.url_pool = []
#         self.url_done_arr = []
#
#     def








