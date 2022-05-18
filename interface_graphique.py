# Auteur : Simon Machielsen
# Encodage : UTF-8

from netmiko import *
from tkinter import *


def lecture_configuration():
    # Cette fonction servira à lire la configuration du routeur (lui demander un show run)
    sshCli = ConnectHandler(
        device_type='cisco_xe',
        host='192.168.56.3',
        port=22,
        username='cisco',
        password='cisco123!')

    output = sshCli.send_command("show running-config")
    print(
        "Voici les paramètres utilsés actuellement par le routeur : \n {} \n".format(
            output))


def modification_parametres():
    # On initialise le client SSH
    sshCli = ConnectHandler(
        device_type='cisco_xe',
        host='192.168.56.3',
        port=22,
        username='cisco',
        password='cisco123!')
    # Cette fonction servira à modifier un des paramètres du routeur
    print("Vous avez choisi de modifier un paramètre du switch. \n Que "
          "souhaitez-vous faire ? : \n"
          "1. Modification du nom du routeur. \n"
          "2. Modification du message du jour. \n"
          "3. Entrer une commande en mode d'exécution privilégié.\n"
          "4. Entrer une commande en mode de configuration global.\n"
          "----------------------------------------------------\n"
          "Attention : Il est demandé d'utiliser le numéro de l'option "
          "sélectionnée.")

    modification_choisie = int(input("Quel est votre choix ? : \n"))
    if modification_choisie == 1:
        newname = input('Comment souhaitez-vous appeler le routeur ?\n')
        sshCli.send_config_set(f'hostname {newname}', )
        print(f"Le nouveau nom d'hôte est : {newname}")
    elif modification_choisie == 2:
        banniere = input(f"Vous allez effectuer un changement de la bannière "
                         f"du message du jour. Que souhaitez-vous dire ? ("
                         f"Attention ! Il n'est pas possible d'utiliser des "
                         f"caractères spéciaux. Veuillez vous limiter aux "
                         f"caractères sans accents.\n\n")
        sshCli.send_config_set(f"banner motd $ {banniere} $")
        input(f"Désormais, le message du jour sera : {banniere}.\nAppuyez "
              f"sur une touche pour sortir de cette modification.\n\n")
    elif modification_choisie == 3:
        commande = input(f"Veuillez entrer la commande souhaitée.\nRappel : "
                         f"le mode d'exécution actuel est PRIVILÉGIÉ.\n\n")
        sshCli.send_command(commande)
        print(f"Modification effectuée ! Consultez la configuration actuelle "
              f"pour vous en assurer.\n")
    elif modification_choisie == 4:
        commande_globale = input(f"Veuillez entrer la commande "
                                 f"souhaitée.\nRappel : le mode d'exécution "
                                 f"actuel est GLOBAL\n\n")
        sshCli.send_config_set(f'{commande_globale}')
        print(f"Modification effectuée ! Consultez la configuration actuelle "
              f"pour vous en assurer.\n")
    else:
        print("Choix non valide ! Retour au menu.\n")
        modification_parametres()
    print("........................\nRetour au menu "
          "principal\n........................\nVeuillez cliquer à nouveau "
          "sur l'un des choix !")


def sauvegarde_parametres():
    # Demande au switch d'effectuer un copy running-config startup-config

    sshCli = ConnectHandler(
        device_type='cisco_xe',
        host='192.168.56.3',
        port=22,
        username='cisco',
        password='cisco123!')

    sshCli.send_command("do wr")
    print("Les paramètres ont bien été sauvegardés.")


def fermeture_programme():
    window.quit()


# Partie graphique

# Création de la fenêtre

window = Tk()

# Informations de l'interface

window.title('Projet DevOps')
window.geometry('960x540')
window.minsize(600, 600)
window.maxsize(1920, 1080)
window.config(background='#9114EE')

# Logo de l'école

width = 600
height = 300
image = PhotoImage(file='logoEAFC.png')
canvas = Canvas(window, width=width, height=height, bg='#9114EE')
canvas.create_image(width / 2, height / 2, image=image)
canvas.pack()

# Message d'introduction à l'utilisateur

label_title = Label(window, text="Bienvenue dans ce programme de gestion "
                                 "d'un switch à distance.\nVous disposez de "
                                 "plusieurs choix :\n "
                                 "------------------------------------------------------------------",
                    font=('Courrier', 20), bg='#9114EE', fg='#FFFFFF')
label_title.pack(side='top')

# Création de la boîte contenant les choix de l'utilisateur

frame = Frame(window, bg='#8213d5', bd=1, relief=SUNKEN)

# Liste des choix

label_firstchoice = Button(frame, text="1. Lecture de la configuration.",
                           font=('Courrier', 12), bg='#9114EE', fg='#FFFFFF',
                           command=lecture_configuration)
label_firstchoice.pack(side='top', fill=X)

label_secondchoice = Button(frame,
                            text="2. Modification d'un paramètre du dispositif réseau.",
                            font=('Courrier', 12), bg='#9114EE', fg='#FFFFFF', command=modification_parametres)
label_secondchoice.pack(side='top', fill=X)

label_thirdchoice = Button(frame, text="3. Sauvegarde des paramètres.",
                           font=('Courrier', 12), bg='#9114EE', fg='#FFFFFF', command=sauvegarde_parametres)
label_thirdchoice.pack(side='top', fill=X)

label_fourthchoice = Button(frame, text="4. Quitter.", font=('Courrier', 12),
                            bg='#9114EE', fg='#FFFFFF',
                            command=fermeture_programme)
label_fourthchoice.pack(side='top', fill=X)

# Ajouter la boîte crée précédemment

frame.pack(expand="YES")

# Affichage de la fenêtre

window.mainloop()
