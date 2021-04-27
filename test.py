import webbrowser

myfile = open("urls.txt","r")
urls = myfile.readlines()
myfile.close()
for url in urls:
    webbrowser.open(url,new=1)