import os

""" 
 Criando arquivos com Python + Context Manager with
 Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)
 Modos:
 r (leitura), w (escrita), x (para criação)
 a (escreve ao final), b (binário)
 t (modo texto), + (leitura e escrita)
 Context manager - with (abre e fecha)
 Métodos úteis
 write, read (escrever e ler)
 writelines (escrever várias linhas)
 seek (move o cursor)
 readline (ler linha)
 readlines (ler linhas)

 Vamos falar mais sobre o módulo os, mas:
 os.remove ou unlink - apaga o arquivo
 os.rename - troca o nome ou move o arquivo

 Vamos falar mais sobre o módulo json, mas:
 json.dump = Gera um arquivo json
 json.load

 Unicode
 use encoding='utf8' para não ter dor de cabeça com acentos e caractares especiais
"""

caminho_arquivo = 'C:\\Users\\caio.dantas\\Desktop\\learningPython_Git\\'
caminho_arquivo += 'manipulando_arqs.txt'

# arquivo = open(caminho_arquivo, 'w')
# # Aqui eu vou fazer alguma coisa com o arquivo!
# # é extremamente importante sempre fechar o arquivo!
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     print(arquivo.read()) # Observe que como o meu cursor do python parou depois que eu pulei a linha no 'Linha 4\n', eu li um arquivo em "branco"

#     arquivo.seek(0, 0)
#     print(arquivo.read()) # Aqui eu já movimentei meu cursor para o início do arquivo e depois li ele

#     print('\nREADLINES MANEIRA INEFICIENTE')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     ########################################
#     ########################################
    
#     print('\nREADLINES MANEIRA EFICIENTE')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())


with open(caminho_arquivo, 'a+', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )


# Executando esses códigos, vc apaga o arquivo, os dois fazem a mesma cosia! Eu não executei, por isso o arquivo continua criados
# os.unlink(caminho_arquivo) 
# os.remove(caminho_arquivo)

os.rename('C:\\Users\\caio.dantas\\Desktop\\learningPython_Git\\manipulando_arqs.txt', 'C:\\Users\\caio.dantas\\Desktop\\learningPython_Git\\Modulo_2\\manipulando_arqs.txt')