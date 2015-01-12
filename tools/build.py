# -*- encoding: utf-8 -*-
import sys
import yaml
from jinja2 import Environment, FileSystemLoader


def build(config_file, template_file, output_file):
    env = Environment(loader=FileSystemLoader('.'))
    with open(config_file, 'r') as f:
        config = yaml.load(f)
    template = env.get_template(template_file)

    with open(output_file, 'w') as f:
        f.write(template.render(config).encode('utf-8'))

    return 0

if __name__ == '__main__':
    sys.exit(build(sys.argv[1], sys.argv[2], sys.argv[3]))
