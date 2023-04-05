import requests
from bs4 import BeautifulSoup

def GetComment(url):
    # GetComment 是一个用于提取评课社区某一门课下所有课评的函数
    # 输入这门课的 url ，以 list 形式返回这门课的所有课评，列表元素为字符串
    
    # 获取源码并解析
    html = requests.get(url)
    soup = BeautifulSoup(html.text,"lxml")

    # 提取课评内容
    rawcomments = soup.find_all(name='div',attrs={"class":"review-content"})
    comments = []
    for content in rawcomments:
        comments = comments + [content.get_text()]
    
    # 以列表形式返回一门课的课评，列表元素为字符串
    return comments