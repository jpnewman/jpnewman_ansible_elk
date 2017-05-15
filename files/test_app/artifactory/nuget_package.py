
from .data import NUGET_PACKAGES


class NugetPackages(object):
    def __init__(self):
        self.packages = []

    def create_all(self):
        for key, val in NUGET_PACKAGES.items():
            for version in val['versions']:
                self.packages.append("{0}.{1}.nupkg".format(key, version))
