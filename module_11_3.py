import inspect


def introspection_info(obj):
    '''возвращает словарь содержащий тип, модуль, атрибуты и методы объекта'''
    info = {'type': type(obj).__name__,
            'attributes': [],
            'methods': []}

    for name in dir(obj):
        if callable(getattr(obj, name)):
            info['methods'].append(name)
        else:
            info['attributes'].append(name)

    obj_module = inspect.getmodule(obj)
    if obj_module is None:
        info['module'] = __name__
    else:
        info['module'] = obj_module.__name__

    return info


if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)


