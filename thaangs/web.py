import json

from thaangs.core import app, db

@app.route('/')
def index():
  results = db.query('select num, count(1) as count from listicles group by num order by count desc ')
  return json.dumps(list(results))

@app.route('/<int:num>')
def num(num):
  results = db.query('select * from listicles where num = {} order by created_at desc'.format(num))
  return json.dumps(list(results))

if __name__ == '__main__':
  app.run(debug=True)
