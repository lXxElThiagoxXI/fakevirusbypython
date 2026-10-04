import os
import random
import time

# Configurar consola Windows en color verde hacker
os.system("color 0a")
os.system("title SYSTEM CORRUPTION DETECTED")

chars = "0101010101010101ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*"
warnings = [
    "[CRITICAL_ERROR] Memory leak detected at 0x004F31",
    "[WARNING] Unauthorized access to System32...",
    "[OVERFLOW] Buffer breach in kernel process",
    "FAKE_VIRUS_HUB: Injecting payload..."
]

print("=== INICIANDO ANÁLISIS DE SISTEMA ===")
time.sleep(1)

try:
    for i in range(1000):
        # Cada cierto tiempo lanza una falsa alerta en rojo
        if i % 40 == 0:
            os.system("color 0c")  # Rojo
            print("\n" + random.choice(warnings) + "\n")
            time.sleep(0.3)
            os.system("color 0a")  # Regresa a Verde
        
        # Generar cadena aleatoria estilo Matrix
        line = "".join(random.choice(chars) for _ in range(75))
        print(line)
        time.sleep(0.01)

except KeyboardInterrupt:
    pass

print("\n\n[+] Broma finalizada. Tu PC está 100% a salvo. XD")
input("Presiona Enter para salir...")