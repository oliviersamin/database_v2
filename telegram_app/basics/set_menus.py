import os
from dotenv import load_dotenv
load_dotenv()


class Item:
    def __init__(self, parent, name, type):
        self.parent = parent
        self.type = type
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def get_model_details(FILE_PATH) -> list:
    """
    get models and attributes of all api modules
    :param self:
    :return:
    """
    with open(FILE_PATH, 'r') as file:
        data = file.readline()
    data = data.split('|')
    results = [item.split(',') for item in data]
    final = []
    for item in results:
        final.append({'module': item[0][item[0].find(':') + 2:], 'model': item[1][item[1].find(':') + 2:],
                      'attributes': item[2][item[2].find(':') + 2:]})
    return final


def create_items(data):
    modules = []
    items = []
    for index, item in enumerate(data):
        if index ==0:
            modules.append([item])
        else:
            if item.get('module') == modules[-1][-1].get('module'):
                modules[-1].append(item)
            else:
                modules.append([item])
    for module in modules:  # create module items
        for index, object in enumerate(module):
            if index == 0:
                print(object)
                items.append(Item(parent='', name=object.get('module'), type='module'))
                print(items[-1])
                items[-1].add_child(object.get('model'))
            else:
                items[-1].add_child(object.get('model'))
    for item in data:  # create models items
        items.append(Item(parent=item.get('module'), name=item.get('model'), type='model'))
        items[-1].children = item.get('attributes').split(';')
    print(items[-1].__dict__)

    return items


def set_menus():
    FILE_PATH = os.environ.get('ATTRIBUTES_FILE_PATH')
    DATA = get_model_details(FILE_PATH)
    items = create_items(DATA)
    return items


if __name__ == '__main__':
    set_menus()