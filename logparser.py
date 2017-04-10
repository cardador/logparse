import os
import shlex
from configuration import Configuration
from traverse import TraverseSource, TraverseLog

class LogParser(object):
    def __init__(self):
        config = Configuration()
        configDict = config.getConfDict()
        traverseSource = TraverseSource()
        self.traverseLog = TraverseLog()
        self.source = traverseSource.generateSource(configDict)
        self.parse(configDict)

    def parse(self, config):
        with open(config['log_file']) as filename:
            self.log = list(self.traverseLog.generateLog(filename, config))

    def printOut(self):
        self.reportList(self.log)
        self.reportDict(self.source)

    def reportList(self, data):
        for entry in data:
            print entry

    def reportDict(self, data):
        for key, entry in data.items():
            print entry

logParser = LogParser()
logParser.printOut()
