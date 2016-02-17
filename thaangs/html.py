import re 
import urllib

from bs4 import BeautifulSoup

from thaangs.feeds import Homepage
from thaangs import utils
from thaangs import network 

class ViralNova(Homepage):

  url = "http://www.viralnova.com/"

  def get_entries(self, soup):

    for div in soup.find_all('div', {'class': 'post-box'}):
      a_tag = div.find('a')
      hed_tag = div.find('h4')
      yield {
        'url': a_tag.attrs.get('href'),
        'headline': hed_tag.text.strip(),
        'created_at': utils.now()
      }


class Distractify(Homepage):

  url = 'http://distractify.com'

  def get_entries(self, soup):
    for a_tag in soup.find_all('a', {'class': 'index-feed__title'}):
      yield {
        'url': self.url + a_tag.attrs.get('href'),
        'headline': a_tag.text.strip(),
        'created_at': utils.now()
      }


class Zergnet(Homepage):

  url = 'http://www.zergnet.com/'
  
  endpoint = "http://www.zergnet.com/ajax/load_results.php"
  pages = 10
  re_c_data = re.compile(r'<!\[CDATA\[(.*?)\]\]>')

  def fetch_entries(self, page):
    url = self.endpoint + "?queryString=" + urllib.quote_plus("#/0/{}/0/0".format(page))
    html = network.get(url)
    parts = html.split('<![CDATA[')
    if not len(parts) > 1:
      return
    html = parts[1].split(']]>')[0]
    return BeautifulSoup(html, 'html.parser')

  def parse_entries(self, soup):
    """
    Parse entries from soup.
    """
    for a_tag in soup.find_all('a', {'class':'box-link'}):
      hed_tag = a_tag.find('strong', {'class':['post-title', 'title-news']})
      yield {
        'url': a_tag.attrs.get('href'),
        'headline': hed_tag.text.strip(),
        'created_at': utils.now()
      }

  def get_entries(self, soup=None):
    """
    Fetch entries.
    """
    for page in range(1, self.pages+1):
      soup = self.fetch_entries(page)
      for entry in self.parse_entries(soup):
        yield entry


# mic sites

class _Mic(Homepage):

  def get_entries(self, soup):
    for a_tag in soup.find_all('a', {'class':'link-article'}):
      yield {
        'url': self.url + a_tag.attrs.get('href'),
        'headline': a_tag.text.strip(),
        'created_at': utils.now()
      }


class NewsMic(_Mic):

  url = 'http://news.mic.com'


class PolicyMic(_Mic):

  url = "http://policy.mic.com"


class WorldMic(_Mic):

  url = "http://world.mic.com"


class IdentitiesMic(_Mic):

  url = "http://identities.mic.com"


class ConnectionsMic(_Mic):

  url = "http://connections.mic.com"


class TechMic(_Mic):

  url = "http://tech.mic.com"


class ScienceMic(_Mic):

  url = "http://science.mic.com"


class ArtsMic(_Mic):

  url = "http://arts.mic.com"


class StyleMic(_Mic):

  url = "http://style.mic.com"


class MusicMic(_Mic):

  url = "http://music.mic.com"


class DailyDot(Homepage):
  
  url = 'http://www.dailydot.com'

  def get_entries(self, soup):
    for a_tag in soup.find_all('a', {'class': 'dd-tile-title'}):
      yield {
        'url': self.url + a_tag.attrs.get('href'),
        'headline': a_tag.text.strip(),
        'created_at': utils.now()
      }


class AllDay(Homepage):

  url = "http://allday.com"

  def get_entries(self, soup=None):
    soup = self.soup
    for div in soup.find_all('div', {'class': ['caption','caption-dark']}):
      a_tag = div.find('a')
      yield {
        'url': self.url + a_tag.attrs.get('href'),
        'headline': a_tag.text.strip().split('\n')[0].strip(),
        'created_at': utils.now()
      }
