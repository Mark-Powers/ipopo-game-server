from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Requires, Validate, Invalidate, Unbind, Bind, Instantiate

@ComponentFactory(name='simple-servlet-factory')
@Instantiate('simple-servlet')
@Requires("_srv", 'game_service')
@Provides(specifications='pelix.http.servlet')
@Property('_path', 'pelix.http.path', "/tictactoe")
class SimpleServletFactory(object):
  """
  Simple servlet factory
  """
  def __init__(self):
      self._path = None

  def bound_to(self, path, params):
      """
      Servlet bound to a path
      """
      print('Bound to ' + path)
      return True

  def unbound_from(self, path, params):
      """
      Servlet unbound from a path
      """
      print('Unbound from ' + path)
      return None

  def do_GET(self, request, response):
      """
      Handle a GET
      """
      print(self._srv.getBoard(0,0))
      content = """<html>
<head>
<title>Tic Tac Toe</title>
<style>
table {
    border-collapse: collapse;
    border-style: hidden;
    align: center;
    margin: auto auto;
    margin-top; 100px;
}
table td {
    border: 1px solid black;
    font: 20px;
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
          value = self._srv.getBoard(x, y)
          content+= "<td>"+value+"</td>\n"
        content += "</tr>\n"
      content += """
</table>
</body>
</html>"""

#        .format(clt_addr=request.get_client_address(),
#                host=request.get_header('host', 0),
#                keys=request.get_headers().keys())

      response.send_content(200, content)
