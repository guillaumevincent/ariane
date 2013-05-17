__author__ = 'gvincent'
import ConfigParser


class Documentation(object):

    def __init__(self, documentation_file):
        try:
            with open(documentation_file):
                self.parse(documentation_file)
                self.is_valid = True
        except IOError:
            self.status_code = 400
            self.is_valid = False
            self.error_message = "%s file doesn't exist!" % documentation_file

    def parse(self, documentation_file):
        config = ConfigParser.RawConfigParser()
        config.read(documentation_file)
        for section in config.sections():
            options = {}
            for option in config.options(section):
                options[option] = config.get(section, option)

            if ":" in section:
                resource = section.split(':')[0]
                methods = self.__dict__[resource] if resource in self.__dict__ else []
                options["method"] = section.split(':')[1]
                methods.append(options)
                self.__dict__[resource] = methods
            else:
                self.__dict__[section] = options


