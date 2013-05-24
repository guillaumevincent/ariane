# -*- coding: utf-8 -*-
import codecs
import os
from jinja2 import Environment, FileSystemLoader

__author__ = 'gvincent'
import ConfigParser


class Documentation(object):

    def __init__(self, documentation_file):
        try:
            with open(documentation_file):
                self.resources = []
                self.parse(documentation_file)
                self.is_valid = True
                self.error_message = ''
        except IOError:
            self.status_code = 400
            self.is_valid = False
            self.error_message = "%s file doesn't exist!" % documentation_file

    def parse(self, documentation_file):
        """Parse documentation_file and add dynamically resources and section in self object attribute
        """
        config = ConfigParser.ConfigParser()
        config.readfp(codecs.open(documentation_file, "r", "utf8"))

        for section in config.sections():
            options = {}
            for option in config.options(section):
                options[option] = config.get(section, option)

            if ":" in section:
                options["method"] = section.split(':')[1]
                options["name"] = section.split(':')[0]
                self.resources.append(options)
            else:
                self.__dict__[section] = options

    def generate(self, template, output_file):
        """Generate documentation with jinja2
        """
        template = os.path.normpath(template)
        try:
            with open(template):
                env = Environment()
                env.loader = FileSystemLoader(os.path.dirname(template))
                template = env.get_template(os.path.basename(template))
                rendering = template.render(doc=self.__dict__)
                with open(os.path.normpath(output_file), 'w') as doc:
                    doc.write(rendering.encode('utf-8'))
        except IOError:
            self.status_code = 400
            self.is_valid = False
            self.error_message = "%s template file doesn't exist!" % template
