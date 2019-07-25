# -*- coding:utf8 -*-
'''
@Author: 异尘
@Date: 2019/07/25 16:25:12
@Description: 
'''

# here put the import lib
import argparse
import logging
import pdb
from flask import Flask, request
from flask import jsonify
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from get_topic import get_topic_from_url

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = "My Super Secret Key"
app.config['JSON_AS_ASCII'] = False

@app.route('/api/topic', methods=['GET'])
def get_topic():
    #logging.info(request.headers)
    pdb.set_trace()
    url = request.args.getlist('url')[0]
    keywords = get_topic_from_url(url)
    return jsonify(keywords)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', '-d', action='store_true', help='whether run at debug mode')
    parser.add_argument('--port', '-p', default=8889, help='the server port')

    args = parser.parse_args()

    if args.debug:
        logging.info("In DEBUG mode ...")
        app.run(host='0.0.0.0', port=args.port, debug=True)
    else:
        logging.info("In Tornado mode, listening %s ..." % args.port)
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(args.port)
        IOLoop.instance().start()