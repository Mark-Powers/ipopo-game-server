from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Requires, Validate, Invalidate, Unbind, Bind, Instantiate

@ComponentFactory(name='simple-servlet-factory')
@Instantiate('simple-servlet')
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
      content = """<html>
<head>
<title>Tic Tac Toe</title>
<style>
table {
    border-collapse: collapse;
    border-style: hidden;
}

table td {
    border: 1px solid black;
    font: 20px;
}
</style>
</head>
<body>
<table>
<tr>
    <td>X</td>
    <td>X</td>
    <td> </td>
</tr>
<tr>
    <td>O</td>
    <td> </td>
    <td> </td>
</tr>
<tr>
    <td> </td>
    <td>O</td>
    <td>O</td>
</tr>
</table>
</body>
</html>"""

#        .format(clt_addr=request.get_client_address(),
#                host=request.get_header('host', 0),
#                keys=request.get_headers().keys())

      response.send_content(200, content)
