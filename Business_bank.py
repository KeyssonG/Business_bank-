conta = 4578
senha = 1234
menu = ' '
conta_saldo = float(100)



conta = int(input('Digite a sua conta: '))
senha = int(input('Digite a sua senha: '))

if conta == 4578 and senha == senha:
    print('Login efetuado com sucesso!')
elif conta == ' ' and senha != senha:
    print('Erro: Tente novamente!')    

print('-'*40)

menu = int(input('Qual opção deseja acessar: Área Pix[1] Fatura[2] Conta[3]: '))

if menu == 3:
    print(f'O seu saldo disponivel é de R${conta_saldo:.2f} reias')
elif menu == 2:
    print('Resumo da fatura:'
          '\n 13 ABR. Oxxo Dumas        R$  6,48'
          '\n 13 ABR. Padaria mercearia R$ 17,00')


print('-'*40)   

retornar = int(input('Deseja retornar ao Menu? Sim[1] Não[2]'))

if retornar == 1:
    menu = int(input('Qual opção deseja acessar: Área Pix[1] Fatura[2] Conta[3]: '))
elif retornar == 2:
    print(f'O seu saldo disponivel é de R${conta_saldo:.2f} reias')    

print('-'*40)

if menu == 2:
    print('Resumo da fatura:'
          '\n 13 ABR. Oxxo Dumas        R$  6,48'
          '\n 13 ABR. Padaria mercearia R$ 17,00')
elif menu == 3:
    print(f'O seu saldo disponivel é de R${conta_saldo:.2f} reias')    