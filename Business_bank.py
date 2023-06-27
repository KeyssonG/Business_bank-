#Bloco de variaveis 

cadastro = ''
novo_cad = ''
cpf = '123065410'# CPF padrão quando o usuário possui cadastro
senha = '123456' #senha padrão quando o usuário possui cadastro
novo_cpf = ''
nova_senha = ''
nome = ''
menu = ''
saldo = float(0)
perfil = ''
autenticacao = ''
conta = '58740'
valor = ''
transf = ''
conta_destin = ''





while True:
    
    entrada = input('[E]ntrar [S]air: ')
    
    if entrada == 'E' or entrada == 'e':
        print('Entrando no sistema.')
        
    elif entrada == 'S' or entrada == 's': 
        print('Acesso encerrado.')

    while True:
        cadastro = input('Você possui uma conta? sim ou não: ') 
              
        print('-'*50)
              
        if cadastro == 'sim' or cadastro =='Sim':
            nome = input('Digite o seu nome: ')
            novo_cpf = input('Digite o seu CPF: ')
            nova_senha = input('Digite a sua senha: ')
                  
            if novo_cpf == novo_cpf and nova_senha == nova_senha:
                print('Login efetuado com sucesso!')
                
                while True:
                     
                    menu = input('Qual opção deseja acessar? [c]onta [t]ransferência [d]epósito [s]air: ')
                           
                          
                    if menu == 'c':
                        print(f'O saldo da sua conta é R${saldo:.2f}')
                                
                        print('-'*50)
                                
                                
                    if menu == 'd':
                        print('Para realizar um Depósito em sua conta, preencha o formulario: ')
                                    
                        print('-'*50)
                                    
                        print('Gerando boleto...')
                                    
                        print('-'*50)
                                    
                        valor = int(input('Digite o valor que deseja depósitar: '))
                                    
                        print(f'Boleto no valor de R${valor:.2f} gerado, prazo para compensação de até 3 dias úteis.')
                            
                        saldo = saldo + valor
                        
                    if menu == 't':
                        trans = input(f'O seu saldo é de R${saldo}, deseja fazer uma TED, DOC ou PIX? ')
                        if trans == 'TED' or trans == 'ted' or trans == 'Ted':
                           transf = int(input('Digite o valor que deseja transferir: '))
                           conta_destin = input('Digite a conta de destino: ')
                           print(f'{nome} a sua transferencia no valor de R${transf:.2f} para a conta {conta_destin} foi enviada com sucesso.                                            '
                           
                                
                                '\nO saldo deve entrar na conta de destino até as 17h de hoje, caso seja feito após esse horário, o saldo compensará no proximo dia útil.')
                                
                        print('-'*50)    
                                
                        saldo = saldo - transf
                
 
                
                    elif menu == 's':
                        print('Acesso encerrado...')
                        break
                    continue
                
                
                
            else:
                print('Erro ao efetuar o login, tente novamente!')
                continue
            break
                 
              
        elif cadastro == 'não' or cadastro == 'Não':
                  
            novo_cad = input('Deseja criar uma nova conta: sim ou não: ')
                  
            if novo_cad == 'sim' and 'Sim':
                nome = input('Digite o seu nome: ')
                novo_cpf = input('Digite o seu CPF: ')
                nova_senha = input('Digite a sua senha: ')
                      
                     
                print('Cadastro registrado com sucesso!')
                break
                      
    print('-'*50)
                      
                      
    while True:
                          
        print('Faça o Login da sua conta: ')
                          
        novo_cpf = input('Digite o seu CPF: ')
        nova_senha = input('Digite a sua senha: ')
                          
        if novo_cpf == novo_cpf and nova_senha == nova_senha:
            print(f'{nome} Bem vindo a sua conta no Business bankt!')
                
            print('-'*50)
                    
        else:
            print('Erro ao efetuar o login, tente novamente!')
            continue
        break
                
                      
        print('-'*50)
                      
                      
                      
    while True:
                     
        menu = input('Qual opção deseja acessar? [c]onta [t]ransferência [d]epósito [s]air: ')
               
              
        if menu == 'c':
            print(f'O saldo da sua conta é R${saldo:.2f}')
                    
            print('-'*50)
                    
                    
        if menu == 'd':
            print('Para realizar um Depósito em sua conta, preencha o formulario: ')
                        
            print('-'*50)
                        
            print('Gerando boleto...')
                        
            print('-'*50)
                        
            valor = int(input('Digite o valor que deseja depósitar: '))
                        
            print(f'Boleto no valor de R${valor:.2f} gerado, prazo para compensação de até 3 dias úteis.')
                
            saldo = saldo + valor
            
        if menu == 't':
            trans = input(f'O seu saldo é de R${saldo}, deseja fazer uma TED, DOC ou PIX? ')
            if trans == 'TED' or trans == 'ted' or trans == 'Ted':
               transf = int(input('Digite o valor que deseja transferir: '))
               conta_destin = input('Digite a conta de destino: ')
               print(f'{nome} a sua transferencia no valor de R${transf:.2f} para a conta {conta_destin} foi enviada com sucesso.                                            '
               
                    
                    '\nO saldo deve entrar na conta de destino até as 17h de hoje, caso seja feito após esse horário, o saldo compensará no proximo dia útil.')
                    
            print('-'*50)    
                    
            saldo = saldo - transf
                
 
                
        elif menu == 's':
            print('Acesso encerrado...')
            break
        continue