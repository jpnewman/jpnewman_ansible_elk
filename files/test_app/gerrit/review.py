
import random

from .data import AUTHORS
from .data import DOMAINS
from .data import SERVER


class Review(object):
    def __init__(self, project):
        change_id = ''.join(random.choice('0123456789abcdef') for i in range(40))
        change_id = "I{0}".format(change_id)

        change_url_id = "{0:04d}".format(random.randint(11111, 99999))

        self.author = random.choice(AUTHORS)
        domain = random.choice(DOMAINS)
        user = "{0} ({1}@{2})".format(self.author, self.author, domain)

        self.project = project
        self.change_id = change_id
        self.change_url_id = change_url_id
        self.change_url = "{0}{1}".format(SERVER, change_url_id)
        self.user = user
        self.commit = ''.join(random.choice('0123456789abcdef') for i in range(40))
        self.patchset = 1
