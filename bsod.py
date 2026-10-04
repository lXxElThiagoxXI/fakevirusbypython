import os
import time

os.system("cls")
os.system("color 1f")  # Fondo Azul con letras Blancas
os.system("title Windows Diagnostic Tool")

print(":( Se ha producido un problema en su dispositivo y necesita reiniciarse.")
print("   Solo estamos recopilando información sobre el error y después se reiniciará automáticamente.\n")

print("   Código de detención: CRITICAL_PROCESS_DIED")
print("   Lo que falló: fakevirus_hub.sys\n")

for percent in range(0, 101, 5):
    print(f"\r   Progresando: {percent}% completado", end="", flush=True)
    time.sleep(0.15)

print("\n\n   [!] Tranquilo, es solo una simulación interactiva de Fake Virus Hub. ;)")
input("\n   Presiona Enter para cerrar la terminal...")