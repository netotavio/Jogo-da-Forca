palavra_secreta = ''.upper()    #Insira aqui a palavra a ser adivinhada
palpite = ''
palavra_escondida = ''
vidas = 3

# Desenha a palavra escondida:
for letra in palavra_secreta:
    palavra_escondida += '_'
print(palavra_escondida)
print(f'Vidas: {vidas}')



while True:

    palavra_escondida_cpy = '' 
    palpite = (input('Digite uma letra palpite: ')).upper()

    if palpite in palavra_secreta:

        i = 0

        for letra in palavra_escondida:

            if palpite == palavra_secreta[i]:
                palavra_escondida_cpy += palpite

            elif palavra_escondida[i] != '_':
                palavra_escondida_cpy += palavra_escondida[i]

            else:
                palavra_escondida_cpy += '_'

            i += 1
            

        palavra_escondida = palavra_escondida_cpy
        print(palavra_escondida)
           

    else:
        vidas -= 1
        print('Palpite errado! Você perdeu uma vida!')
        print(f'Vidas: {vidas}')

    
    
    
    # Verifica se o jogador acertou a palavra
    if palavra_escondida == palavra_secreta:
        print('Parabéns! Você adivinhou a palavra!')
        break

    # Verifica se acabaram as vidas
    elif vidas == 0:
        print('Acabaram as vidas! Você perdeu!')
        break

    
