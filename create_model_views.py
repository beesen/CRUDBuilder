from django_basic_crud_generator import open_or_create_file


def write_header(file):
    file.write(
        f'from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView\n')
    file.write(f'\n')
    file.write(f'\n')


def write_list_view(file, model_name):
    file.write(f'class {model_name}ListView(ListView):\n')
    file.write(f'\tmodel = {model_name}\n')
    file.write(f'\tfields = "__all__"\n')
    file.write(f'\n')
    file.write(f'\n')
    return


def write_create_view(file, model_name):
    file.write(f'class {model_name}CreateView(UpdateView):\n')
    file.write(f'\tmodel = {model_name}\n')
    file.write(f'\tfields = "__all__"\n')
    file.write(f'\n')
    file.write(f'\n')
    return


def write_update_view(file, model_name):
    file.write(f'class {model_name}UpdateView(UpdateView):\n')
    file.write(f'\tmodel = {model_name}\n')
    file.write(f'\tfields = "__all__"\n')
    file.write(f'\n')
    file.write(f'\n')
    return


def write_delete_view(file, model_name):
    file.write(f'class {model_name}DeleteView(DeleteView):\n')
    file.write(f'\tmodel = {model_name}\n')
    file.write(f'\tfields = "__all__"\n')
    file.write(f'\n')
    file.write(f'\n')
    return


def write_detail_view(file, model_name):
    file.write(f'class {model_name}DetailView(DetailView):\n')
    file.write(f'\tmodel = {model_name}\n')
    file.write(f'\tfields = "__all__"\n')
    file.write(f'\n')
    file.write(f'\n')
    return


def create_model_views(model_name, model_fields):
    """
    Create views.py in current directory
    """
    file = open_or_create_file("views.py")
    write_header(file)
    write_list_view(file, model_name)
    write_create_view(file, model_name)
    write_update_view(file, model_name)
    write_delete_view(file, model_name)
    write_detail_view(file, model_name)
    file.close()
    return
