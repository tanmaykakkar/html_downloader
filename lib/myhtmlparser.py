from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):
    """This class is child class of HTMLParser overrides starttag handler"""

    def handle_starttag(self, tag, attrs):
        """find out <a> tag anf href attribute in that for urls"""
        import constants
        import logging
        if tag != constants.HTML_TAG_A:
            return

        attrs = dict(attrs)
        url_path = attrs[constants.HTML_TAG_A_ATTR_HREF]

        from html import Html
        from url import InvalidUrlError

        try:
            html = Html.from_url_string(url_string=url_path)
        except InvalidUrlError as e:
            logging.debug(e)

        else:
            import db

            try:
                db.add(html)
            except db.NotUniqueError as e:
                logging.debug(e)