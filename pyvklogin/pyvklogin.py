from __future__ import print_function
import sys
import logging

if sys.version_info[0] < 3:
    from urlparse import parse_qsl
    from urllib2 import urlopen, HTTPCookieProcessor
    from urllib import urlencode
else:
    from urllib.parse import parse_qsl, urlencode
    from urllib.request import urlopen, HTTPCookieProcessor, build_opener

log = logging.getLogger(__name__)


def token_getter_url(**kwargs):
    return "https://oauth.vk.com/authorize?" + urlencode(kwargs)


def parse_token(url_with_token):
    qsl = parse_qsl(url_with_token.split("#", 1)[1])
    token = {}

    for el in qsl:
        token[el[0]] = el[1]

    return token


def get_token_cmd(app_id, api_ver='5.64', scope=0):
    if sys.version[0] < 3:
        from cookielib import CookieJar
    else:
        from http.cookiejar import CookieJar
    redirect_uri = 'https://oauth.vk.com/blank.html'
    op = build_opener()
    op.addheaders.append(('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'))
    op.addheaders.append(('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'))
    op.addheaders.append(('Accept-Language', 'en-US;q=0.5,en;q=0.3'))

    cj = CookieJar()
    op.add_handler(HTTPCookieProcessor(cj))

    r = op.open(token_getter_url(
        client_id=app_id,
        scope=scope,
        redirect_uri=redirect_uri,
        display="wap",
        v=api_ver,
        response_type='token'
    ))
    print(r.read())


def get_token_gui_subprocess(queue, app_id, scope, redirect_uri, api_ver, storage, no_show):
    
    return ret


def get_token_gui(app_id, api_ver='5.64', scope=0, storage=None, no_show=False):
    from multiprocessing import Process, Queue

    redirect_uri = 'https://oauth.vk.com/blank.html'

    queue = Queue()
    proc = Process(target=get_token_gui_subprocess,
                   args=(queue, app_id, scope, redirect_uri, api_ver, storage, no_show))
    proc.start()

    return parse_token(queue.get())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app_id = 4527090
    secret_key = "m0WcIM4xQAMZXJVVpwqU"
    api_versin = "5.95"
    lang = 'ru'
    max_attempts = 10
    timeout = 30.

    print(get_token_gui(app_id=app_id, api_ver=api_versin, storage="""vkstorage"""))
