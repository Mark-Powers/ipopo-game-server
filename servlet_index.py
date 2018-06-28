from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Requires, Validate, Invalidate, Unbind, Bind, Instantiate

from pelix.http import HTTP_SERVLET, HTTP_SERVLET_PATH
from pelix.http.routing import RestDispatcher, HttpGet, HttpPost, HttpPut

@ComponentFactory()
@Instantiate('index-servlet')
@Provides(HTTP_SERVLET)
@Property('_path', 'pelix.http.path', "/")
class IndexServletFactory(RestDispatcher):
    def __init__(self):
        super(IndexServletFactory, self).__init__()
        self._path = None

    def bound_to(self, path, params):
        return True

    def unbound_from(self, path, params):
        return None

    @HttpGet("/")
    def get_index(self, request, response):
        content = """<html>
<head>
<meta charset="UTF-8"> 
<title>ipopo game server</title>
</head>
<body>
    <div>
        <h1>Games</h1>
        <div>
            <a href="/tictactoe">Tic Tac Toe</a>
        </div>
        <div>
            <a href="/set_theme/1">Set Theme</a>
            <a href="/reset_theme">Reset Theme</a>
        </div>
    </div>
</body>
</html>
"""        
        cookie = request.get_header("Cookie")
        print(cookie)
        #response.set_header("Cookie", cookie)
        response.send_content(200, content)

    @HttpGet("/set_theme/<number:string>")
    def set_theme(self, request, response, number):
        response.set_header("Set-Cookie", "theme="+number)
        self.get_index(request, response)

    @HttpGet("/reset_theme")
    def reset_theme(self, request, response):
        response.set_header("Set-Cookie", "theme=deleted; Expires=Thu, 01 Jan 1970 00:00:01")
        self.get_index(request, response)
        
