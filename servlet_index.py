from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Requires, Validate, Invalidate, Unbind, Bind, Instantiate

from pelix.http import HTTP_SERVLET, HTTP_SERVLET_PATH

@ComponentFactory()
@Instantiate('index-servlet')
@Provides(HTTP_SERVLET)
@Property('_path', 'pelix.http.path', "/")
class IndexServletFactory(object):
  def __init__(self):
      self._path = None

  def bound_to(self, path, params):
      return True

  def unbound_from(self, path, params):
      return None

  def do_GET(self, request, response):
      content = """<html>
<head>
<meta charset="UTF-8"> 
<title>ipopo game server</title>
</head>
<body>
    <h1>Games</h1>
    <div>
        <a href="/tictactoe">Tic Tac Toe</a>
    </div>
</body>
</html>
"""

      response.send_content(200, content)
