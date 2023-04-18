from flask import Flask
from flask import render_template #渲染
 
app = Flask(__name__)
@app.route('/') #主页地址,“装饰器”
def news():
    the_news = {
            'XXX1':'1',
            'XXX2':'2',
            'XXX3':'3',
            'XXX4':'4',
    }
    context = {
        'title':'新闻',
        'the_news': the_news,
    }
    return render_template('index.html',context=context) #把index.html文件读进来，再交给浏览器
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80) #127.0.0.1 回路 自己返回自己
