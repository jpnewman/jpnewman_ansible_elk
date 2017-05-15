
import datetime

from collections import OrderedDict

from . import utils


class Comment(object):
    def __init__(self, review):
        self.review = review

        self.comment = OrderedDict()
        self.comment['change'] = review.change_id
        self.comment['is-draft'] = False
        self.comment['change-url'] = review.change_url
        self.comment['change-owner'] = review.user
        self.comment['project'] = review.project.project
        self.comment['branch'] = review.project.branch
        self.comment['author'] = review.author
        self.comment['commit'] = review.commit
        self.comment['comment'] = "Patch Set 1: Code-Review+1 Verified+1"
        self.comment['code-review'] = 1
        self.comment['verified'] = 1

    def to_json(self):
        return utils.to_json(self.comment.items())

    def to_xml(self):
        event = OrderedDict()
        event['ChangeId'] = self.comment['change']
        event['Repo'] = self.comment['project']
        event['Branch'] = self.comment['branch']
        event['EventType'] = 'comment'
        event['Patchset'] = self.review.patchset
        event['EventData'] = 'Code-Review+1'
        event['EventTime'] = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        event['Author'] = self.comment['author']

        return utils.to_xml(event, 'GerritEvent')
