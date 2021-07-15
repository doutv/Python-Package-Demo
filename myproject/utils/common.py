# common.py
RULE = {}


def prepare_init_data():
    from ruamel.yaml import YAML
    try:
        import importlib.resources as pkg_resources
    except ImportError:
        # Try backported to PY<37 `importlib_resources`.
        import importlib_resources as pkg_resources
    from myproject import data
    yaml = YAML()
    filename = "data.yaml"
    in_data = pkg_resources.read_text(data, filename)
    global RULE
    RULE = yaml.load(in_data)


def parse_data_by_rule(data):
    global RULE
    return RULE.get(data)


def get_rule():
    global RULE
    return RULE
