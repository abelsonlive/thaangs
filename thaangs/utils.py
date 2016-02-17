import re
import hashlib
from urlparse import urlsplit, urlunsplit
from datetime import datetime

import pytz

re_prefix = '(the |here\'s |these )'
re_year = re.compile(r'^.*(18|19|20)[0-9]{2}.*$')
re_num = '(two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fiteen|sixteen|seventeen|eighteen|nineteen|twenty)'
re_listicle = re.compile(r"^{}?([0-9]+)\s.*$".format(re_prefix), flags=re.IGNORECASE)
re_num_listicle = re.compile(r"^{}?{}\s.*$".format(re_prefix, re_num), flags=re.IGNORECASE)
re_top_x_listicle = re.compile(r'.*(top|best|greatest|worst) ([0-9]{1,3}) .*$')
re_top_x_num_listicle = re.compile(r'.*(top|best|greatest|worst) {} .*$'.format(re_num), flags=re.IGNORECASE)
re_intro_listicle = re.compile(r"^[^:]+: ([0-9]+) .*$")
re_intro_num_listicle = re.compile(r"^[^:]+: {} .*$".format(re_num), flags=re.IGNORECASE)
re_photo_listicle = re.compile(r"^.*([0-9]+) (photos|gifs|animations) .*$", flags=re.IGNORECASE)

WORD_TO_NUM = {
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20
}


def get_listicle_num(headline):
    """
    get the number of items in a listicle. return None if it's not a listicle
    """
    if not headline:
        return

    if re_year.search(headline):
        return

    m = re_listicle.search(headline)
    if m: return int(m.group(2))
    
    m = re_num_listicle.search(headline)
    if m: return WORD_TO_NUM.get(m.group(2).lower())
    
    m = re_top_x_listicle.search(headline)
    if m: return int(m.group(2))
    
    m = re_top_x_num_listicle.search(headline)
    if m: return WORD_TO_NUM.get(m.group(2).lower())

    m = re_intro_listicle.search(headline)
    if m: return int(m.group(1))

    m = re_intro_num_listicle.search(headline)
    if m: return WORD_TO_NUM.get(m.group(1).lower())



def now():
    """
    The current timestamp.
    """
    return int(datetime.utcnow().strftime('%s'))


def uniq(seq, idfun=lambda x: x):
    """
    Order-preserving unique function.
    """
    # order preserving
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        if marker in seen:
            continue
        seen[marker] = 1
        result.append(item)
    return result


def remove_args(url, keep_params=(), frags=False):
    """
    Remove all param arguments from a url.
    """
    if not url:
        return None
    parsed = urlsplit(url)
    filtered_query = '&'.join(
        qry_item for qry_item in parsed.query.split('&')
        if qry_item.startswith(keep_params)
    )
    if frags:
        frag = parsed[4:]
    else:
        frag = ('',)

    return urlunsplit(parsed[:3] + (filtered_query,) + frag)


def md5(s):
    """
    make an md5 hash of a string.
    """
    return str(hashlib.md5(s).hexdigest())


def struct_time_to_ts(t, tz=pytz.utc):
    """
    Turn a python structtime object into a unix timestamp.
    """
    return int(datetime(
        year=t.tm_year,
        month=t.tm_mon,
        day=t.tm_mday,
        hour=t.tm_hour,
        minute=t.tm_min,
        second=t.tm_sec,
        tzinfo=tz
    ).strftime('%s'))
