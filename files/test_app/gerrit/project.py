
import random

from .data import PROJECTS
from .data import BRANCHES


class Project(object):
    def __init__(self):
        self.project = random.choice(PROJECTS)
        self.branch = random.choice(BRANCHES)

    def __str__(self):
        return "Project: {0}\nBranch: {1}".format(self.project, self.branch)
