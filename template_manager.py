class TemplateManager():
    def __init__(self, path):
        self.templates_folder = path

    def get_template(self, template_number):
        with open(f"{self.templates_folder}/letter_{template_number}.txt") as template:
            return template.read()
