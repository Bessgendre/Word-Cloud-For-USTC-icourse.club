from flask import Flask
from flask import render_template #渲染
from flask import request
 
app = Flask(__name__)


# 搜索页面
@app.route('/',  methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        # 渲染搜索页面 indexsearch.html
        return render_template('indexsearch.html')

    
# 保存图片并显示，只需要从前端传递一个搜索结果页面的URL过来
@app.route('/wordcloud')
def result():
    Names= []
    for i in range(6):
        Names.append('./wordcloud/' + str(i) + '.png')

    return render_template('wordcloud.html', PictureNames=Names)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80) #127.0.0.1 回路 自己返回自己
