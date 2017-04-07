import ConfigParser, os

class Configuration(object):

    def __init__(self):
        self.data = {}
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open('./logparser.cfg'))
        self.fieldsString = {'Parser':[
                'search_for',
                'log_file',
                'source_pattern',
                'delimiter',
                'source_code'
                ]}
        self.fieldsInt = {'Parser':[
                'sub_data_source_column',
                'data_column',
                ]}
        self.load()

    def load(self):
        for field in self.fieldsString['Parser']: 
            self.data[field] = self.config.get('Parser', field)
        for field in self.fieldsInt['Parser']: 
            self.data[field] = self.config.getint('Parser', field)


    def getConfDict(self):
        return self.data
