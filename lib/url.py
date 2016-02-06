"""This module is all about url"""


class InvalidUrlError(ValueError):
    """This is exception for invalid urls"""
    pass


class Url(object):
    """This class represent urls and its properties i.e.- scheme, hostname, port etc"""
    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return 'Url(url=%s)' % self.url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, _url):
        self._validate(_url=_url)
        self._url = _url

    def _validate(self, _url):

        from urlparse import urlparse
        parse_result = urlparse(_url)

        is_valid = parse_result.netloc and parse_result.scheme and True or False
        if not is_valid:
            raise InvalidUrlError("URL Invalid: %s" % (_url) )

        # setting all properties after _validating
        self.hostname = parse_result.hostname
        self.path = parse_result.path
        self.scheme = parse_result.scheme
        self.netloc = parse_result.netloc