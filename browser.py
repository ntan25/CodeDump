import webbrowser

# webbrowser.open("https://www.python.org/", new= 2)
#
# help(webbrowser)
chrome = webbrowser.get(using= "chrome")
chrome.open_new("https://python.org/")

