# -*- coding: utf-8 -*-
import tkinter as tk
import requests
import urllib.parse

# Funcion para realizar la traduccion utilizando la API de MagicLoops
def traducir_magicloops(texto, idioma_origen, idioma_destino):
    url = 'https://magicloops.dev/api/loop/7eeeddb1-64e3-4a2b-9ae3-b22dc3002d3a/run'
    
    # Parametros para la solicitud GET
    params = {
        'q': texto,
        'source': idioma_origen,
        'target': idioma_destino,
        'format': 'text'
    }

    # Codificar los parámetros para la URL
    query_string = urllib.parse.urlencode(params)

    # Realizar la solicitud GET con los parámetros codificados
    response = requests.get(f"{url}?{query_string}")
    
    # Verificar si la respuesta es exitosa (código 200)
    if response.status_code == 200:
        try:
            # Intentamos convertir la respuesta a JSON
            result = response.json()

            # Imprimir la respuesta para inspeccionar su contenido
            print(f"Respuesta de la API: {result}")

            # Comprobamos si la respuesta tiene el formato esperado
            if isinstance(result, dict) and 'translated_text' in result:
                return result['translated_text']
            else:
                # Si la respuesta no es como esperábamos, devolvemos el contenido de la respuesta
                return f"Error: Respuesta inesperada de la API. Respuesta: {result}"
        except ValueError:
            # Si no podemos convertir la respuesta a JSON, es probable que sea un texto plano
            return f"Error: La respuesta no es un JSON valido. Respuesta: {response.text}"
    else:
        return f"Error en la solicitud: {response.status_code}"



# Funcion para obtener la traduccion y actualizar el texto en la interfaz
def obtener_traduccion():
    texto = texto_entrada.get("1.0", "end-1c")
    idioma_origen = idioma_origen_var.get()
    idioma_destino = idioma_destino_var.get()

    # Realizamos la traduccion utilizando la API de MagicLoops
    traduccion = traducir_magicloops(texto, idioma_origen, idioma_destino)

    # Mostrar la traduccion en el cuadro de texto de salida
    texto_salida.config(state=tk.NORMAL)  # Habilitar el cuadro de texto para editar
    texto_salida.delete("1.0", "end")  # Limpiar el cuadro de texto
    texto_salida.insert(tk.END, traduccion)  # Insertar el texto traducido
    texto_salida.config(state=tk.DISABLED)  # Deshabilitar el cuadro de texto para evitar edicion

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Traductor")

# Crear los cuadros de texto para ingresar el texto a traducir y mostrar el resultado
texto_entrada = tk.Text(ventana, height=10, width=50)
texto_entrada.pack(padx=10, pady=10)

texto_salida = tk.Text(ventana, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED)
texto_salida.pack(padx=10, pady=10)

# Crear los campos para seleccionar los idiomas de origen y destino
idiomas_disponibles = ["es", "en", "fr", "de", "it", "pt", "ru"]  # Agregar mas idiomas si es necesario

idioma_origen_var = tk.StringVar(ventana)
idioma_origen_var.set("es")  # Idioma de origen predeterminado: Español

idioma_destino_var = tk.StringVar(ventana)
idioma_destino_var.set("en")  # Idioma de destino predeterminado: Ingles

# Etiquetas y menus desplegables para seleccionar los idiomas
tk.Label(ventana, text="Idioma de origen:").pack()
idioma_origen_menu = tk.OptionMenu(ventana, idioma_origen_var, *idiomas_disponibles)
idioma_origen_menu.pack(pady=5)

tk.Label(ventana, text="Idioma de destino:").pack()
idioma_destino_menu = tk.OptionMenu(ventana, idioma_destino_var, *idiomas_disponibles)
idioma_destino_menu.pack(pady=5)

# Crear el boton para realizar la traduccion
boton_traducir = tk.Button(ventana, text="Traducir", command=obtener_traduccion)
boton_traducir.pack(pady=20)

# Iniciar la ventana de la aplicacion
ventana.mainloop()
