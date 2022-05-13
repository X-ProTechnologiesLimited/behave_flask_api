from flask import Blueprint, request
import logging
import logging.config

util = Blueprint('util', __name__)
logger = logging.getLogger('util')


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@util.route('/quit', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
