import webbrowser
lib = input('what')
url = 'https://www.youtube.com/results?search_query='+str(lib)
webbrowser.open_new(url)
