import customtkinter as ctk
from flask import Flask
import webbrowser
import threading
import time


#Configuração da aparência
ctk.set_appearance_mode('dark') #Só como vai ficar o fundo

appe = Flask(__name__)

@appe.route("/")
def homepage():
    return "Vamos se beijar ou nada a ver?"

def iniciarServidor():
    appe.run(debug=False, use_reloader=False)
    
#Criação das funções de funcionalidade 
def validarLogin():
    usuario = campoUsuario.get()
    senha = campoSenha.get()

    if usuario =="pedro" and senha == "1309":
        feedback.configure(text="Senha correta", text_color="green")

        servidor = threading.Thread(target=iniciarServidor, daemon=True)
        servidor.start()

        def abrirSite():
            time.sleep(1)
            webbrowser.open("http://127.0.0.1:5000")

        threading.Thread(target=abrirSite, daemon=True).start()

    else:
        feedback.configure(text="Senha incorreta", text_color="red")
        
#Criação da janela principal
app =  ctk.CTk() #Inicialização
app.title("Sistema de Login") #Texto na parte da aba
app.geometry("300x300") #Tamanho da janela
#Criação dos campos 
#Label
labelUsuario = ctk.CTkLabel(app, text="Usuário") #Criar o texto "usuario"
labelUsuario.pack(pady= 10) #padding do HTML
#Entry
campoUsuario = ctk.CTkEntry(app,placeholder_text="Digite o seu login")
campoUsuario.pack(pady=10)
#Label
labelSenha = ctk.CTkLabel(app, text="Senha")
labelSenha.pack(pady=10)
#Entry
campoSenha = ctk.CTkEntry(app,placeholder_text="Digite a sua senha", show='*')
campoSenha.pack(pady=10)
#Buttom
botao = ctk.CTkButton(app, text="Login", command=validarLogin)
botao.pack(pady=10)

#Feedback
feedback = ctk.CTkLabel(app, text="")
feedback.pack(pady=10)
#Iniciar o loop da aplicação 
app.mainloop()  #Funcionar o código 