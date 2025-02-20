class MinhaClasse:
    def __enter__(self):
        print('Entrando...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Saindo...')

with MinhaClasse() as mc:
    print('Executando...')