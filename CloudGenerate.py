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
    

Course_Name = "马克思主义基本原理"


# get all links
links = web.SearchCourse(Course_Name)
print("course searching finished")

# excavate words with multi-thread
comments_thd = list(map(CommentsThread,links))

for threads in comments_thd:
    threads.start()
for threads in comments_thd:
    threads.join()

all_course_comments = []
for i in range(len(links)):
    all_course_comments.append(comments_thd[i].get_result())
print("words extracted")

print("generating wordcloud...")

for i in range(len(all_course_comments)):
    web.TheWordCloud(all_course_comments[i],i)
    print(str(i) + " picture is generated")
    
print("finished, check static//wordcloud!")