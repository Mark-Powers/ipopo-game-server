import pelix.framework
from pelix.utilities import use_service
from pelix.ipopo.constants import use_ipopo

import logging

def main():
    framework = pelix.framework.create_framework((
        "pelix.ipopo.core",
        "pelix.shell.core",
        "pelix.shell.console",
        "pelix.shell.ipopo"
    ))
    framework.start()
    context = framework.get_bundle_context()

    # Games here
    context.install_bundle('game_tictactoe', './games/').start()
    # Servlets here
    context.install_bundle('servlet_index').start()
    context.install_bundle('servlet_tictactoe', './games/').start()

    context.install_bundle('pelix.http.basic').start()
    with use_ipopo(context) as ipopo:
        ipopo.instantiate(
            'pelix.http.service.basic.factory', 'http-server',
            {'pelix.http.address': 'localhost',
             'pelix.http.port': 9000})

    framework.wait_for_stop()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
