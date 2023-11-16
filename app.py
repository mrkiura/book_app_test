from rizz_wsgi.api import API


app = API()


@app.route("/", allowed_methods=["get"])
def index(request, response):
    response.html = app.template("index.html")
