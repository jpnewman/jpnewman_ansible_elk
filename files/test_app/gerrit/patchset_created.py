
import logging
from logging.config import fileConfig

import os

from .patchset import Patchset
from .patchset_enum import PatchsetKind


class PatchsetCreated(object):
    def __init__(self):
        log_folder = "./logs/gerrit"
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        fileConfig('gerrit/log_configs/patchset_created.ini', disable_existing_loggers=False)
        self.logger = logging.getLogger('gerrit.patchset.created')

    def patchset_created(self, review):
        patchset = Patchset(review, PatchsetKind.REWORK)

        self.logger.info("\n%s", patchset.to_json())
        self.logger.info("\n%s", patchset.to_xml())
        self.logger.info('OK')

        self.logger.error('getaddrinfo: Name or service not known')
        self.logger.info('Posting statistics to http://stats.gerrit.com:80/GerritStatCollector')

        return patchset

    def patchset_updated(self, review):
        patchset = Patchset(review, PatchsetKind.TRIVIAL_REBASE)

        self.logger.info("\n%s", patchset.to_json())
        self.logger.info("\n%s", patchset.to_xml())
        self.logger.info('OK')

        self.logger.error('getaddrinfo: Name or service not known')
        self.logger.info('Posting statistics to http://stats.gerrit.com:80/GerritStatCollector')

        return patchset
