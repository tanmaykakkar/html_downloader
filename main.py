def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(description="html_downloader")
    parser.add_argument('url')
    args = parser.parse_args()
    return args

def config_logging(filehandler=False):
    import logging
    import settings

    handlers = [logging.StreamHandler()]
    if filehandler:
        handlers += [logging.FileHandler(settings.LOG_FILE)]

    logging.basicConfig(
            level=settings.LOG_LEVEL,
            format=settings.LOG_FORMAT,
            handlers=handlers
    )

def write_to_file(html_obj):
    import os
    import settings
    html_file_name = ''.join( [html_obj.url.hostname, ' - ', html_obj.url.path, '.html'] )
    if not os.path.exists(settings.HTML_FILES_DIR):
        os.makedirs(settings.HTML_FILES_DIR)

    abs_html_file = os.path.join(settings.HTML_FILES_DIR, html_file_name)
    with open(abs_html_file, 'w') as f:
        f.writelines(html_obj.html)

def main():

    import logging
    config_logging()

    from html import Html
    from myhtmlparser import MyHTMLParser
    import db

    arguments = parse_arguments()
    html = Html.from_url_string(url_string=arguments.url)

    db.html_objs.append(html)

    html_parser = MyHTMLParser()
    html_parser.feed(html.html)

    logging.info( 'Urls count in db: %d' % len(db.html_objs))
    logging.debug('Urls in db are: {0}'.format([obj.url.url for obj in db.html_objs]))

    logging.debug('All hostnames and corr. paths are: {0}'.format([(obj.url.hostname, obj.url.path) for obj in db.html_objs]))

    write_in_files()

if __name__ == '__main__':
    main()