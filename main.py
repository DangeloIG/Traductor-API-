
from ui import TraductorApp
import tkinter as tk

def main():
    # URL de la API
    api_url = 'https://magicloops.dev/api/loop/7eeeddb1-64e3-4a2b-9ae3-b22dc3002d3a/run'

    # Crear la ventana principal
    root = tk.Tk()
    
    # Crear la aplicación
    app = TraductorApp(root, api_url)

    # Ejecutar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
