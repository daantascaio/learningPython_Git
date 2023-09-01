# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

from pathlib import Path
PATH_FILE = Path(__file__).parent / 'contexlib_contextManager_functions.txt'

@contextmanager
def my_open(path_file, mode):
    try:
        print('ABRINDO FILE')
        file = open(path_file, mode, encoding='utf8')
        yield file
    # except Exception as e:         DEVE SER UTILIZADO O finally ao invés do expect!
    #     print('Ocorreu erro:', e)
    finally:
        print('FECHANDO ARQUIVO')
        file.close()

with my_open(PATH_FILE, 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n', 123)
    file.write('Linha 3\n')
    print('WITH', file)
    

