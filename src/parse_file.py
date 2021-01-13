import re

from pycparser import CParser

from src.pre_process import pre_process

RE_CHILD_ARRAY = re.compile(r'(.*)\[(.*)]')
RE_INTERNAL_ATTR = re.compile('__.*__')


def _child_attrs_of(klass):
    """
    Given a Node class, get a set of child attrs.
    Memoized to avoid highly repetitive string manipulation
    """
    non_child_attrs = set(klass.attr_names)
    all_attrs = set([i for i in klass.__slots__ if not RE_INTERNAL_ATTR.match(i)])
    return all_attrs - non_child_attrs


def to_dict(node):
    """ Recursively convert an ast into dict representation. """
    klass = node.__class__

    # Metadata
    result = {'_nodetype': klass.__name__}

    # Local node attributes
    for attr in klass.attr_names:
        result[attr] = getattr(node, attr)

    # Coord object
    if node.coord:
        result['coord'] = str(node.coord)
    else:
        result['coord'] = None

    # Child attributes
    for child_name, child in node.children():
        # Child strings are either simple (e.g. 'value') or arrays (e.g. 'block_items[1]')
        match = RE_CHILD_ARRAY.match(child_name)
        if match:
            array_name, array_index = match.groups()
            array_index = int(array_index)
            # arrays come in order, so we verify and append.
            result[array_name] = result.get(array_name, [])
            if array_index != len(result[array_name]):
                raise RuntimeError('Internal ast error. Array {} out of order. '
                                   'Expected index {}, got {}'.format(
                    array_name, len(result[array_name]), array_index))
            result[array_name].append(to_dict(child))
        else:
            result[child_name] = to_dict(child)

    # Any child attributes that were missing need "None" values in the json.
    for child_attr in _child_attrs_of(klass):
        if child_attr not in result:
            result[child_attr] = None

    return result


def get_ast(filename):
    with open(filename) as f:
        parser = CParser()
        text = f.read()
        text = pre_process(text)
        ast = parser.parse(text, filename)
    return to_dict(ast)
