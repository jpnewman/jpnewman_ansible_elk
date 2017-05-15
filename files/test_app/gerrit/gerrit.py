
import random

from .project import Project
from .review import Review
from .patchset_created import PatchsetCreated
from .comment_added import CommentAdded
from .change_merged import ChangeMerged


class Gerrit(object):
    def __init__(self):
        self.projects = [Project() for _ in range(100)]
        self.reviews = []

        self.patchset_created_obj = PatchsetCreated()
        self.comment_added_obj = CommentAdded()
        self.merge_change_obj = ChangeMerged()

    def _create_review(self, project):
        review = Review(project)
        self.reviews.append(review)
        return review

    def create_patchset(self):
        project = random.choice(self.projects)
        review = self._create_review(project)

        self.patchset_created_obj.patchset_created(review)

    def update_patchset(self):
        if not self.reviews:
            return

        review = random.choice(self.reviews)
        self.patchset_created_obj.patchset_updated(review)

    def added_comment(self):
        if not self.reviews:
            return

        review = random.choice(self.reviews)
        self.comment_added_obj.comment_added(review)

    def merge_change(self):
        if not self.reviews:
            return

        review = random.choice(self.reviews)
        change = self.merge_change_obj.change_merged(review)
        self.reviews.remove(review)
