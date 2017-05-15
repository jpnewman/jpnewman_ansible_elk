
import datetime
import random

from collections import OrderedDict
from .patchset_enum import PatchsetKind

from . import utils


class Patchset(object):
    def __init__(self, review, patchset_kind):
        change_id = review.change_id
        if patchset_kind == PatchsetKind.TRIVIAL_REBASE:
            change_id = utils.change_joined_id(review.project.project,
                                               review.project.branch,
                                               review.change_id)
            review.patchset += 1

        self.review = review

        self.patchset = OrderedDict()
        self.patchset['change'] = change_id
        self.patchset['is-draft'] = random.choice([True, False])
        self.patchset['kind'] = patchset_kind
        self.patchset['change-url'] = review.change_url
        self.patchset['change-owner'] = review.user
        self.patchset['project'] = review.project.project
        self.patchset['branch'] = review.project.branch

        if patchset_kind == PatchsetKind.TRIVIAL_REBASE:
            self.patchset['topic'] = 'nil'

        self.patchset['uploader'] = review.user
        self.patchset['commit'] = review.commit
        self.patchset['patchset'] = review.patchset

    def to_json(self):
        return utils.to_json(self.patchset.items())

    def to_xml(self):
        event = OrderedDict()
        event['ChangeId'] = self.patchset['change']
        event['Patchset'] = self.patchset['patchset']
        event['Repo'] = self.patchset['project']
        event['Branch'] = self.patchset['branch']
        event['EventType'] = 'patchset'
        event['EventTime'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        event['Author'] = self.review.author

        return utils.to_xml(event, 'GerritEvent')
