""" Django Basic CRUD Generator """
import codecs
import os
import re

from argumentParser import argument_parser
from create_model_views import create_model_views


def camel_case_to_underscore(name):
    """
    This function camel_case_to_underscores a Camel Case word to a underscore word
    """
    temp = re.sub('(.)([A-Z][a-z]+)', r'/1_/2', name)
    return re.sub('([a-z0-9])([A-Z])', r'/1_/2', temp).lower()


def is_file(file_name):
    """ Simple shortcut to check if file exist  """
    return os.path.isfile(file_name)


def read_file(file_path):
    """ Read the file and return its content """
    file = open(file_path, 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()
    return lines


def prepend_to_file(file_path, content):
    """ Add content to begin of the file  """
    file = open(file_path, 'r+', encoding='utf-8')
    lines = file.readlines()
    file.seek(0)
    file.write(content)
    for line in lines:  # write old content after new
        file.write(line)
    file.close()


def append_to_file(file_path, content):
    """ Add Content to the end of file """
    file = open(file_path, 'a+', encoding='utf-8')
    # lines = file.readlines()
    file.write(content)
    # for line in lines:  # write old content after new
    #    file.write(line)
    file.close()


def is_folder(folder_name):
    """ Simple shortcut to check if folder exist  """
    return os.path.isdir(folder_name)


def create_folder_if_not(folder):
    """ Check if folder exists and create one if not """
    if is_folder(folder):
        print("%s exists" % folder)
    else:
        print("%s created" % folder)
        os.mkdir(folder)


def open_or_create_file(file):
    """ Check if file exists and return it,
    create a new one if not and return the new created one """
    if is_file(file):
        print("%s exists" % file)
        return codecs.open(file, 'a+')
    else:
        print("%s created" % file)
        return codecs.open(file, 'w+')


def parse_line(line):
    """
    Example line format => code = models.CharField(unique=True, max_length=15)
    Return dict
    """
    x = line.partition("=")
    field_name = x[0].strip()
    field_type = x[2].strip()
    field_type = field_type[len('models.'):field_type.find('(')]
    return {
        "field_name": field_name,
        "field_type": field_type
    }


def parse_model(lines, model_name):
    """
    Parse lines and return dict of fields
    """

    # Find line with model(models.Model)
    for i in range(len(lines)):
        line = lines[i]
        x = line.find(f'{model_name}(models.Model')
        if x > 0:
            break

    # Loop over lines with fields
    fields = []
    for i in range(i + 1, len(lines)):
        line = lines[i]
        y = line.find('models.')
        if y > 0:
            fields.append(parse_line(line))
        else:
            break
    return fields


def get_model_fields(file, model_name):
    lines = read_file(file)
    return parse_model(lines, model_name)


def create_model_urls(app_name, model_name):
    """
    Create url.py in current directory
    """
    file = open_or_create_file("urls.py")
    file.write(f'from django.urls import path\n')
    file.write(f'\n')
    file.write(
        f'from .views import {model_name}ListView, {model_name}CreateView, {model_name}UpdateView, {model_name}DeleteView, {model_name}DetailView\n')
    file.write(f'\n')
    file.write(f'app_name = "{app_name}"\n')
    file.write(f'urlpatterns = [\n')
    file.write(f'\tpath("", {model_name}ListView.asView(), name="list"),\n')
    file.write(f'\tpath("create/", {model_name}CreateView.asView(), name="create"),\n')
    file.write(
        f'\tpath("<int:pk>/update/", {model_name}UpdateView.asView(), name="update"),\n')
    file.write(
        f'\tpath("<int:pk>/delete/", {model_name}DeleteView.asView(), name="delete"),\n')
    file.write(
        f'\tpath("<int:pk>/detail/", {model_name}DetailView.asView(), name="detail"),\n')
    file.write(f']\n')
    file.close()
    return


def execute_from_command_line():
    args = argument_parser()
    project_path = '/home/john/PycharmProjects/owb_forms/'
    project_path = 'C:/Users/beesen/PycharmProjects/bhv/'
    app_name = args['app_name']
    model_name = args['model_name']
    # model_name_underscore = camel_case_to_underscore(model_name)
    use_template_layout = args['use_template_layout']
    override_templates = args['override_templates']

    model_path = os.path.join(project_path, app_name, 'models.py')
    model_fields = get_model_fields(model_path, model_name)
    print(model_fields)

    # create views.py
    create_model_views(model_name, model_fields)

    # create urls.py
    create_model_urls(app_name, model_name)

    components = [
        "views",
        "templates",
        # "tests",
        "urls"
    ]

    crud_items = [
        "list",
        "create",
        "detail",
        "update",
        "delete"
    ]

    # Create app folder with given app_name if there is no one
    create_folder_if_not(app_name)


def __main__():
    # python - m django_basic_crud_generator --app_name MY_APP --model_name MY_MODEL
    execute_from_command_line()
