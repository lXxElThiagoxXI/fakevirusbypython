import tkinter as tk
from tkinter import messagebox

def fake_decrypt():
    messagebox.showinfo("Fake Virus Hub", "¡Archivos desbloqueados! Era solo una broma. XD")
    root.destroy()

root = tk.Tk()
root.title("⚠️ WARNING - Fake Ransomware Simulation")
root.geometry("450x250")
root.configure(bg="#121212")
root.resizable(False, False)

# Etiqueta de advertencia
lbl_title = tk.Label(root, text="🔒 ¡TUS ARCHIVOS HAN SIDO ENCRIPTADOS!", fg="#ff0055", bg="#121212", font=("Consolas", 12, "bold"))
lbl_title.pack(pady=15)

lbl_desc = tk.Label(root, text="Se ha detectado la simulación Fake Virus Hub.\nIngresa la clave de desbloqueo o presiona el botón.", fg="#ffffff", bg="#121212", font=("Consolas", 9))
lbl_desc.pack(pady=10)

# Botón de rescate
btn_pay = tk.Button(root, text="Desbloquear Sistema", bg="#00ff66", fg="#000000", font=("Consolas", 10, "bold"), command=fake_decrypt)
btn_pay.pack(pady=20)

root.mainloop()