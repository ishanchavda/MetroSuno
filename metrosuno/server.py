import json, sqlite3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT / 'metrosuno.sqlite3'

def db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    c.execute('CREATE TABLE IF NOT EXISTS complaints (id INTEGER PRIMARY KEY, text TEXT NOT NULL, lang TEXT, dept TEXT, urgency TEXT, status TEXT, case_status TEXT, owner TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP)')
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, login TEXT UNIQUE, password TEXT, role TEXT)')
    for login, password, role in [('operator','metro123','operator'),('admin','admin123','admin'),('judge@example.com','pass1234','passenger')]:
        c.execute('INSERT OR IGNORE INTO users(login,password,role) VALUES(?,?,?)',(login,password,role))
    c.commit(); return c

def payload(handler):
    n=int(handler.headers.get('Content-Length','0')); return json.loads(handler.rfile.read(n) or '{}')

class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(ROOT),**kwargs)
    def log_message(self,*args): pass
    def send_json(self, data, code=200):
        raw=json.dumps(data).encode(); self.send_response(code); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(raw))); self.end_headers(); self.wfile.write(raw)
    def do_GET(self):
        if self.path == '/api/complaints':
            with db() as c: self.send_json([dict(x) for x in c.execute('SELECT id,text,lang,dept,urgency,status,case_status,owner,created_at FROM complaints ORDER BY id DESC')])
        else: super().do_GET()
    def do_POST(self):
        if self.path == '/api/login':
            p=payload(self)
            with db() as c: row=c.execute('SELECT login,role FROM users WHERE login=? AND password=?',(p.get('login'),p.get('password'))).fetchone()
            self.send_json(dict(row) if row else {'error':'Invalid credentials'}, 200 if row else 401); return
        if self.path == '/api/complaints':
            p=payload(self)
            with db() as c:
                cur=c.execute('INSERT INTO complaints(text,lang,dept,urgency,status,case_status,owner) VALUES(?,?,?,?,?,?,?)',(p.get('text',''),p.get('lang'),p.get('dept'),p.get('urgency'),p.get('status','Pending sync'),p.get('case_status','Received'),p.get('owner','passenger'))); c.commit(); self.send_json({'id':cur.lastrowid},201)
            return
        self.send_json({'error':'Not found'},404)
    def do_PATCH(self):
        if self.path.startswith('/api/complaints/'):
            cid=self.path.rsplit('/',1)[-1]; p=payload(self)
            with db() as c: c.execute('UPDATE complaints SET case_status=?,status=? WHERE id=?',(p.get('case_status'),p.get('status','Pending sync'),cid)); c.commit()
            self.send_json({'ok':True}); return
        self.send_json({'error':'Not found'},404)

if __name__ == '__main__':
    db().close(); server=ThreadingHTTPServer(('127.0.0.1',8000),Handler); print('MetroSuno web app: http://127.0.0.1:8000')
    try: server.serve_forever()
    except KeyboardInterrupt: pass
    finally: server.server_close()
