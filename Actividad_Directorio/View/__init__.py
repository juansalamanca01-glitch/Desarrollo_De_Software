# View.py
import tkinter as tk
from tkinter import messagebox
from Controller import UserController

class LoginView:
    def __init__(self):
        self.controller = UserController()

        # Ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Login App")
        self.ventana.geometry("500x350")
        self.ventana.config(bg="#eaeaea")  # gris claro neutral

        # Centrar ventana en la pantalla
        ancho = 500
        alto = 350
        x = (self.ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (alto // 2)
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

        # Marco central con contraste
        frame = tk.Frame(self.ventana, bg="#f9f9f9", padx=30, pady=30, relief="groove", bd=3)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        titulo = tk.Label(frame, text="Iniciar Sesión",
                          font=("Segoe UI", 20, "bold"),
                          bg="#f9f9f9", fg="#2c3e50")
        titulo.pack(pady=20)

        # Campo usuario
        self.entry_usuario = tk.Entry(frame, font=("Segoe UI", 14), width=28,
                                      fg="#2c3e50", relief="solid", bd=1)
        self.entry_usuario.insert(0, "")
        self.entry_usuario.pack(pady=10, ipady=5)

        # Campo contraseña
        self.entry_contrasena = tk.Entry(frame, font=("Segoe UI", 14), width=28,
                                         fg="#2c3e50", relief="solid", bd=1, show="*")
        self.entry_contrasena.pack(pady=10, ipady=5)

        # Botón login
        btn_login = tk.Button(frame, text="Entrar", font=("Segoe UI", 14, "bold"),
                              bg="#5a8ca5", fg="white", activebackground="#3d6d83",
                              width=20, height=2, command=self.login)
        btn_login.pack(pady=20)

        self.ventana.mainloop()

    def login(self):
        user = self.entry_usuario.get()
        pwd = self.entry_contrasena.get()
        result = self.controller.login(user, pwd)

        if "Bienvenido" in result:
            messagebox.showinfo("Acceso permitido", result)
        else:
            messagebox.showerror("Acceso denegado", result)
