import feedparser
from win10toast import ToastNotifier
import os
from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

t = ToastNotifier()
def Parsefeed():
    c = input("Enter country :\n1.UK\n2.India\n3.Exit")
    if (c == '1' or c=='UK'):
        f1 = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
        f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    elif(c == '2' or c == 'India') : 
        f1 = feedparser.parse("https://feeds.feedburner.com/ndtvnews-top-stories")
        f = feedparser.parse("https://feeds.feedburner.com/ndtvnews-top-stories")
    else:
        os._exit
    ICON_PATH = os.getcwd() + "/icon.ico"
    d=1
    for newsitem in f['items']:
        if d<=10:
            modified = f1.get('modified')
            if modified is not None:
                print(modified)
                print(newsitem['title'])
                title = newsitem['title']
                print(newsitem['summary'])
                print('\n')
                summary = modified  + '\n' + newsitem['summary']
                t.show_toast(title,summary,ICON_PATH,duration = 10)
                d = d+1
            else :
                today = date.today()
                modified = today.strftime("%B %d, %Y")
                print(modified)
                print(newsitem['title'])
                title = newsitem['title']
                print(newsitem['summary'])
                print('\n')
                summary = modified  + '\n' + newsitem['summary']
                t.show_toast(title,summary,ICON_PATH,duration = 10)
                d = d+1

if __name__ == '__main__':
    try:
        Parsefeed()
        scheduler = BlockingScheduler()
        scheduler.add_job(Parsefeed,'interval',hour = 1)
        scheduler.start()
    except:
        print("Error")
