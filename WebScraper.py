from urllib.request  import urlopen
import re

title = "<title>"
endTitle = "</title>"

url1 = "http://olympus.realpython.org/profiles/aphrodite"

web_page = urlopen(url1)
html_bytes = web_page.read()
html = html_bytes.decode("utf-8")

print (html)


title_index_start = html.find(title)
print (title_index_start)

start_of_profile = title_index_start + len(title)
print(start_of_profile)

title_index_end = html.find(endTitle)
print (title_index_end)

profile_name = html[start_of_profile:title_index_end]
print (profile_name)