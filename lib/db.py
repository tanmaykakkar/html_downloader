"""This module is html_object storing db"""

class NotUniqueError(ValueError):
    """Exception as name suggests"""
    pass

_html_objs = list()

def _unique(html_obj):
    url_objs = [h_obj.url for h_obj in _html_objs]
    for obj in url_objs:
        if (html_obj.url.scheme == obj.scheme and html_obj.url.netloc == obj.netloc and html_obj.url.path == obj.path):
            return False
    return True

def add(html_obj):
    """Add new html_obj"""
    if _unique(html_obj):
        _html_objs.append(html_obj)
    else:
        raise NotUniqueError(
                'url: {0} (scheme, netloc and path) corr. to html_obj is failing unique constrain'.format(
                        html_obj.url.url
                )
        )

def get_all_url_strings():
    """Return all urls in string"""
    return [obj.url.url for obj in _html_objs]

def get_all():
    """Return all html objs"""
    return _html_objs