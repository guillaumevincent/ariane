import ConfigParser
from jinja2 import Environment, FileSystemLoader

__author__ = 'gvincent'

ARIANE_SECTION = [('api', {}), ('code_status', {})]


class RestAPIDoc(object):
    def __init__(self, documentation_file=None):

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

        try:
            self.extract_resources(description_file)
        except:
            self.is_valid = False
            self.error_message = "problem occurs during parsing"
            raise

    def extract_ariane_sections(self, description_file):
        for section, initial_value in ARIANE_SECTION:
            for item in description_file.items(section):
                self.__dict__[section][item[0]] = item[1]

    def extract_resources(self, description_file):
        self.resources = []
        for section in self.difference_between(self.get_ariane_section(), description_file.sections()):
            r = section.split(':')
            s = dict(name=r[0], type=r[1])
            for item in description_file.items(section):
                s[item[0]] = item[1]
            self.resources.append(s)

    def difference_between(self, list1, list2):
        s = set(list1)
        return [x for x in list2 if x not in s]

    def get_ariane_section(self):
        return [k for k, v in ARIANE_SECTION]

    def print_documentation(self, save_file, template_path, template_name):
        env = Environment()
        env.loader = FileSystemLoader(template_path)
        template = env.get_template(template_name)
        rendering = template.render(dict(resources=self.resources,
                                         api=self.api,
                                         code_status=self.code_status))
        with open(save_file, 'w') as doc:
            doc.write(rendering)