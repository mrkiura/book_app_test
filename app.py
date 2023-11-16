from rizz_wsgi.api import API
from storage import BookStorage


app = API()
book_storage = BookStorage()
book_storage.create(name="Mastery", author="Robert Greene")


@app.route("/", allowed_methods=["get"])
def index(request, response):
    books = book_storage.all()
    response.html = app.template("index.html", context={"books": books})
