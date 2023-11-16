from rizz_wsgi.api import API
from storage import BookStorage
from book_factory import test_books
from auth import STATIC_TOKEN


app = API()
book_storage = BookStorage()
book_storage.bulk_create(test_books)


@app.route("/", allowed_methods=["get"])
def index(request, response):
    books = book_storage.all()
    response.html = app.template("index.html", context={"books": books})


@app.route("/login", allowed_methods=["post"])
def login(request, response):
    response.json = {"token": STATIC_TOKEN}
