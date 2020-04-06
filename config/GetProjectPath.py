import os


def get_project_path():

    path = os.path.split(os.path.realpath(__file__))[0]
    project_path = os.path.abspath(os.path.join(path, '..'))
    return project_path
