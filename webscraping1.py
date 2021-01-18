# Grabbing a title from webpage with python
import requests
import bs4

result = requests.get("http://www.example.com") # any domain can be taken (permission included) this is a dummy website
print(type(result))  # prints the class og the result
# print(result.text)# prints the source code
soup = bs4.BeautifulSoup(result.text, "lxml")  # prints the source code in a html format
title = soup.select('title')  # creates a list of the text present in the tags
print(title)  # prints the list
site_para = soup.select('p') # selects all the text enclosed in <p> tags(can be more than 1)
print(site_para[1].getText()) # prints only the text of the second para enclosed by <p>
