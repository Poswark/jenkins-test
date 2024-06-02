import json
import sys

def agregar_usuario(usuario, edad, namespace, branch):
    archivo_json = 'template.json'
    
    try:
        with open(archivo_json, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    if branch == "dev":
        nuevo_usuario = {
            "name": usuario,
            "edad": edad,
            "namespace": namespace,
            "host-dev": {
                "port": 1234,
                "server": "boxunging"
            }
        }
    elif branch == "uat":
        nuevo_usuario = {
            "name": usuario,
            "edad": edad,
            "namespace": namespace,
            "host-uat": {
                "port": 4321,
                "server": "boxuguat"
            }
        }
    elif branch == "prd":
        nuevo_usuario = {
            "name": usuario,
            "edad": edad,
            "namespace": namespace,
            "host-prd": {
                "port": 5678,
                "server": "boxuprd"
            }
        }
    else:
        print(f"Rama desconocida: {branch}")
        sys.exit(1)

    data.append(nuevo_usuario)
    
    with open(archivo_json, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Usuario {usuario} agregado correctamente en la rama {branch}.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: python actualizar_usuarios.py <nombre_usuario> <edad> <namespace> <rama>")
        sys.exit(1)
    
    nombre_usuario = sys.argv[1]
    edad = sys.argv[2]
    namespace = sys.argv[3]
    branch = sys.argv[4]
    
    agregar_usuario(nombre_usuario, edad, namespace, branch)
