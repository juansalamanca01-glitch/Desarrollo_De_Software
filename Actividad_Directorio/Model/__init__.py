class UserModel:
    def __init__(self):
        # Diccionario simulando usuario
        self.users = {
            "Juan ": "Salamanca",
            "Santiago": "Sanchez"
        }

    def validate_user(self, username, password):
        #Lógica de negocio --- validar credenciales
        return username in self.users and self.users[username] == password

