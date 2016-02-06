def _generate_unique_filename(html_obj):

    import constants

    if html_obj.url.path == '':
        html_obj.url.path.join(constants.URL_SEPARATOR_IN_URL)
    sentized_url_path = html_obj.url.path.replace(
            constants.URL_SEPARATOR_IN_URL,
            constants.URL_SEPARATOR_IN_FILE_NAME
    )
    return ''.join(
            [
                html_obj.url.hostname,
                constants.URL_HOSTNAME_SEPARATOR_IN_FILE_NAME,
                sentized_url_path,
                constants.FILE_NAME_SUFFIX
            ]
    )

def _mkdir_if_not_exists(directory):
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)

def _filter_url_path_components(html_obj):
    filter_non_empty_components = lambda component: component != ''
    url_path_components = filter(filter_non_empty_components, html_obj.url.path.split('/'))
    return url_path_components

def _write_html_to_file(filename, content):

    import constants

    with open(filename, content) as f:
        f.writelines(content.encode(constants.FILE_CONTENT_ENCODING))

def write_to_file(html_obj):

    import os
    import settings
    import constants

    html_files_hostname_root = os.path.join(settings.HTML_FILES_ROOT, html_obj.url.hostname)

    _mkdir_if_not_exists(settings.HTML_FILES_ROOT)
    _mkdir_if_not_exists(html_files_hostname_root)

    url_path_componets = _filter_url_path_components(html_obj)

    if len(url_path_componets) == 0:
        html_file_name = ''.join(['root', constants.FILE_NAME_SUFFIX])

    elif len(url_path_componets) == 1:
        html_file_name = ''.join([url_path_componets.pop(), constants.FILE_NAME_SUFFIX])

    else:
        html_file_name = ''.join([url_path_componets.pop(), constants.FILE_NAME_SUFFIX])
        html_files_endpoint_rec_dir = '/'.join(url_path_componets)
        _mkdir_if_not_exists(html_files_endpoint_rec_dir)

    abs_html_file = os.path.join(html_files_hostname_root, html_file_name)
    _write_html_to_file(filename=abs_html_file, content=constants.FILE_OPEN_MODE_WRITE_PLUS)