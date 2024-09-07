import ctypes
import pyttsx3
import os
import subprocess
import webbrowser
import smtplib
import time
import tkinter as tk
from tkinter import messagebox, Menu
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def tts(message):
   
    engine.say(message)
    engine.runAndWait()

def bomber():
   
    def send_bombing():
        
        email = email_entry.get()
        password = password_entry.get()
        recipient = recipient_entry.get()
        message = message_text.get("1.0", tk.END).strip()
        repetition = repetition_entry.get()
        interval = interval_entry.get()

        if not (email and password and recipient and message and interval):
            
            bombing_info = "Veuillez remplir tous les champs pour envoyer le bombing au destinataire !"
            
            tts(bombing_info)
            messagebox.showwarning(title="E-Bomber :", message=bombing_info)
            
            return

        try:
            
            repetition = int(repetition)
            interval = int(interval)
        
        except ValueError:
            
            value_info = "Veuillez remplir les champs de répétition et intervalle avec des nombres entiers !"
            tts(value_info)
            messagebox.showerror(title="E-Bomber :", message=value_info)
            
            return

        if not email.endswith("@gmail.com"):
            
            email_info = "Veuillez entrer uniquement une adresse électronique Google !"
            tts(email_info)
            messagebox.showerror(title="E-Bomber :", message=email_info)
            
            return

        try:
           
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)

            for _ in range(repetition):
               
                msg = MIMEMultipart()
                msg["From"] = email
                msg["Subject"] = "Votre adresse électronique vient d'être la cible d'une cyberattaque !"
                msg["To"] = recipient
                msg.attach(MIMEText(message, "plain"))
                
                server.sendmail(email, recipient, msg.as_string())
                time.sleep(interval)

            server.quit()
            send_bombing_info = "Votre bombing vient d'être envoyé !"
            
            tts(send_bombing_info)
            messagebox.showinfo(title="E-Bomber :", message=send_bombing_info)

        except Exception as e:
            
            exception_info = f"Une erreur est survenue lors de l'envoi du bombing ! {e}"
            
            tts(exception_info)
            messagebox.showerror(title="E-Bomber :", message=exception_info)

    def help_request():

        tts("En cas de problème avec le logiciel, veuillez contacter le développeur du logiciel à cette adresse électronique !")
        messagebox.showinfo(title="Contacter le développeur :", message="steven_itec@proton.com")
    
    window = tk.Tk()
    window.title("E-Bomber :")
    window.iconbitmap("bombing.ico")
    window.geometry("990x920")
    window.resizable(False, False)

    menu = Menu(window)
    window.config(menu=menu)
    
    help_menu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Contact", menu=help_menu)
    help_menu.add_command(label="Contacter le développeur par courriel.", command=help_request)

    tk.Label(window, text="Quelle est votre adresse électronique ?", font=("Arial", 12)).pack(pady=10)
    
    email_entry = tk.Entry(window, font=("Arial", 12), width=40)
    email_entry.pack(pady=10)

    tk.Label(window, text="Quel est votre mot de passe d'application ?", font=("Arial", 12)).pack(pady=10)
    
    password_entry = tk.Entry(window, font=("Arial", 12), show="*", width=40)
    password_entry.pack(pady=5)

    tk.Label(window, text="Quelle est l'adresse électronique du destinataire ?", font=("Arial", 12)).pack(pady=10)
    
    recipient_entry = tk.Entry(window, font=("Arial", 12), width=40)
    recipient_entry.pack(pady=5)

    tk.Label(window, text="Quel est votre message ?", font=("Arial", 12)).pack(pady=10)
    
    message_text = tk.Text(window, font=("Arial", 12), height=20, width=100)
    message_text.pack(pady=5)

    tk.Label(window, text="Combien de fois souhaitez-vous envoyer votre message au destinataire ?", font=("Arial", 12)).pack(pady=10)
    
    repetition_entry = tk.Entry(window, font=("Arial", 12), width=10)
    repetition_entry.pack(pady=5)

    tk.Label(window, text="Quel intervalle de temps souhaitez-vous entre chaque envoi de courriel ?", font=("Arial", 12)).pack(pady=10)
    
    interval_entry = tk.Entry(window, font=("Arial", 12), width=10)
    interval_entry.pack(pady=15)

    send_button = tk.Button(window, text="Envoyer !", font=("Arial", 12), command=send_bombing)
    send_button.pack(pady=15)

    window.mainloop()

