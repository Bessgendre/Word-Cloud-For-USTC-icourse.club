from flask import Flask
from flask import render_template #渲染
from flask import request

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

app = Flask(__name__)


# 搜索页面
@app.route('/',  methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        # 渲染搜索页面 indexsearch.html
        return render_template('indexsearch.html')

    
# 保存图片并显示，只需要从前端传递一个搜索结果页面的URL过来
@app.route('/wordcloud',  methods = ['POST', 'GET'])
def result():
    Course_Name = str(request.args.get('name'))

    # f = open("./static/name.txt")
    # Course_Name = f.read()
    # f.close()

    # 获得一个搜索结果下的所有课程链接
    links = web.SearchCourse(Course_Name)
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

    k = 0
    for i in range(len(all_course_comments)):
        
        if len(all_course_comments[i]) != 0:
            web.TheWordCloud(all_course_comments[i],i)
            k = k + 1
            print(str(k) + " picture drown...")

    print("all pictures finished, please check static//wordcloud")
    
    
    Names= []
    for i in range(6):
        Names.append('./wordcloud/' + str(i) + '.png')

    return render_template('wordcloud.html', PictureNames=Names)


if __name__ == '__main__':
    app.run()
