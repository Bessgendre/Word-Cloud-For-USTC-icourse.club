from flask import Flask
from flask import render_template #渲染
from flask import request

# # 数值计算
# import numpy as np


# # 绘图
# import matplotlib.pyplot as plt
# import seaborn as sns
# from wordcloud import WordCloud
# from imageio import imread

# # 浏览器控制
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# #网站解析
# import requests, lxml
# from bs4 import BeautifulSoup
# import jieba

# #自定义模块
# import package.web as web

# # 多线程
# from threading import Thread
 
app = Flask(__name__)


# 搜索页面
@app.route('/',  methods = ['POST', 'GET']) #主页地址,“装饰器”
def index():
    if request.method == 'GET':
        # 渲染搜索页面 indexsearch.html
        return render_template('indexsearch.html')
    
    # elif request.method == 'POST':
    #     # 获取数据
    #     webresult = request.args.get('course_name')
        
    #     # 返回到前端去
    #     return render_template('wordcloud.html',data=webresult)

    # return render_template('indexsearch.html')


# 保存图片并显示
@app.route('/wordcloud')
def wordcloud():
    return render_template('wordcloud.html')
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80) #127.0.0.1 回路 自己返回自己
