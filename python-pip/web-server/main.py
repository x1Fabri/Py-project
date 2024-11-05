import store 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() #Creamos nuestra primera instancia y con esto creamos nuestro primer recurso

#Ruta primaria
@app.get("/") #Agregamos el decorador para decirle cual es la ruta
def get_list(): #Devuelve una lista de números
    return [1, 2, 3,]

#Ruta secundaria
@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return """
            <h1>Soy un sitio web</h1>
            <p>Soy un párrafo para que tu me leas</p>
"""

def run():
    store.get_razas()

if __name__ == "__main__":
    run()

    