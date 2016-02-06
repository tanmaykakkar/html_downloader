def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(description="html_downloader")
    parser.add_argument('url')
    args = parser.parse_args()
    return args

def main():

    import logging
    import settings

    if settings.DEBUG:
        import helper
        helper.config_logging()

    from html import Html
    from myhtmlparser import MyHTMLParser
    from file import write_to_file
    import db

    arguments = parse_arguments()
    html = Html.from_url_string(url_string=arguments.url)

    db.add(html)

    html_parser = MyHTMLParser()
    html_parser.feed(html.html)

    urls_in_db = db.get_all_url_strings()

    logging.debug( 'Url count in db: %d' % len(urls_in_db))
    logging.debug('Urls in db are: {0}'.format(urls_in_db))

    [write_to_file(html_obj=obj) for obj in db.get_all()]

if __name__ == '__main__':
    main()