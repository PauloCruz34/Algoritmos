#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


nome = input("\n Digite seu nome: ")
senha = input("\n Digite uma senha diferente do nome: ")
while nome == senha :
    print("\n Senha invalida ")
    senha = input("\n Digite uma senha diferente do nome: ")    
print("\n Senha válida")




