import os
from pdf2docx import Converter

def renombrar_py_a_txt():
    print("\nBuscando archivos .py para transformar a .txt...")
    archivos_modificados = 0
    # Recorre todos los archivos en la carpeta actual
    for archivo in os.listdir('.'):
        # Evitamos renombrar el propio script si lo estás ejecutando como .py
        if archivo.endswith('.py') and archivo != 'conversor.py':
            nombre_base = os.path.splitext(archivo)[0]
            nuevo_nombre = nombre_base + '.txt'
            os.rename(archivo, nuevo_nombre) # Esto es exactamente lo que hacía el comando 'ren'
            print(f"  [+] Renombrado: {archivo} -> {nuevo_nombre}")
            archivos_modificados += 1
            
    if archivos_modificados == 0:
        print("  [-] No se encontraron archivos .py para convertir.")

def convertir_pdf_a_word():
    print("\n--- Conversor PDF a Word ---")
    pdf_file = input("Escribe el nombre del archivo PDF (ejemplo: mi_documento.pdf): ")
    
    if os.path.exists(pdf_file):
        docx_file = pdf_file.replace('.pdf', '.docx')
        print("Convirtiendo... Esto puede tardar unos segundos.")
        try:
            cv = Converter(pdf_file)
            cv.convert(docx_file)
            cv.close()
            print(f"  [+] ¡Convertido con éxito a {docx_file}!")
        except Exception as e:
            print(f"  [-] Hubo un error al convertir: {e}")
    else:
        print("  [-] Archivo no encontrado. Asegúrate de que esté en la misma carpeta.")

def main():
    while True:
        print("\n===============================")
        print("   SÚPER CONVERSOR DE ARCHIVOS   ")
        print("===============================")
        print("1. Transformar todos los .py a .txt (estilo ren *.py *.txt)")
        print("2. Convertir un .pdf a Word (.docx)")
        print("3. Salir")
        
        opcion = input("\nElige una opción (1/2/3): ")

        if opcion == '1':
            renombrar_py_a_txt()
        elif opcion == '2':
            convertir_pdf_a_word()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()