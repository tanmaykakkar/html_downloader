from HTMLParser import HTMLParser
import logging
import constants

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag != constants.HTML_TAG_A:
            return

        attrs = dict(attrs)
        url_path = attrs[constants.HTML_TAG_A_ATTR_HREF]

        from html import Html
        from url import InvalidUrlError
        try:
            html = Html.from_url_string(url_string=url_path)

        except InvalidUrlError as e:
            pass

        else:
            import db
            try:
                db.add(html)

            except db.NotUniqueError as e:
                pass