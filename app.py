import os
import yaml

# Configuración
app_name = "my-new-app"  # Nombre de la nueva aplicación
namespace = "my-namespace"  # Namespace donde se desplegará la aplicación
project_name = "my-project"  # Nombre del proyecto

base_path = "namespace-argocd-apps/base"
env_path = "namespace-argocd-apps/env"
environments = ["dev", "uat", "prd"]

# Template de la nueva aplicación
app_template = {
    "apiVersion": "argoproj.io/v1alpha1",
    "kind": "Application",
    "metadata": {
        "name": app_name,
        "namespace": namespace
    },
    "spec": {
        "project": project_name,
        "destination": {
            "namespace": namespace,
            "server": "https://kubernetes.default.svc"
        },
        "source": {
            "path": "kustomize-guestbook",
            "repoURL": "https://github.com/argoproj/argocd-example-apps",
            "targetRevision": "HEAD",
            "kustomize": {
                "commonAnnotationsEnvsubst": True,
                "commonAnnotations": {
                    "app-source": "${ARGOCD_APP_NAME}"
                }
            }
        },
        "syncPolicy": {
            "syncOptions": [
                "CreateNamespace=true"
            ]
        }
    }
}

# Crear el archivo YAML para la nueva aplicación
app_yaml_path = os.path.join(base_path, f"{app_name}.yaml")
with open(app_yaml_path, 'w') as yaml_file:
    yaml.dump(app_template, yaml_file, default_flow_style=False)
print(f"Archivo YAML creado en: {app_yaml_path}")

# Agregar el nuevo archivo a kustomization.yaml en cada entorno
for env in environments:
    kustomization_path = os.path.join(env_path, env, "kustomization.yaml")
    
    with open(kustomization_path, 'r') as kustom_file:
        kustom_data = yaml.safe_load(kustom_file)
    
    # Añadir el nuevo recurso
    if "resources" not in kustom_data:
        kustom_data["resources"] = []
    
    new_resource = os.path.relpath(app_yaml_path, start=os.path.dirname(kustomization_path))
    
    if new_resource not in kustom_data["resources"]:
        kustom_data["resources"].append(new_resource)
    
    # Guardar el archivo actualizado
    with open(kustomization_path, 'w') as kustom_file:
        yaml.dump(kustom_data, kustom_file, default_flow_style=False)
    print(f"Actualizado kustomization.yaml en: {kustomization_path}")
