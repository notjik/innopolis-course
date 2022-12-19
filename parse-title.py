import datetime
import argparse
from googletrans import Translator


def repl(s: str) -> str:
    r = {'.': ' ', ',': '', '?': '', '~': '', '!': '', '@': '', '#': '',
         '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '_': '-', '=': '', '+': '',
         ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
         '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': '', 'Ї': '',
         'Є': '', '—': '', ' ': '-', '--': '-'}
    for key in r:
        s = s.strip()
        s = s.replace(key, r[key])
    return s


parser = argparse.ArgumentParser(prog='ParseTitle')
parser.add_argument('-T', '--title', nargs='*', type=str, help='name of your topic')
parser.add_argument('-D', '--date', type=str, help='date of your topic',
                    default=datetime.datetime.now().strftime("%d%m%y"))
parser = parser.parse_args()
if parser.title:
    if type(parser.title) == list:
        title = ' '.join(map(lambda x: x.strip(), parser.title))
    else:
        title = parser.title.strip()
    translation = Translator().translate(f'{title}', dest='en')
    print('{}_{}'.format(parser.date, repl(translation.text).lower()))
