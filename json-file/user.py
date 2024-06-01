import json
import sys

def add_data(usuario, edad, namespace):
    archivo_json = 'template.json'
    
    try:
        with open(archivo_json, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    # Asegurarse de que data es una lista
    if not isinstance(data, list):
        data = []

    # Agregar nuevo usuario con edad y namespace
    data.append({
        "name": usuario,
        "edad": edad,
        "namespace": namespace,
        "host": {
            "port": 1234,
            "server": "boxung"
        }
    })
    
    with open(archivo_json, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Usuario {usuario} con edad {edad} y namespace {namespace} agregado correctamente.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python actualizar_usuarios.py <nombre_usuario> <edad> <namespace>")
        sys.exit(1)
    
    nombre_usuario = sys.argv[1]
    edad = sys.argv[2]
    namespace = sys.argv[3]
    
    add_data(nombre_usuario, edad, namespace)
