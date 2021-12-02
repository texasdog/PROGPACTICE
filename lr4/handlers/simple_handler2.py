from cleanapi.server import BaseHandler

url_tail = '/test.json'

class Handler(BaseHandler):
    async def get(self):
        self.set_status(200)
        self.write({'success': 'EVERIKA '})
        self.write({'result': 'IT WORKS!'})
        self.write({'version': 'v.1'})