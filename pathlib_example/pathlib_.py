# We use pathlib to work with paths, folders and files so that one code works on Windows, Linux and Mac

from pathlib import Path

caminho_projeto = Path()
print(f'1 {caminho_projeto}')
print(f'2 {caminho_projeto.absolute()}')

caminho_projeto = Path(__file__)
print(f'3 {caminho_projeto}')

print(f'4 {caminho_projeto.parent}')

# print(f'5 {caminho_projeto.parent.parent}')
# print(f'6 {caminho_projeto.parent.parent.parent}')

criar_caminho = caminho_projeto.parent / 'criar_caminho'
print(f'7 {criar_caminho}')

criar_caminho = caminho_projeto.parent / 'criar_caminho' / 'arquivo.txt'
print(f'8 {criar_caminho}')
print()
print()

print(f'9 {Path.home()}')
print(f"10 {Path.home() / 'Desktop'}")


