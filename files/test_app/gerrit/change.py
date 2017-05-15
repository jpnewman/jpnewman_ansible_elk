
import datetime
import random

from collections import OrderedDict

from . import utils


class Change(object):
    def __init__(self, review):
        self.review = review

        self.change = OrderedDict()
        self.change['change'] = utils.change_joined_id(review.project.project,
                                                       review.project.branch,
                                                       review.change_id)
        self.change['change-url'] = review.change_url
        self.change['change-owner'] = review.user
        self.change['project'] = review.project.project
        self.change['branch'] = review.project.branch
        self.change['topic'] = 'nil'
        self.change['submitter'] = review.user
        self.change['commit'] = review.commit
        self.change['newrev'] = ''.join(random.choice('0123456789abcdef') for i in range(40))

    def to_json(self):
        return utils.to_json(self.change.items())

    def to_xml(self):
        event = OrderedDict()
        event['ChangeId'] = self.change['change']
        event['Repo'] = self.change['project']
        event['Branch'] = self.change['branch']
        event['EventType'] = 'merged'
        event['EventTime'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        event['Author'] = self.review.author

        return utils.to_xml(event, 'GerritEvent')
