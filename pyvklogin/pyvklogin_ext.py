from __future__ import print_function
import sys
import logging

log = logging.getLogger(__name__)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage

app = QApplication([])
browser = QWebEngineView()

if storage is not None:
    profile = QWebEngineProfile(storage, browser)
    webpage = QWebEnginePage(profile, browser)
    browser.setPage(webpage)

def url_listener(url):
    url_s = url.toString()
    log.info(url_s)
    if url_s.startswith(redirect_uri):
        queue.put(url.toString())
        browser.close()

browser.urlChanged.connect(url_listener)

browser.load(QUrl(token_getter_url(
    client_id=app_id,
    scope=scope,
    redirect_uri=redirect_uri,
    display="mobile",
    v=api_ver,
    response_type='token'
)))
if not no_show:
    browser.show()
ret = app.exec_()