
import feedparser
from win10toast import ToastNotifier
import os
from datetime import date

t = ToastNotifier()
def Parsefeed():
    c = input("Enter country :\n1.UK\n2.India")
    if (c=='1' or c=='UK'):
        f1 = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
        f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
    else : 
        f1 = feedparser.parse("https://feeds.feedburner.com/ndtvnews-top-stories")
        f = feedparser.parse("https://feeds.feedburner.com/ndtvnews-top-stories")
    ICON_PATH = os.getcwd() + "/icon.ico"
    for newsitem in f['items']:
        if c<=5:
            modified = f1.get('modified')
            if modified is not None:
                print(modified)
                print(newsitem['title'])
                title = newsitem['title']
                print(newsitem['summary'])
                print('\n')
                summary = modified  + '\n' + newsitem['summary']
                t.show_toast(title,summary,ICON_PATH,duration = 10)
                c = c+1
            else :
                if c<=5:
                    today = date.today()
                    modified = today.strftime("%B %d, %Y")
                    print(modified)
                    print(newsitem['title'])
                    title = newsitem['title']
                    print(newsitem['summary'])
                    print('\n')
                    summary = modified  + '\n' + newsitem['summary']
                    t.show_toast(title,summary,ICON_PATH,duration = 10)
                    c = c+1

if __name__ == '__main__':
    try:
        Parsefeed()
    except:
        print("Error")
