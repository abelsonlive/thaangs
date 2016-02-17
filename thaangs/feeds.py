from bs4 import BeautifulSoup
import jsonpath_rw as jsonpath
import feedparser
import urllib

from thaangs import network
from thaangs import utils

# JSONPATH CANDIDATES
URL_CANDIDATE_JSONPATH = [
    'id', 'feedburner_origlink', 'link', 'link[*].href'
]

# applies to feed AND individual entries.
DATE_CANDIDATE_JSONPATH = [
    'updated_parsed', 'published_parse'
]

TITLE_CANDIDATE_JSONPATH = [
    'title', 'title_detail.value'
]


class RSS(object):

  def __init__(self, feed_url):
    self.feed_url = feed_url

  def get_jsonpath(self, obj, path, null=[]):
    """
    from https://pypi.python.org/pypi/jsonpath-rw/1.3.0
    parse a dict with jsonpath:
    usage:
    d = {'a' : [{'a':'b'}]}
    get_jsonpath(d, 'a[0].a')
    ['b']
    """
    jp = jsonpath.parse(path)
    res = [m.value for m in jp.find(obj)]
    if len(res) == 0:
      return null
    return res

  def get_candidates(self, obj, jsonpaths):
      """
      evaluate an object with jsonpaths,
      and get all unique vals / lists
      of values
      """
      candidates = []
      for path in jsonpaths:
        path_candidates = self.get_jsonpath(obj, path)

        if isinstance(path_candidates, list):
          for candidate in path_candidates:
            if candidate:
              candidates.append(candidate)

        elif isinstance(path_candidates, str):
          candidates.append(candidate)

      return utils.uniq(candidates)

  def pick_longest(self, candidates):
      """
      Pick the longest option of all candidates
      """
      if len(candidates) == 0:
        return None
      candidates.sort(key=len)
      return candidates[-1]

  def get_created(self, obj):
      """
      return earliest time of candidates or current time.
      """
      candidates = self.get_candidates(obj, DATE_CANDIDATE_JSONPATH)
      if len(candidates) > 0:
        return utils.struct_time_to_ts(sorted(candidates)[0])
      return utils.now()

  def get_title(self, entry):
      """
      return all candidates, and parse unique
      """
      titles = self.get_candidates(entry, TITLE_CANDIDATE_JSONPATH)
      return self.pick_longest(titles)

  def get_url(self, entry):
      """
      Get the url.
      """
      # get potential candidates
      candidates = self.get_candidates(entry, URL_CANDIDATE_JSONPATH)
      urls = [c for c in candidates if c.startswith('http')]
      u = self.pick_longest(urls)
      return utils.remove_args(u)

  def parse_entry(self, entry):
      """
      Parse an entry in an RSS feed.
      """
      u =  self.get_url(entry)
      return {
          'url': u,
          'headline': self.get_title(entry),
          'created_at': self.get_created(entry)
      }

  def get_entries(self):
      """
      Parse an RSS Feed.
      """
      f = feedparser.parse(self.feed_url)
      for entry in f.entries:
          yield self.parse_entry(entry)

  def get_listicles(self):
      """
      Identify all listicles and their lenghths in an RSS feed
      """
      for entry in self.get_entries():
          list_num = utils.get_listicle_num(entry.get('headline'))
          if list_num:
              entry['num'] = list_num
              yield entry


class Homepage:
  """
  Given a homepage URL, extract entries. This is an abstract class which is inherited from.
  It should return an object like this:

  {
    headline: 10 things on the internet,
    url: http://lists.come/10-things-on-the-internet,
    created_at: 1123456789

  }
  """
  url = None

  def __init__(self, url=None):
    if not url:
      html = network.get(self.url)
    else:
      html = network.get(url)
    if html:
      self.soup = BeautifulSoup(html, "html.parser")
    else:
      self.soup = None
  

  def get_entries(self, soup):
    raise NotImplemented


  def get_listicles(self):
    """
    Get listicles from a homepage.
    """
    if self.soup:
      for entry in self.get_entries(self.soup):
        list_num = utils.get_listicle_num(entry.get('headline'))
        if list_num:
          entry['num'] = list_num
          yield entry


if __name__ == '__main__':
  import json
  items = list(RSS('http://feeds.foxnews.com/foxnews/latest?format=xml').get_entries())
  print json.dumps(items)
