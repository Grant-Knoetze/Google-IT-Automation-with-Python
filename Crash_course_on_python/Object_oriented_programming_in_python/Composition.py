class Repository:
    """Create the repository class which
    starts with an empty dictionary of packages.
    ALWAYS INITIALIZE MUTABLE ASSETS IN THE CONSTRUCTOR!"""

    def __init__(self):
        self.packages = {}

    def add_package(self, package):
        self.packages[package.name] = package

    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result

