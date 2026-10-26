import sys
import cifraSimetrico as sim
import cifraAsimetrico as asim

def ejecutar_demostracion_simetrica():
    print("=" * 50)
    print("DEMOSTRACIÓN DE CIFRADO SIMÉTRICO (FERNET)")
    print("=" * 50)
    mensaje = input("Ingrese la cadena de texto a cifrar: ")
    if not mensaje.strip():
        print("[!] Error: Cadena vacía.")
        return
    clave = sim.generar_clave_simetrica()
    criptograma = sim.cifrar_texto_simetrico(mensaje, clave)
    texto_recuperado = sim.descifrar_texto_simetrico(criptograma, clave)
    print(f"Texto Original: {mensaje}")
    print(f"Texto Cifrado (Hex): {criptograma.hex()}")
    print(f"Texto Descifrado: {texto_recuperado}")

def ejecutar_demostracion_asimetrica():
    print("=" * 50)
    print("DEMOSTRACIÓN DE CIFRADO ASIMÉTRICO (RSA)")
    print("=" * 50)
    mensaje = input("Ingrese la cadena de texto a cifrar: ")
    if not mensaje.strip():
        print("[!] Error: Cadena vacía.")
        return
    print("Generando claves RSA...")
    privada, publica = asim.generar_par_claves_rsa()
    criptograma = asim.cifrar_texto_asimetrico(mensaje, publica)
    texto_recuperado = asim.descifrar_texto_asimetrico(criptograma, privada)
    print(f"Texto Original: {mensaje}")
    print(f"Texto Cifrado (Hex): {criptograma.hex()}")
    print(f"Texto Descifrado: {texto_recuperado}")

def mostrar_menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Cifrado Simétrico")
        print("2. Cifrado Asimétrico")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            ejecutar_demostracion_simetrica()
        elif opcion == "2":
            ejecutar_demostracion_asimetrica()
        elif opcion == "3":
            sys.exit(0)
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    mostrar_menu()