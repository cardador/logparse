import os

class TraverseSource(object):

    def __init__(self, config):
        self.config = config
        self.source = {}
        self.traverseSource()


    def traverseSource(self):
        for root, firs, files in os.walk(self.config['source_code']):
            for file in files:
                if file.endswith(self.config['source_pattern']):
                    self.source[file] = os.path.join(root, file)


    def getSourceTree(self):
        return self.source
