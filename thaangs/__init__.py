import re
import json

from joblib import Parallel, delayed

from thaangs.settings import RSS_FEEDS, FEED_WORKERS
from thaangs.feeds import RSS, Homepage
from thaangs.core import db
from thaangs import html 


def fetch_all(n_jobs=FEED_WORKERS):
  """
  Fetch all listicles from all feeds.
  """

  # build up list of all html + rss feed sources
  modules = []
  for m_name in dir(html):

    if m_name.startswith('_'):
      continue

    if not re.search(r'^[A-Z]+.*$', m_name):
      continue

    m = getattr(html, m_name, None)
    if not m:
      continue

    if isinstance(m, object) and not issubclass(m, Homepage):
      continue


    modules.append(m())

  for feed in RSS_FEEDS:
    r = RSS(feed)
    modules.append(r)

  for m in modules:
     _fetch_one(m)
  
  # Parallel(n_jobs=n_jobs)(delayed(_fetch_one)(m) for m in modules)


def _fetch_one(m):
  """
  Fetch all listicles from one feed.
  """

  for listicle in m.get_listicles():
    db['listicles'].upsert(listicle, ['url'])
    print json.dumps(listicle)

if __name__ == '__main__':
  fetch_all()