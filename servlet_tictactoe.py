from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Requires, Validate, Invalidate, Unbind, Bind, Instantiate

from pelix.http import HTTP_SERVLET, HTTP_SERVLET_PATH
from pelix.http.routing import RestDispatcher, HttpGet, HttpPost, HttpPut

@ComponentFactory()
@Instantiate('simple-servlet')
@Requires("_srv", 'game_tictactoe_service')
@Provides(HTTP_SERVLET)
@Property('_path', 'pelix.http.path', "/tictactoe")
class TicTacToeServletFactory(RestDispatcher):
  def __init__(self):
      super(TicTacToeServletFactory, self).__init__()
      self._path = None

  def bound_to(self, path, params):
      return True

  def unbound_from(self, path, params):
      return None

  @HttpGet("/set/<x:int>/<y:int>")
  def set_board(self, request, response, x, y):
    self._srv.setPos(x, y);
    self.show_board(request, response);

  @HttpGet("/")  
  def show_board(self, request, response):
      content = """<html>
<head>
<meta charset="UTF-8"> 
<title>Tic Tac Toe</title>
<style>
table {
    border-collapse: collapse;
    border-style: hidden;
    align: center;
    margin: 100px auto 50px auto;
}
table td {
    border: 3px solid black;
    font-size: 40px;
    font-family: "Courier New", monospace;
    width: 50px;
    height: 50px;
}
</style>
</head>
<body>
<table>
"""
      for x in range(3):
        content += "<tr>\n"
        for y in range(3):
          value = self._srv.getPos(x, y)
          content+= "<td><a href="
          content+= '"/tictactoe/set/' + str(x) +'/' + str(y) + '"'
          content+= ">" 
          content+= value
          content+= "</a></td>\n"
        content += "</tr>\n"
      content += """
</table>\n"""
      if self._srv.checkWinner():
          content+="<h2>GAME OVER</h2>\n"

      content += """</body>
</html>"""

      response.send_content(200, content)
