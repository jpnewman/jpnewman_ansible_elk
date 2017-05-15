
import logging
from logging.config import fileConfig

import random
import os

from .change import Change


class ChangeMerged(object):
    def __init__(self):
        log_folder = "./logs/gerrit"
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        fileConfig('gerrit/log_configs/change_merged.ini', disable_existing_loggers=False)
        self.logger = logging.getLogger('gerrit.change.merged')

    def change_merged(self, review):
        change = Change(review)

        self.logger.info("\n%s", change.to_json())
        self.logger.info("\n%s", change.to_xml())
        self.logger.info('OK')
