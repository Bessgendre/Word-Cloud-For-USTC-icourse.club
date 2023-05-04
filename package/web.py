import matplotlib.pyplot as plt

# wordcloud
from wordcloud import WordCloud
from imageio import imread

# webpage analysis
import requests, lxml
from bs4 import BeautifulSoup
import jieba

def SearchCourse(course_name):
    # With the name of a course, SearchCourse returns links of the same course taught by different teachers. This shall be the first step for a student when choosing courses at the beginning of every semester.
    
    root_path = 'https://icourse.club'
    
    html = requests.get(root_path + '/search/?q=' + course_name)
    soup = BeautifulSoup(html.text,"lxml")
    raw_link_sourse = soup.find_all(name='a',attrs={"class":"px16"})

    links = []
    for link_sourse in raw_link_sourse:
        links = links + [root_path + str(link_sourse.get('href'))]
    
    return links

def GetComment(url):
    # GetComment is a function appling to the icourse.club that can extract all comments under a single course taught by one lecturer.
    # input the url of that course, and return all comments in one list.
    
    # analysis the page
    html = requests.get(url)
    soup = BeautifulSoup(html.text,"lxml")

    # extract comments
    rawcomments = soup.find_all(name='div',attrs={"class":"review-content"})
    comments = []
    for content in rawcomments:
        comments = comments + [content.get_text()]
    
    return comments

def CatchWords(comments):
    # CatchWords is a function that decompose the list of comments into key words. it is recommended to act on the result of GetComment.
    
    if len(comments) == 0:
        return "error"
    
    # choose worthy comments as long as possible
    worthycomments = []
    for chunk in comments:
        if len(chunk) >= 200:
            worthycomments = worthycomments + [chunk]       

    if worthycomments == []:
        for chunk in comments:
            if len(chunk) >= 100:
                worthycomments = worthycomments + [chunk] 

    if worthycomments == []:
        worthycomments = comments
    
    allcomments = ' \n '.join(worthycomments)
       
        
    # divide words with jieba
    seg_str = jieba.cut(allcomments, cut_all=False)
    liststr = "/".join(seg_str)

    # read stopwords
    stopwords_path = "./stopwords.txt"
    f_stop=open(stopwords_path, encoding='utf8')
    f_stop_text = f_stop.read()
    f_stop.close()

    mywordlist=[]
    f_stop_seg_list = f_stop_text.split('\n')

    # create the mywordlist for wordcloud generation
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list)and len(myword.strip())>1:
            mywordlist.append(myword)
            
    return mywordlist

def TheWordCloud(comments,FileNumber):
    # TheWordCloud is an integrated function that combines all functions above, leading to the generation of a wordcloud.
    # It is fed on list of comments (which is based on GetComments) and FileNumber is the number used to name the wordcloud.png
    
    if len(comments) == 0:
        return "error, no comments under this course!"
    # word excavation
    words = ' '.join(CatchWords(comments))
    
    # plot the wordcloud
    
    # bg = "./static/USTC.jpg"
    # imgbg = imread(bg)

    a = WordCloud(font_path = "./font/simkai.ttf", 
                  background_color = 'white', 
                  width = 1618, 
                  height =1000,
                #   mask = imgbg,
                  scale = 2,
                  colormap = "summer")
    
    a.generate(words)
    plt.imshow(a)
    plt.axis("off")
    plt.savefig('./static/wordcloud/' + str(FileNumber) + '.png')
    
    
    