if __name__ == "__main__":

    ctypes.windll.kernel32.SetConsoleTitleW("E-Bomber :")

    tts("Souhaitez-vous écouter les messages de prévention du logiciel concernant son utilisation à des fins malveillantes ?")

    warning_window = tk.Tk()
    warning_window.title("Messages de prévention :")
    warning_window.iconbitmap("bombing.ico")
    warning_window.geometry("660x150")
    warning_window.resizable(False, False)

    tk.Label(warning_window, text="Souhaitez-vous écouter les messages de prévention concernant l'utilisation du logiciel ?", font=("Arial", 12)).grid(row=0, column=0, columnspan=2, pady=20, padx=20)

    def warning_yes():

        warning_1 = "Ce logiciel ne doit pas être utilisé à des fins malveillantes, le développeur ne pourra être tenu responsable en cas de cyberattaques !"
        warning_2 = "Si telle est votre vocation, vos informations d'identification et celles du serveur SMTP de Google, y compris l'adresse IP, pourraient être utilisées contre vous pour des poursuites pénales !"
        warning_3 = "Selon l'article 222-16 du Code pénal :"
        warning_4 = "Les appels téléphoniques malveillants répétés, les envois répétés de messages malveillants ou les agressions sonores visant à troubler la tranquillité d'autrui sont punis de 1 an d'emprisonnement et de 15 000 euros d'amende !"
        warning_5 = "Lorsqu'ils sont commis par le conjoint, le concubin ou le partenaire lié à la victime par un pacte civil de solidarité, ces faits sont punis de trois ans d'emprisonnement et de 45 000 euros d'amende !"
        warning_6 = "Par mesure de sécurité, veuillez utiliser ce logiciel dans une machine virtuelle avec un VPN afin de maximiser votre sécurité et anonymat !"
       
        tts(warning_1 + warning_2 + warning_3 + warning_4 + warning_5 + warning_6)

        messagebox.showwarning(title="E-Bomber :", message=warning_1)
        messagebox.showwarning(title="E-Bomber :", message=warning_6)

        warning_window.destroy()
        webbrowser.open("https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042193596")

        information_1 = "Pour utiliser ce logiciel, veuillez créer un mot de passe d'application pour votre adresse électronique !"
        information_2 = "Cela permettra au serveur SMTP de Google de vous identifier et d'autoriser l'envoi des courriels au destinataire !"
        
        tts(information_1 + information_2)
        messagebox.showwarning(title="E-Bomber :", message=information_1 + "\n\n" + information_2)

        google = "Si vous ne savez pas ce qu'est un mot de passe d'application, veuillez vous rendre à l'adresse suivante :"
        
        tts(google)
        messagebox.showinfo(title="E-Bomber :", message="https://support.google.com/mail/answer/185833")

        tts("Souhaitez-vous créer un mot de passe d'application pour votre adresse électronique ?")

        password_window = tk.Tk()
        password_window.title("Création de mot de passe d'application :")
        password_window.iconbitmap("bombing.ico")
        password_window.geometry("650x150")
        password_window.resizable(False, False)

        tk.Label(password_window, text="Souhaitez-vous créer un mot de passe d'application pour votre adresse électronique ?", font=("Arial", 12)).grid(row=0, column=0, columnspan=2, pady=20, padx=20)

        def password_yes():

            webbrowser.open("https://myaccount.google.com/apppasswords")
            password_window.destroy()

        def password_no():
           
            password_information = "Si vous avez un mot de passe d'application pour votre adresse électronique, veuillez le saisir dans le champ dédié au mot de passe !"
            tts(password_information)
            
            messagebox.showinfo(title="E-Bomber :", message=password_information)
            password_window.destroy()

        tk.Button(password_window, text="Oui !", command=password_yes, width=10).grid(row=1, column=0, padx=10, pady=20, sticky="e")
        tk.Button(password_window, text="Non !", command=password_no, width=10).grid(row=1, column=1, padx=10, pady=20, sticky="w")

        password_window.mainloop()
        bomber()

    def warning_no():

        warning_window.destroy()
        bomber()

    tk.Button(warning_window, text="Oui !", command=warning_yes, width=10).grid(row=1, column=0, padx=10, pady=20, sticky="e")
    tk.Button(warning_window, text="Non !", command=warning_no, width=10).grid(row=1, column=1, padx=10, pady=20, sticky="w")

    warning_window.mainloop()