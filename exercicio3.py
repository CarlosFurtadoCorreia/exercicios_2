'''EXERCÍCIO 3

- Pedir ao utilizador para escrever uma frase com + de 10 caracteres
- Não permitir mais que 2 caracteres seguidos iguais
- Quantas unidades de caracteres de cada contém a frase
- Frase tem que terminar obrigatoriamente com '. ! ?'''

if __name__ == '__main__':
    frase = input('Insira uma frase com + de 10 caracteres. (Deve terminar com ". ! ?"): ')
    ver_char = [frase]
    count_char_iguais = []
    count_frase = 0
    fim = ['.', '!', '?']
    for f in frase:
        count_frase += 1
    print({count_frase})
    if count_frase < 10:
        print('A sua frase tem que ter + de 10 caracteres.')
    else:
        pass
    #for c in range(frase):

    '''if len(frase - 1) != fim:
        pass
    else:
        print('A sua frase deve terminar com ". ! ?"')
    print('passou')'''
