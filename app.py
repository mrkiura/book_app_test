from rizz_wsgi.api import API
from storage import BookStorage
from book_factory import test_books
from auth import login_required, STATIC_TOKEN, TokenMiddleware, on_exception
from rizz_wsgi.response import Response
from rizz_wsgi.request import Request


app = API()
book_storage = BookStorage()
book_storage.bulk_create(test_books)

app.add_middleware(TokenMiddleware)
app.add_exception_handler(on_exception)


@app.route("/", allowed_methods=["get"])
def index(request: Request, response: Response):
    books = book_storage.all()
    response.html = app.template("index.html", context={"books": books})


@app.route("/login", allowed_methods=["post"])
def login(request: Request, response: Response):
    response.json = {"token": STATIC_TOKEN}


@app.route("/books", allowed_methods=["post"])
@login_required
def create_book(request: Request, response: Response):
    book = book_storage.create(**request.POST)

    response.status_code = 201
    response.json = book._asdict()


@app.route("/books/{id:d}", allowed_methods=["delete"])
@login_required
def delete_book(request: Request, response: Response, id: str):
    book_storage.delete(id)
    response.status_code = 204
