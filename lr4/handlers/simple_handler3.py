from cleanapi.server import BaseHandler
import json
import requests
import tornado
url_tail = '/area_triangle'

class Handler(tornado.web.RequestHandler):
    # SQR triangle with base and height
    def post(self):
        # Receive first argument
        a = self.get_argument('a', 'No data received')
        # Receive second argument
        h = self.get_argument('h', 'No data received')
     
        s = str((1/2)*int(a)*int(h))

        self.write({'success': 'EVERIKA! '})
        self.write({'version': 'v.2'})
        self.write({'result': s})