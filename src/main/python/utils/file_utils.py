
import os
import logging
from werkzeug import secure_filename


def get_destination (target, filename):
    return "/".join([target, secure_filename(filename)])

def is_valid_file (filename):
    if not filename:
        return false

    ext = os.path.splitext(filename)[1]
    return (ext == ".txt") or (ext == ".lc")


# upload_file_to_server: Upload a data file to the Flask server path
#
# @param: file: file to upload
# @param: target: folder name for upload destination
#
def save_file (file, target):

    logging.debug("file: %s - %s" % (type(file), file))

    if not os.path.isdir(target):
        os.mkdir(target)

    destination = get_destination(target, file.filename)
    file.save(destination)

    return destination
