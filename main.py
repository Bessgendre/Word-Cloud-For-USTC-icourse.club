from flask import Flask
from flask import render_template
from flask import request


import package.web as web


from threading import Thread
 
# CommentsThread helps to get result from threads
class CommentsThread(Thread):

    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        self.result = web.GetComment(self.url)

    def get_result(self):
        return self.result

app = Flask(__name__)


# a beautiful searching page
@app.route('/',  methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('indexsearch.html')

    
# a beautiful presenting page
@app.route('/wordcloud',  methods = ['POST', 'GET'])
def result():
    Course_Name = str(request.args.get('name'))

    # get links and comments
    links = web.SearchCourse(Course_Name)
    comments_thd = list(map(CommentsThread,links))
    
    for threads in comments_thd:
        threads.start()
    for threads in comments_thd:
        threads.join()

    all_course_comments = []
    for i in range(len(links)):
        all_course_comments.append(comments_thd[i].get_result())

    # generating wordclouds
    k = 0
    for i in range(len(all_course_comments)):
        
        if len(all_course_comments[i]) != 0:
            web.TheWordCloud(all_course_comments[i],i)
            k = k + 1
            print(str(k) + " picture drown...")

    print("all pictures finished, please check static//wordcloud")
    
    # present these pictures
    Names= []
    for i in range(6):
        Names.append('./wordcloud/' + str(i) + '.png')

    return render_template('wordcloud.html', PictureNames=Names)


if __name__ == '__main__':
    app.run()
