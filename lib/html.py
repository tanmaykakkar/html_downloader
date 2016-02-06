"""This module is all about html"""


class Html(object):
    """This class is to store html_content and url corr."""
    def __init__(self, html):
        self.html = html
        self.url = None

    def __repr__(self):
        return 'Html(html=%s)' % self.html

    @property
    def html(self):
        return self._html

    @html.setter
    def html(self, _html):
        self._validate(_html=_html)
        self._html = _html

    def _validate(self, _html):
        from HTMLParser import HTMLParser
        HTMLParser().feed(_html)

    @classmethod
    def from_url_obj(cls, url_obj):
        import requests
        url_path = url_obj.url
        response = requests.get(url_path)
        html = response.text

        obj = cls(html)
        obj.url = url_obj

        return obj

    @classmethod
    def from_url_string(cls, url_string):
        from url import Url
        url = Url(url=url_string)

        import requests
        response = requests.get(url_string)
        html = response.text

        obj = cls(html)
        obj.url = url

        return obj
