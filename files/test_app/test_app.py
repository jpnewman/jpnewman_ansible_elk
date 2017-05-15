#!/usr/bin/env python3

from gerrit.gerrit import Gerrit
from artifactory.artifactory import Artifactory

def main():
    gerrit_log = Gerrit()
    for _ in range(0, 5):
        gerrit_log.create_patchset()
        gerrit_log.update_patchset()
        gerrit_log.added_comment()
        gerrit_log.merge_change()

    artifactory_logs = Artifactory()
    artifactory_logs.create_all_packages()


if __name__ == '__main__':
    main()
