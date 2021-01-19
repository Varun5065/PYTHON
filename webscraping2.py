# to get all the books with a 2 star rating
import requests
import bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html' # a webpage for scraping
two_star = []
for i in range(1, 51): # all the 50 pages in the website
    res = requests.get(base_url.format(i))
    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod") # list of all the books prsent in the class product_pod
    for book in books:
        if len(book.select('.star-rating.Two')) != 0: # if the list is not empty(i.e, star_rating Two class exists for the book)
            title = book.select("a")[1]['title'] # the book title is selected and appended into a list
            two_star.append(title)
for i in range(0, len(two_star)):
    print(two_star[i])
