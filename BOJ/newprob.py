from os import mkdir, getcwd, chdir
from os.path import exists, isdir, isfile, basename
from argparse import ArgumentParser, Namespace


# Make help command
parser = ArgumentParser()
parser.add_argument('number', type=int, help='The number to start')


if __name__ == '__main__':
    args: Namespace = parser.parse_args()

    no: int = args.number

    if basename(getcwd()) != 'BOJ' and exists('BOJ') and isdir('BOJ'):
        chdir('BOJ')

    if exists(str(no)):
        parser.exit(-1, 'ERROR: File or Directory `{}` already exists'.format(no))
        exit(-1)

    mkdir(str(no))
    open('{0}/{0}.py'.format(no), 'w', encoding='UTF-8').write('')
    open('{0}/README.md'.format(no), 'w', encoding='UTF-8').write('')
    parser.exit(0, 'SUCCESS: Created Directory `{}`'.format(no))
