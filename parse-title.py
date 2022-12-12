import sys
from googletrans import Translator


def repl(s: str) -> str:
    r = {',': '', '?': '', ' ': '-', '~': '', '!': '', '@': '', '#': '',
         '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '_': '-', '=': '', '+': '',
         ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
         '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': '', 'Ї': '',
         'Є': '', '—': ''}
    for key in r:
        s = s.replace(key, r[key])
    return s


translation = Translator().translate(f'{" ".join(sys.argv[1:])}', dest='en')
print(repl(translation.text).lower())
