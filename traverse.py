import os
import shlex

class TraverseSource(object):

    def generateSource(self, config):
        source = {}
        for root, firs, files in os.walk(config['source_code']):
            for file in files:
                if file.endswith(config['source_pattern']):
                    source[file] = os.path.join(root, file)
        return source

class TraverseLog(object):

    def generateLog(self, log_fh, config):
        current = []
        search_for = config['search_for']
        for line in log_fh:
            # Only bother if it matches what we look for
            if search_for in line:
                if current:
                    yield current
                try:
                    # break lines into a list
                    brokenLog = shlex.split(line)
                    # lookup for the correct column
                    secBreak = brokenLog[config['data_column']].split(config['delimiter'])
                    # since a few lines might not be the entry we ignore those
                    try:
                        # extract the source file and line
                        intSecBreak = shlex.split(secBreak[0])
                        intSecBreakP = intSecBreak[config['sub_data_source_column']]
                    except IndexError:
                        continue
                    current = [intSecBreakP, secBreak[-1]]
                except ValueError:
                    continue
        yield current

