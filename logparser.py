import os
import shlex
from configuration import Configuration
from traverse import TraverseSource

class LogParser(object):
    def __init__(self):
        config = Configuration()
        self.data = config.getConfDict()
        traverse = TraverseSource(self.data)
        self.log = ()
        self.source = traverse.getSourceTree()
        self.parse()

    def generateLogDicts(self, log_fh):
        current = []
        search_for = self.data['search_for']
        for line in log_fh:
            # Only bother if it matches what we look for
            if search_for in line:
                if current:
                    yield current
                try:
                    # break lines into a list
                    brokenLog = shlex.split(line)
                    # lookup for the correct column
                    secBreak = brokenLog[self.data['data_column']].split(self.data['delimiter'])
                    # since a few lines might not be the entry we ignore those
                    try:
                        # extract the source file and line
                        intSecBreak = shlex.split(secBreak[0])
                        intSecBreakP = \
                        intSecBreak[self.data['sub_data_source_column']]
                    except IndexError:
                        continue
                    current = [intSecBreakP, secBreak[-1]]
                except ValueError:
                    continue
        yield current

    def parse(self):
        with open(self.data['log_file']) as filename:
            self.log = list(self.generateLogDicts(filename))

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
