from Controller import UserController
from View import LoginView


def main():
    controller = UserController()

    print("=== Sistema de Login (MVC en consola) ===")
    username = input("Usuario: ")
    password = input("Contraseña: ")

    result = controller.login(username, password)
    print(result)

if __name__ == "__main__":
    #main()  #por consola
    LoginView()   #ventana grafica


  