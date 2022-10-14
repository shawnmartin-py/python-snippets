books = [],
URL = None
urlopen = None

def get_books():
    for isbn in books:
        fetch(isbn)

def fetch(isbn):
    url = URL.format(isbn)
    download(url)

def download(url):
    u = urlopen(url)
    data = u.read()
    return data

# architecture

def get_books():
    urls = book_urls(books)
    for url in urls:
        u = urlopen(url)
        data = u.read()

def book_urls(books):
    for isbn in books:
        yield build_url(isbn)

def build_url(isbn):
    return URL.format(isbn)