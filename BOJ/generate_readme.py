from os import mkdir, getcwd, chdir, listdir
from os.path import exists, isdir, isfile, basename, getsize
from urllib.parse import quote
from datetime import datetime, timezone
from argparse import ArgumentParser, Namespace

CODE_EXTENSIONS = {
    'c': 'C',
    'cpp': 'C++',
    'py': 'Python',
    }


# Make help command
parser = ArgumentParser()
parser.add_argument('target', type=str,  nargs='*', default='*', help='Target folder to generate')
parser.add_argument('--override', action='store_true', help='Override exist README files')


def escape(name: str) -> str:
    name = name.replace(' ', '%20')
    return name


def render_template(num: int=1000, title: str=None):
    TEMPLATE = '''# BOJ{prob_num} - {prob_title}

> [View in BOJ](https://www.acmicpc.net/problem/{prob_num})

## Solutions
{solutions}

_Page built: {dtime}_
'''

    codes = [*filter(lambda x: x.split('.')[-1].lower() in CODE_EXTENSIONS.keys(), listdir(str(num)))]

    solution_string = ''
    for code in codes:
        lang = CODE_EXTENSIONS[code.split('.')[-1].lower()]
        solution_string += '- [Solution on {}]({})\n'.format(lang, escape(code))

    return TEMPLATE.format(prob_num=num, prob_title=None, solutions=solution_string,
                           dtime=datetime.utcnow().strftime('%b %d %Y %X (W+%W, UTC)'))


if __name__ == '__main__':
    args: Namespace = parser.parse_args()
    target = args.target
    override = args.override

    if target == '*':
        target = filter(lambda x: x.isnumeric() and isdir(x), listdir('.'))

    for prob in target:
        if not override and exists('{}/README.md'.format(prob)):
            if getsize('{}/README.md'.format(prob)) > 0:
                print('Ignoring `{}` because it is not empty.'.format(prob))
                continue

        open('{}/README.md'.format(prob), 'w', encoding='UTF-8').write(render_template(int(prob)))
