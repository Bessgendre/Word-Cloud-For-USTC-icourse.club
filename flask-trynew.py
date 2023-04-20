from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # 渲染index页面
        return render_template('form.html')
    elif request.method == 'POST':
        # 获取数据
        data = {}
        data['name'] = request.args.get('name')   # 后面这个name和前端的name保持一致
        data['passwd'] = request.args.get('password')

        # 返回到前端去
        return render_template('formresult.html', data=data)

@app.route('/index')
def index():
    return render_template('formresult.html', data=data)  # 渲染当前的html页面
app.run()
