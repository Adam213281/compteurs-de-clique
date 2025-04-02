import tkinter as tk


def incrementer():
    global compteur
    compteur += 1
    label_compteur.config(text=str(compteur))


root = tk.Tk()
root.title("Compteur de Clics")


compteur = 0


label_compteur = tk.Label(root, text=str(compteur), font=("Arial", 30))
label_compteur.pack(pady=20)


bouton = tk.Button(root, text="Cliquez ici", command=incrementer, font=("Arial", 20))
bouton.pack(pady=20)


root.mainloop()
