from Model import UserModel

class UserController:
    def __init__(self):
        self.model = UserModel()

    def login(self, username, password):
        #Llama al modelo para validar credenciales
        if self.model.validate_user(username, password):
            return f"Bienvenido, {username}!"
        else:
            return "Usuario o contraseña incorrectos"
