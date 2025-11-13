u=input("Usuário:")
s=int(input("Digite sua senha:"))
if u=="admin":
    if s==1234:
        print("login realizado com sucesso!")
if u!="admin":
    if s==1234:
        print("Usuário incorreto")
if u=="admin":
    if s!=1234: 
        print("Senha incorreta")
if u!="admin":
    if s!=1234:
        print("Usuário e senhas estão incorretas")