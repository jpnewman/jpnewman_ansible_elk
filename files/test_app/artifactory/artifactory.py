
from .nuget_package import NugetPackages

class Artifactory(object):
    def __init__(self):
        self.nuget_package_obj = NugetPackages()

    def create_all_packages(self):
        self.nuget_package_obj.create_all()
