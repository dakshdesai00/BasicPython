from GoogleNews import GoogleNews
googlenews=GoogleNews()
googlenews=GoogleNews('en')
googlenews.search('Corona Virus')
for i in range(10):
    print(str(googlenews.gettext()[i]))