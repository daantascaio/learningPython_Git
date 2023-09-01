from pathlib import Path

PATH_FILE = Path(__file__).parent / 'contextManager_class.txt'
# print(PATH_FILE)

class MyOpen:
    def __init__(self, path_file, modo):
        self.path_file = path_file
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.path_file,self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()

        # raise class_exception(*exception_.args).with_traceback(traceback_)

        # print(class_exception)
        # print(exception_)
        # print(traceback_)
        # exception_.add_note('Minha nota')

        # return True  # Tratei a exceção


with MyOpen('aula149.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
