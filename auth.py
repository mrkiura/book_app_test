import re
from rizz_wsgi.middleware import Middleware


STATIC_TOKEN = "6cc37289cff1440f95363c43388d91b4"


class TokenMiddleware(Middleware):
    _regex = re.compile(r"^Token: (\w+)$")

    def process_request(self, request):
        header = request.headers.get("Authorization", "")
        match = self._regex.match(header)
        token = match and match.group(1) or None
        request.token = token