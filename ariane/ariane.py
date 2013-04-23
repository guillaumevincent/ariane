import ConfigParser

__author__ = 'gvincent'

ARIANE_SECTION = [('api', {}), ('code_status', {})]


class RestAPIDoc(object):
    def __init__(self, documentation_file=None, sections=None):
        if not sections:
            for (section, initial_value) in ARIANE_SECTION:
                        self.__dict__[section] = initial_value

        self.is_valid = False
        try:
            with open(documentation_file) as df:
                self.parse(df)
        except IOError:
            self.error_message = "documentation_file = %s doesn't exist !" % documentation_file

    def is_valid(self):
        return self.is_valid

    def parse(self, documentation_file):

        description_file = ConfigParser.RawConfigParser()

        try:
            description_file.readfp(documentation_file)
            self.extract_ariane_sections(description_file)
            self.is_valid = True
            self.error_message = "ok"
        except ConfigParser.ParsingError:
            self.error_message = "File contains parsing errors: sections_test"
        except ConfigParser.NoSectionError as e:
            self.error_message = e
        except:
            self.error_message = "problem occurs during parsing"
            raise

    def extract_ariane_sections(self, description_file):
        for section, initial_value in ARIANE_SECTION:
            for item in description_file.items(section):
                self.__dict__[section][item[0]] = item[1]
