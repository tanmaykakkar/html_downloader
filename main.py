#1/usr/local/env python

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(description="html_downloader")
    parser.add_argument('url')
    args = parser.parse_args()
    return args

# execution starts here
def main():

    import logging
    import settings

    if settings.DEBUG:
        from lib import helper
        helper.config_logging()

    from lib.html import Html
    from lib.myhtmlparser import MyHTMLParser
    from lib.file import write_to_filesystem
    from lib import db

    # fetching cli args
    arguments = parse_arguments()

    # creating Html object
    html = Html.from_url_string(url_string=arguments.url)

    # db is a storage of all html_objs containing url as html_content
    # adding in db, with uniqueness of urls
    db.add(html)

    # html parser to findout urls i.e.- <a href=''>
    html_parser = MyHTMLParser()
    html_parser.feed(html.html)

    # for debugging
    urls_in_db = db.get_all_url_strings()
    logging.debug( 'Url count in db: %d' % len(urls_in_db))
    logging.debug('Urls in db are: {0}'.format(urls_in_db))

    # after fetching, writing to files
    [write_to_filesystem(html_obj=obj) for obj in db.get_all()]

if __name__ == '__main__':
    main()