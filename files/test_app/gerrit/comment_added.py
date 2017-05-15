
import logging
from logging.config import fileConfig

import os

from .comment import Comment


class CommentAdded(object):
    def __init__(self):
        log_folder = "./logs/gerrit"
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        fileConfig('gerrit/log_configs/comment_added.ini', disable_existing_loggers=False)
        self.logger = logging.getLogger('gerrit.comment.added')

    def comment_added(self, review):
        comment = Comment(review)

        self.logger.info("\n%s", comment.to_json())
        self.logger.info("\n%s", comment.to_xml())
        self.logger.info('OK')

        self.logger.error('getaddrinfo: Name or service not known')
        self.logger.info('Posting statistics to http://stats.gerrit.com:80/GerritStatCollector')
