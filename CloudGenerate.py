# 数值计算
# import numpy as np

# 绘图
# from wordcloud import WordCloud
# from imageio import imread

# 浏览器控制
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

#网站解析
# import requests, lxml
# from bs4 import BeautifulSoup
# import jieba

#自定义模块
import package.web as web

# 多线程
from threading import Thread

# 多线程获得返回值的 CommentsThread 类
class CommentsThread(Thread):

    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        self.result = web.GetComment(self.url)

    def get_result(self):
        return self.result
    
f = open("./static/name.txt")
Course_Name = f.read()
f.close()

# 获得一个搜索结果下的所有课程链接
links = web.SearchCourse(Course_Name)
print("course searching finished")

# 初始化线程
comments_thd = list(map(CommentsThread,links))

#多进程的开始与结束
for threads in comments_thd:
    threads.start()
for threads in comments_thd:
    threads.join()

# 综合一下结果
all_course_comments = []
for i in range(len(links)):
    all_course_comments.append(comments_thd[i].get_result())
    
print("words extracted")

print("generating wordcloud...")

for i in range(len(all_course_comments)):
    web.TheWordCloud(all_course_comments[i],i)
