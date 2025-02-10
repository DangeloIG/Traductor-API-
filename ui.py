import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from traductor import TraductorAPI

class TraductorApp:
    def __init__(self, root, api_url):
        self.root = root
        self.root.title("Traductor Profesional")
        self.root.geometry("600x400")
        self.root.config(bg="#f0f0f0")
        self.api = TraductorAPI(api_url)

        self.crear_widgets()

    def crear_widgets(self):
        # Frame principal
        frame = tk.Frame(self.root, bg="#ffffff", padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)

        # Etiquetas
        tk.Label(frame, text="Frase a traducir:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Label(frame, text="Idioma de origen:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Label(frame, text="Idioma de destino:", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Entrada de texto
        self.entrada_texto = tk.Entry(frame, font=("Arial", 12), width=40)
        self.entrada_texto.grid(row=0, column=1, padx=10, pady=10)

        # Combobox para idioma de origen
        self.idioma_origen_combo = ttk.Combobox(frame, values=['es', 'en', 'fr', 'de', 'it'], state="readonly", width=10)
        self.idioma_origen_combo.set('es')
        self.idioma_origen_combo.grid(row=1, column=1, padx=10, pady=10)

        # Combobox para idioma de destino
        self.idioma_destino_combo = ttk.Combobox(frame, values=['es', 'en', 'fr', 'de', 'it'], state="readonly", width=10)
        self.idioma_destino_combo.set('en')
        self.idioma_destino_combo.grid(row=2, column=1, padx=10, pady=10)

        # Botón de traducción
        self.boton_traducir = tk.Button(frame, text="Traducir", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.traducir)
        self.boton_traducir.grid(row=3, column=0, columnspan=2, pady=20)
        self.boton_traducir.bind("<Enter>", self.on_hover_enter)  # Hover efect
        self.boton_traducir.bind("<Leave>", self.on_hover_leave)  # Hover effect out

        # Cuadro de texto para mostrar la traducción
        self.resultado_texto = tk.Text(frame, font=("Arial", 12), width=40, height=5, wrap=tk.WORD, state=tk.DISABLED)
        self.resultado_texto.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def traducir(self):
    # Obtener los valores de los campos
        texto = self.entrada_texto.get()
        idioma_origen = self.idioma_origen_combo.get()
        idioma_destino = self.idioma_destino_combo.get()

    # Verificar que el campo de texto no esté vacío
        if not texto.strip():
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese una frase para traducir.")
            return  # Termina la ejecución de la función si no hay texto

    # Depuración: imprimir los valores antes de enviarlos a la API
    print(f"Texto: {texto}, Idioma origen: {idioma_origen}, Idioma destino: {idioma_destino}")

    # Llamada a la API para obtener la traducción
    traduccion = self.api.traducir(texto, idioma_origen, idioma_destino)

    # Mostrar la traducción en el cuadro de texto
    self.resultado_texto.config(state=tk.NORMAL)
    self.resultado_texto.delete(1.0, tk.END)
    self.resultado_texto.insert(tk.END, traduccion)
    self.resultado_texto.config(state=tk.DISABLED)


    def on_hover_enter(self, event):
        self.boton_traducir.config(bg="#45a049")  # Cambiar color de fondo en hover

    def on_hover_leave(self, event):
        self.boton_traducir.config(bg="#4CAF50")  # Restaurar color de fondo
