class Usuario:
    email = 'admin@gmail.com'
    password = '123'

    def __init__(self):
        pass

    def login (self, email, password):
        if email == self.email and password == self.password:
            print('Login exitoso')
        else:
            print('Login fallido')

print('LOGIN DE USUARIO')
email = input('Ingrese su email: ')
password = input('Ingrese su password: ')   

usuario = Usuario()
print(usuario.usuario_password)
usuario.login(email, password)

        