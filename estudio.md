# 🚀 Bootcamp: Agente CI/CD con MCP y Gemini

## Del concepto a producción en 7 días

---

## 📋 Índice

1. [Día 0: Preparación y Setup](#día-0-preparación-y-setup)
2. [Día 1: Fundamentos y Arquitectura](#día-1-fundamentos-y-arquitectura)
3. [Día 2: MCP Server - Herramientas Básicas](#día-2-mcp-server---herramientas-básicas)
4. [Día 3: Agente Inteligente con Gemini](#día-3-agente-inteligente-con-gemini)
5. [Día 4: Herramientas Avanzadas](#día-4-herramientas-avanzadas)
6. [Día 5: UI y Experiencia de Usuario](#día-5-ui-y-experiencia-de-usuario)
7. [Día 6: Testing y Optimización](#día-6-testing-y-optimización)
8. [Día 7: Deploy y Monitoreo](#día-7-deploy-y-monitoreo)
9. [Bonus: Ideas de Expansión](#bonus-ideas-de-expansión)

---

## 🎯 Objetivo Final

Construir un agente AI que pueda:

```
"¿Qué pipelines fallaron hoy?"
"Analiza por qué falló el build #1234"
"Ejecuta el pipeline de backend en staging"
"Dame métricas DORA de esta semana"
"Haz rollback del último deploy de payment-service"
```

---

## 📦 Stack Tecnológico

```yaml
AI Engine: Google Gemini 2.5 Flash
MCP Framework: FastMCP
CI/CD Platforms:
  - GitHub Actions (principal)
  - GitLab CI (opcional)
  - Jenkins (opcional)
Backend: Python 3.11+
UI: Streamlit
DevOps: Docker + Docker Compose
```

---

# Día 0: Preparación y Setup

## ✅ Pre-requisitos

### Conocimientos necesarios:
- ✅ Python básico
- ✅ Git básico
- ✅ Docker básico
- ✅ Familiaridad con CI/CD (haber usado GitHub Actions o similar)

### Cuentas requeridas:
- GitHub account (gratis)
- Google Cloud (para Gemini API - gratis)
- Acceso a un repo con GitHub Actions

### Software a instalar:
```bash
# 1. Python 3.11+
python --version

# 2. Docker Desktop
docker --version

# 3. Git
git --version

# 4. Editor (VS Code recomendado)
code --version
```

---

## 🎯 Setup Inicial

### 1. Crear estructura del proyecto

```bash
mkdir cicd-mcp-agent
cd cicd-mcp-agent

# Estructura de carpetas
mkdir -p {mcp-server,agent,ui,tests,docs}

# Archivos base
touch .env.example .gitignore README.md
touch docker-compose.yml Makefile
```

### 2. Estructura final

```
cicd-mcp-agent/
├── mcp-server/           # Servidor MCP con herramientas
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── config.py
│   ├── server.py
│   └── tools/
│       ├── github.py     # GitHub Actions tools
│       ├── metrics.py    # DORA metrics
│       └── analysis.py   # Log analysis
├── agent/                # Agente con Gemini
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── agent.py
│   ├── prompts.py
│   └── ui.py             # Streamlit UI
├── tests/                # Tests
├── docs/                 # Documentación
├── .env.example
├── docker-compose.yml
└── Makefile
```

### 3. Obtener credenciales

**GitHub Personal Access Token:**
```bash
# 1. Ve a: https://github.com/settings/tokens
# 2. Generate new token (classic)
# 3. Permisos necesarios:
#    - repo (todos)
#    - workflow
#    - read:org (si usas organizaciones)
# 4. Copia el token

# En .env:
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxx
GITHUB_OWNER=tu-usuario-o-org
GITHUB_REPO=tu-repo
```

**Gemini API Key:**
```bash
# 1. Ve a: https://makersuite.google.com/app/apikey
# 2. Create API key
# 3. Copia la key

# En .env:
GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxx
```

### 4. Crear .env.example

```bash
cat > .env.example << 'EOF'
# Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# GitHub
GITHUB_TOKEN=your_github_token_here
GITHUB_OWNER=your-github-username
GITHUB_REPO=your-repo-name

# MCP Server
MCP_SERVER_URL=http://mcp-server:8000

# Logging
LOG_LEVEL=INFO
EOF
```

### 5. Verificar setup

```bash
# Copiar .env
cp .env.example .env

# Editar con tus credenciales
nano .env

# Verificar que todo está listo
python --version    # 3.11+
docker --version    # 20.10+
echo $GITHUB_TOKEN  # Debería mostrar tu token
```

---

# Día 1: Fundamentos y Arquitectura

## 📚 Conceptos Clave

### 1. ¿Qué vamos a construir?

```
Usuario → UI → Agente (Gemini) → MCP Server → GitHub API
         Chat   Cerebro IA        Herramientas   Datos CI/CD
```

**Flujo de ejemplo:**
```
Usuario: "¿Por qué falló el build #123?"
   ↓
Agente analiza con Gemini
   ↓
Decide usar: get_workflow_run(123) + get_job_logs(123)
   ↓
MCP Server ejecuta tools
   ↓
GitHub API devuelve datos
   ↓
Agente formatea respuesta: "Falló el test de integración 
por timeout en conexión a DB"
```

---

## 🏗️ Arquitectura Detallada

### Componentes:

**1. UI (Streamlit)**
```python
# Interfaz web donde el usuario hace preguntas
# Puerto: 8501
# Funciones:
- Chat interactivo
- Historial de conversación
- Botones de ejemplo
- Visualización de métricas
```

**2. Agente (Gemini + Python)**
```python
# Cerebro del sistema
# Responsabilidades:
- Entender lenguaje natural
- Decidir qué herramientas MCP usar
- Formatear respuestas
- Mantener contexto de conversación
```

**3. MCP Server (FastMCP)**
```python
# Servidor de herramientas
# Puerto: 8000
# Herramientas:
- get_workflow_runs()      # Lista de pipelines
- get_workflow_run(id)     # Detalles de pipeline
- get_job_logs(job_id)     # Logs específicos
- trigger_workflow()       # Ejecutar pipeline
- get_deployments()        # Historial de deploys
- calculate_dora_metrics() # Métricas DORA
- analyze_failure()        # Análisis de fallos
```

**4. GitHub API**
```python
# API REST de GitHub
# Endpoints principales:
/repos/{owner}/{repo}/actions/runs
/repos/{owner}/{repo}/actions/runs/{run_id}
/repos/{owner}/{repo}/actions/runs/{run_id}/jobs
/repos/{owner}/{repo}/deployments
```

---

## 📊 Casos de Uso

### Caso 1: Consulta Simple
```
Usuario: "¿Qué pipelines corrieron hoy?"
   ↓
Agente: get_workflow_runs(date=today)
   ↓
Respuesta: "Hoy corrieron 15 pipelines:
  - backend-ci: ✅ Exitoso
  - frontend-ci: ✅ Exitoso
  - deploy-staging: ❌ Fallido
  ..."
```

### Caso 2: Análisis Complejo
```
Usuario: "¿Por qué falló el deploy a staging?"
   ↓
Agente:
  1. get_workflow_runs(name="deploy-staging", status="failed")
  2. get_workflow_run(id) → obtiene job IDs
  3. get_job_logs(job_id) → analiza logs
  4. Gemini analiza los logs
   ↓
Respuesta: "El deploy falló porque:
  1. Test de integración timeout (línea 234)
  2. Error conectando a DB staging
  3. Posible causa: Credenciales vencidas
  
  Recomendación: Verificar secrets en GitHub"
```

### Caso 3: Acción + Análisis
```
Usuario: "Ejecuta el pipeline de backend en staging"
   ↓
Agente:
  1. trigger_workflow(workflow="backend-ci", ref="staging")
  2. Espera inicio
  3. get_workflow_run(id) → monitorea progreso
   ↓
Respuesta: "Pipeline iniciado (#456)
  Estado: En progreso
  Jobs completados: 2/5
  
  Te notificaré cuando termine"
```

---

## 🔑 Herramientas MCP (Overview)

### Básicas (Día 2):
1. **get_workflow_runs()** - Lista pipelines
2. **get_workflow_run(id)** - Detalles de pipeline
3. **get_job_logs(job_id)** - Logs de job

### Intermedias (Día 4):
4. **trigger_workflow()** - Ejecutar pipeline
5. **get_deployments()** - Historial deploys
6. **cancel_workflow()** - Cancelar pipeline

### Avanzadas (Día 4):
7. **calculate_dora_metrics()** - Lead time, deploy frequency
8. **analyze_failure()** - AI analysis de logs
9. **compare_runs()** - Comparar pipelines

---

## 📝 Ejercicio Día 1

### Tarea: Planifica tu agente

**1. Define tu caso de uso principal:**
```
Ejemplo: "Quiero saber rápido por qué fallan los pipelines 
sin revisar manualmente GitHub Actions"
```

**2. Lista las preguntas más comunes que harías:**
```
- ¿Qué pipelines fallaron hoy?
- ¿Por qué falló X?
- ¿Cuánto tardó el último deploy?
- ¿Hay algún pipeline corriendo ahora?
```

**3. Identifica tu repo de prueba:**
```
GITHUB_OWNER: tu-usuario
GITHUB_REPO: tu-repo-con-actions
```

**4. Revisa que tengas workflows activos:**
```bash
# Lista tus workflows
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$GITHUB_OWNER/$GITHUB_REPO/actions/workflows
```

---

# Día 2: MCP Server - Herramientas Básicas

## 🎯 Objetivo del día
Crear el servidor MCP con 3 herramientas básicas funcionando.

---

## 📦 Setup del MCP Server

### 1. Crear requirements.txt

```python
# mcp-server/requirements.txt
fastmcp==0.5.0
requests==2.31.0
PyGithub==2.1.1
python-dotenv==1.0.0
pydantic==2.5.0
```

### 2. Crear config.py

```python
# mcp-server/config.py
import os
from typing import Optional

class Config:
    """Configuración del servidor MCP"""
    
    # GitHub Configuration
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")
    GITHUB_OWNER: str = os.getenv("GITHUB_OWNER", "")
    GITHUB_REPO: str = os.getenv("GITHUB_REPO", "")
    GITHUB_API_BASE: str = "https://api.github.com"
    
    # Server Configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # Timeouts
    MAX_RETRIES: int = 3
    TIMEOUT: int = 30
    
    @classmethod
    def validate(cls):
        """Valida que las variables necesarias estén configuradas"""
        if not cls.GITHUB_TOKEN:
            raise ValueError("GITHUB_TOKEN no configurado")
        if not cls.GITHUB_OWNER:
            raise ValueError("GITHUB_OWNER no configurado")
        if not cls.GITHUB_REPO:
            raise ValueError("GITHUB_REPO no configurado")

config = Config()
```

---

## 🔧 Herramienta 1: get_workflow_runs

### Propósito:
Obtener lista de ejecuciones de workflows (pipelines)

### Código:

```python
# mcp-server/tools/github.py
import requests
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import logging
from config import config

logger = logging.getLogger(__name__)

def get_headers() -> Dict[str, str]:
    """Headers para autenticación con GitHub"""
    return {
        "Authorization": f"token {config.GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

def get_workflow_runs(
    status: Optional[str] = None,
    branch: Optional[str] = None,
    event: Optional[str] = None,
    per_page: int = 30
) -> Dict[str, Any]:
    """
    Obtiene lista de workflow runs (pipelines)
    
    Args:
        status: Estado del workflow (queued, in_progress, completed)
        branch: Filtrar por rama
        event: Filtrar por evento (push, pull_request, etc.)
        per_page: Número de resultados (max 100)
        
    Returns:
        Diccionario con workflow runs y metadata
    """
    try:
        url = f"{config.GITHUB_API_BASE}/repos/{config.GITHUB_OWNER}/{config.GITHUB_REPO}/actions/runs"
        
        params = {
            "per_page": min(per_page, 100)
        }
        
        if status:
            params["status"] = status
        if branch:
            params["branch"] = branch
        if event:
            params["event"] = event
        
        logger.info(f"Obteniendo workflow runs con params: {params}")
        
        response = requests.get(
            url,
            headers=get_headers(),
            params=params,
            timeout=config.TIMEOUT
        )
        response.raise_for_status()
        
        data = response.json()
        
        # Formatear respuesta
        runs = []
        for run in data.get("workflow_runs", []):
            runs.append({
                "id": run["id"],
                "name": run["name"],
                "status": run["status"],
                "conclusion": run.get("conclusion"),
                "branch": run["head_branch"],
                "event": run["event"],
                "created_at": run["created_at"],
                "updated_at": run["updated_at"],
                "html_url": run["html_url"],
                "run_number": run["run_number"]
            })
        
        logger.info(f"Encontrados {len(runs)} workflow runs")
        
        return {
            "total_count": data.get("total_count", 0),
            "runs": runs
        }
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error obteniendo workflow runs: {e}")
        return {"error": str(e), "runs": []}
```

### Ejemplo de uso:

```python
# Lista todos los pipelines
result = get_workflow_runs()
# → {"total_count": 150, "runs": [{...}, {...}]}

# Solo los que fallaron
result = get_workflow_runs(status="completed", conclusion="failure")

# Solo de la rama main
result = get_workflow_runs(branch="main")
```

---

## 🔧 Herramienta 2: get_workflow_run

### Propósito:
Obtener detalles de un workflow run específico

### Código:

```python
# mcp-server/tools/github.py (continúa)

def get_workflow_run(run_id: int) -> Dict[str, Any]:
    """
    Obtiene detalles de un workflow run específico
    
    Args:
        run_id: ID del workflow run
        
    Returns:
        Diccionario con detalles completos del run
    """
    try:
        url = f"{config.GITHUB_API_BASE}/repos/{config.GITHUB_OWNER}/{config.GITHUB_REPO}/actions/runs/{run_id}"
        
        logger.info(f"Obteniendo detalles del workflow run: {run_id}")
        
        response = requests.get(
            url,
            headers=get_headers(),
            timeout=config.TIMEOUT
        )
        response.raise_for_status()
        
        run = response.json()
        
        # Obtener también los jobs de este run
        jobs = get_run_jobs(run_id)
        
        return {
            "id": run["id"],
            "name": run["name"],
            "status": run["status"],
            "conclusion": run.get("conclusion"),
            "branch": run["head_branch"],
            "event": run["event"],
            "created_at": run["created_at"],
            "updated_at": run["updated_at"],
            "run_started_at": run.get("run_started_at"),
            "html_url": run["html_url"],
            "run_number": run["run_number"],
            "commit": {
                "message": run["head_commit"]["message"],
                "author": run["head_commit"]["author"]["name"],
                "sha": run["head_sha"][:7]
            },
            "jobs": jobs,
            "run_duration_seconds": calculate_duration(run)
        }
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error obteniendo workflow run {run_id}: {e}")
        return {"error": str(e), "run_id": run_id}

def get_run_jobs(run_id: int) -> List[Dict[str, Any]]:
    """Obtiene los jobs de un workflow run"""
    try:
        url = f"{config.GITHUB_API_BASE}/repos/{config.GITHUB_OWNER}/{config.GITHUB_REPO}/actions/runs/{run_id}/jobs"
        
        response = requests.get(
            url,
            headers=get_headers(),
            timeout=config.TIMEOUT
        )
        response.raise_for_status()
        
        data = response.json()
        
        jobs = []
        for job in data.get("jobs", []):
            jobs.append({
                "id": job["id"],
                "name": job["name"],
                "status": job["status"],
                "conclusion": job.get("conclusion"),
                "started_at": job.get("started_at"),
                "completed_at": job.get("completed_at"),
                "html_url": job["html_url"],
                "steps": len(job.get("steps", []))
            })
        
        return jobs
        
    except Exception as e:
        logger.error(f"Error obteniendo jobs: {e}")
        return []

def calculate_duration(run: Dict) -> int:
    """Calcula duración de un run en segundos"""
    try:
        if run.get("run_started_at") and run.get("updated_at"):
            start = datetime.fromisoformat(run["run_started_at"].replace("Z", "+00:00"))
            end = datetime.fromisoformat(run["updated_at"].replace("Z", "+00:00"))
            return int((end - start).total_seconds())
    except:
        pass
    return 0
```

---

## 🔧 Herramienta 3: get_job_logs

### Propósito:
Obtener logs de un job específico

### Código:

```python
# mcp-server/tools/github.py (continúa)

def get_job_logs(job_id: int) -> Dict[str, Any]:
    """
    Obtiene los logs de un job específico
    
    Args:
        job_id: ID del job
        
    Returns:
        Diccionario con logs del job
    """
    try:
        url = f"{config.GITHUB_API_BASE}/repos/{config.GITHUB_OWNER}/{config.GITHUB_REPO}/actions/jobs/{job_id}/logs"
        
        logger.info(f"Obteniendo logs del job: {job_id}")
        
        response = requests.get(
            url,
            headers=get_headers(),
            timeout=config.TIMEOUT
        )
        response.raise_for_status()
        
        # Los logs vienen como texto plano
        logs_text = response.text
        
        # Parsear logs para extraer errores
        errors = extract_errors_from_logs(logs_text)
        
        return {
            "job_id": job_id,
            "logs": logs_text,
            "log_length": len(logs_text),
            "errors_found": len(errors),
            "errors": errors[:10]  # Primeros 10 errores
        }
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error obteniendo logs del job {job_id}: {e}")
        return {"error": str(e), "job_id": job_id}

def extract_errors_from_logs(logs: str) -> List[str]:
    """Extrae líneas de error de los logs"""
    errors = []
    
    # Patrones comunes de error
    error_patterns = [
        "error:",
        "ERROR:",
        "failed:",
        "FAILED:",
        "exception:",
        "Exception:",
        "Error:",
        "✗",
        "❌"
    ]
    
    for line in logs.split("\n"):
        line_lower = line.lower()
        if any(pattern.lower() in line_lower for pattern in error_patterns):
            # Limpiar ANSI codes
            clean_line = line.strip()
            if clean_line and len(clean_line) > 10:  # Ignorar líneas muy cortas
                errors.append(clean_line[:200])  # Limitar longitud
    
    return errors
```

---

## 🚀 Crear el servidor MCP

### server.py completo:

```python
# mcp-server/server.py
"""
CI/CD MCP Server
Servidor MCP para GitHub Actions
"""

import logging
from fastmcp import FastMCP
from config import config
from tools.github import (
    get_workflow_runs,
    get_workflow_run,
    get_job_logs
)

# Configurar logging
logging.basicConfig(
    level=getattr(logging, config.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Validar configuración
config.validate()

# Inicializar FastMCP
mcp = FastMCP("CI/CD MCP Server")

# Registrar herramientas
@mcp.tool()
def list_workflow_runs(
    status: str = None,
    branch: str = None,
    limit: int = 30
):
    """
    Lista las ejecuciones de workflows (pipelines)
    
    Args:
        status: Filtrar por estado (queued, in_progress, completed)
        branch: Filtrar por rama
        limit: Número máximo de resultados (1-100)
    """
    return get_workflow_runs(status=status, branch=branch, per_page=limit)

@mcp.tool()
def get_run_details(run_id: int):
    """
    Obtiene detalles completos de un workflow run específico
    
    Args:
        run_id: ID del workflow run
    """
    return get_workflow_run(run_id)

@mcp.tool()
def get_logs(job_id: int):
    """
    Obtiene los logs de un job específico
    
    Args:
        job_id: ID del job
    """
    return get_job_logs(job_id)

@mcp.tool()
def health_check():
    """Verifica el estado del servidor y conexión con GitHub"""
    try:
        # Test simple: obtener info del repo
        import requests
        url = f"{config.GITHUB_API_BASE}/repos/{config.GITHUB_OWNER}/{config.GITHUB_REPO}"
        headers = {"Authorization": f"token {config.GITHUB_TOKEN}"}
        response = requests.get(url, headers=headers, timeout=5)
        
        github_status = "healthy" if response.status_code == 200 else "unhealthy"
        
        return {
            "server": "healthy",
            "github_api": github_status,
            "repo": f"{config.GITHUB_OWNER}/{config.GITHUB_REPO}"
        }
    except Exception as e:
        return {
            "server": "healthy",
            "github_api": f"error: {str(e)}"
        }

if __name__ == "__main__":
    logger.info("Iniciando CI/CD MCP Server")
    logger.info(f"Repo: {config.GITHUB_OWNER}/{config.GITHUB_REPO}")
    logger.info(f"Escuchando en {config.HOST}:{config.PORT}")
    
    try:
        logger.info("Servidor MCP listo. Esperando conexiones...")
        import signal
        signal.pause()
    except KeyboardInterrupt:
        logger.info("Servidor detenido por usuario")
```

---

## 🐳 Dockerizar el MCP Server

### Dockerfile:

```dockerfile
# mcp-server/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Exponer puerto
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "from tools.github import get_workflow_runs; print('OK')"

# Comando de inicio
CMD ["python", "server.py"]
```

---

## 🧪 Testing Día 2

### Test manual de las herramientas:

```python
# test_tools.py
from tools.github import (
    get_workflow_runs,
    get_workflow_run,
    get_job_logs
)

# Test 1: Listar workflows
print("=" * 50)
print("TEST 1: Listar workflow runs")
print("=" * 50)
result = get_workflow_runs(per_page=5)
print(f"Total encontrados: {result['total_count']}")
for run in result['runs'][:3]:
    print(f"  - {run['name']} #{run['run_number']}: {run['conclusion']}")

# Test 2: Detalles de un run
print("\n" + "=" * 50)
print("TEST 2: Detalles de workflow run")
print("=" * 50)
if result['runs']:
    run_id = result['runs'][0]['id']
    details = get_workflow_run(run_id)
    print(f"Run #{details['run_number']}: {details['name']}")
    print(f"Status: {details['status']}")
    print(f"Jobs: {len(details['jobs'])}")
    for job in details['jobs']:
        print(f"  - {job['name']}: {job['conclusion']}")

# Test 3: Logs de un job
print("\n" + "=" * 50)
print("TEST 3: Logs de job")
print("=" * 50)
if details['jobs']:
    job_id = details['jobs'][0]['id']
    logs = get_job_logs(job_id)
    print(f"Job ID: {job_id}")
    print(f"Tamaño de logs: {logs['log_length']} caracteres")
    print(f"Errores encontrados: {logs['errors_found']}")
    if logs['errors']:
        print("Primeros errores:")
        for error in logs['errors'][:3]:
            print(f"  - {error[:100]}...")
```

### Ejecutar test:

```bash
cd mcp-server
python test_tools.py
```

**Output esperado:**
```
==================================================
TEST 1: Listar workflow runs
==================================================
Total encontrados: 150
  - CI Pipeline #45: success
  - Deploy Staging #12: failure
  - Tests #234: success

==================================================
TEST 2: Detalles de workflow run
==================================================
Run #45: CI Pipeline
Status: completed
Jobs: 3
  - build: success
  - test: success
  - lint: success

==================================================
TEST 3: Logs de job
==================================================
Job ID: 12345678
Tamaño de logs: 45230 caracteres
Errores encontrados: 0
```

---

## ✅ Checklist Día 2

- [ ] `mcp-server/` estructura creada
- [ ] `config.py` configurado con GitHub token
- [ ] `tools/github.py` con 3 herramientas funcionando
- [ ] `server.py` con FastMCP inicializado
- [ ] `Dockerfile` creado
- [ ] Test manual ejecutado exitosamente
- [ ] Logs muestran conexión exitosa a GitHub

---

## 📝 Ejercicio Día 2

### Tarea: Agregar una herramienta personalizada

Crea una nueva herramienta que filtre workflows por conclusión:

```python
def get_failed_runs_today():
    """
    Obtiene todos los workflows que fallaron hoy
    
    Returns:
        Lista de workflow runs que fallaron
    """
    # Tu código aquí
    # Pista: Usa get_workflow_runs() y filtra por fecha
    pass
```

**Bonus:** Haz que retorne también un resumen:
```python
{
    "total_failed": 5,
    "runs": [...],
    "most_common_failure": "test timeout"
}
```

---

# Día 3: Agente Inteligente con Gemini

## 🎯 Objetivo del día
Crear el agente que usa Gemini para entender consultas y usar las herramientas MCP.

---

## 📦 Setup del Agente

### 1. Crear requirements.txt

```python
# agent/requirements.txt
google-generativeai>=0.7.0
requests==2.31.0
python-dotenv==1.0.0
pydantic==2.5.0
rich==13.7.0
```

### 2. Crear prompts.py

```python
# agent/prompts.py
"""
Prompts del sistema para el agente CI/CD
"""

SYSTEM_PROMPT = """Eres un agente AI experto en CI/CD y DevOps.
Tu objetivo es ayudar a desarrolladores y DevOps engineers a entender y 
gestionar sus pipelines de CI/CD.

CAPACIDADES:
- Analizar workflows de GitHub Actions
- Identificar causas de fallos en pipelines
- Proporcionar métricas y estadísticas
- Ejecutar y monitorear pipelines
- Dar recomendaciones de mejora

HERRAMIENTAS DISPONIBLES (vía MCP Server):
1. list_workflow_runs(status, branch, limit) - Lista ejecuciones de workflows
2. get_run_details(run_id) - Detalles completos de un run
3. get_logs(job_id) - Logs de un job específico
4. health_check() - Estado del sistema

ESTILO DE RESPUESTA:
- Sé directo y técnico pero claro
- Usa emojis para estados: ✅ (success), ❌ (failure), ⏳ (in progress)
- Proporciona URLs cuando sea relevante
- Sugiere acciones concretas
- Si encuentras errores en logs, explícalos claramente

FORMATO:
- Organiza información con bullets o numeración
- Resalta lo importante
- Incluye timestamps cuando sea relevante
"""

USER_GREETING = """¡Hola! Soy tu asistente de CI/CD 🚀

Puedo ayudarte con:
• Revisar estado de pipelines
• Analizar fallos de builds
• Obtener métricas de deployment
• Ejecutar y monitorear workflows

¿Qué necesitas saber sobre tus pipelines?
"""

ANALYSIS_PROMPT_TEMPLATE = """
Analiza esta consulta del usuario y determina qué herramientas MCP necesitas:

CONSULTA: {user_query}

HERRAMIENTAS DISPONIBLES:
- list_workflow_runs(status, branch, limit): Para listar workflows
- get_run_details(run_id): Para detalles de un workflow específico
- get_logs(job_id): Para obtener logs de un job

Responde en formato JSON:
{{
    "tools_needed": [
        {{"tool": "nombre_herramienta", "params": {{"param1": "valor"}}}}
    ],
    "reasoning": "Por qué necesitas estas herramientas"
}}
"""

ERROR_ANALYSIS_PROMPT = """
Analiza estos logs de error y proporciona:
1. Causa raíz del problema
2. Línea o sección específica donde ocurre
3. Posible solución
4. Recomendaciones para prevenir en el futuro

LOGS:
{logs}

ERRORES IDENTIFICADOS:
{errors}
"""
```

---

## 🧠 Crear el Agente

### agent.py completo:

```python
# agent/agent.py
"""
CI/CD Agent
Agente inteligente para gestión de pipelines CI/CD
"""

import os
import json
import logging
from typing import Dict, Any, List
import google.generativeai as genai
import requests
from rich.console import Console
from rich.markdown import Markdown
from dotenv import load_dotenv

from prompts import (
    SYSTEM_PROMPT,
    USER_GREETING,
    ANALYSIS_PROMPT_TEMPLATE,
    ERROR_ANALYSIS_PROMPT
)

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

console = Console()


class MCPClient:
    """Cliente para interactuar con el servidor MCP"""
    
    def __init__(self, server_url: str):
        self.server_url = server_url
        self.session = requests.Session()
        logger.info(f"MCPClient inicializado con URL: {server_url}")
    
    def call_tool(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """
        Llama a una herramienta del servidor MCP
        
        Args:
            tool_name: Nombre de la herramienta
            **kwargs: Argumentos para la herramienta
            
        Returns:
            Resultado de la herramienta
        """
        # Mapeo de herramientas a endpoints
        # En producción, esto usaría el protocolo MCP real
        # Por ahora, llamamos directamente a las funciones
        
        try:
            logger.info(f"Llamando herramienta: {tool_name} con args: {kwargs}")
            
            # Import dinámico de las herramientas
            from mcp_server.tools.github import (
                get_workflow_runs,
                get_workflow_run,
                get_job_logs
            )
            
            if tool_name == "list_workflow_runs":
                result = get_workflow_runs(
                    status=kwargs.get('status'),
                    branch=kwargs.get('branch'),
                    per_page=kwargs.get('limit', 30)
                )
            elif tool_name == "get_run_details":
                result = get_workflow_run(kwargs.get('run_id'))
            elif tool_name == "get_logs":
                result = get_job_logs(kwargs.get('job_id'))
            elif tool_name == "health_check":
                result = {"server": "healthy", "github": "connected"}
            else:
                raise ValueError(f"Herramienta desconocida: {tool_name}")
            
            logger.info(f"Herramienta {tool_name} ejecutada exitosamente")
            return result
            
        except Exception as e:
            logger.error(f"Error en {tool_name}: {e}")
            return {"error": str(e), "tool": tool_name}
    
    def health_check(self) -> bool:
        """Verifica si el servidor MCP está activo"""
        try:
            result = self.call_tool("health_check")
            return "error" not in result
        except:
            return False


class CICDAgent:
    """Agente principal con Gemini"""
    
    def __init__(self, gemini_api_key: str, mcp_client: MCPClient):
        self.mcp_client = mcp_client
        
        # Configurar Gemini
        genai.configure(api_key=gemini_api_key)
        
        # Lista de modelos a probar
        models_to_try = [
            'gemini-2.5-flash',
            'gemini-flash-latest',
            'gemini-2.0-flash',
            'gemini-2.5-pro',
            'gemini-pro-latest',
        ]
        
        model_initialized = False
        
        for model_name in models_to_try:
            try:
                logger.info(f"Intentando inicializar modelo: {model_name}")
                
                try:
                    self.model = genai.GenerativeModel(
                        model_name=model_name,
                        system_instruction=SYSTEM_PROMPT
                    )
                except TypeError:
                    self.model = genai.GenerativeModel(model_name=model_name)
                
                self.chat = self.model.start_chat(history=[])
                
                if not hasattr(self.model, 'system_instruction'):
                    self.chat.send_message(SYSTEM_PROMPT)
                
                logger.info(f"✅ Modelo inicializado: {model_name}")
                model_initialized = True
                break
                
            except Exception as e:
                logger.warning(f"❌ Error con modelo {model_name}: {e}")
                continue
        
        if not model_initialized:
            raise RuntimeError("No se pudo inicializar ningún modelo de Gemini")
    
    def process_query(self, user_query: str) -> str:
        """
        Procesa una consulta del usuario
        
        Args:
            user_query: Consulta del usuario
            
        Returns:
            Respuesta generada
        """
        try:
            logger.info(f"Procesando query: {user_query}")
            
            # Paso 1: Analizar qué herramientas necesitamos
            analysis_prompt = ANALYSIS_PROMPT_TEMPLATE.format(
                user_query=user_query
            )
            
            response = self.chat.send_message(analysis_prompt)
            plan_text = response.text
            
            # Limpiar JSON
            if "```json" in plan_text:
                plan_text = plan_text.split("```json")[1].split("```")[0]
            elif "```" in plan_text:
                plan_text = plan_text.split("```")[1].split("```")[0]
            
            plan_text = plan_text.strip()
            
            try:
                plan = json.loads(plan_text)
            except json.JSONDecodeError:
                # Fallback: búsqueda simple
                plan = {
                    "tools_needed": [{"tool": "list_workflow_runs", "params": {}}],
                    "reasoning": "Consulta general"
                }
            
            logger.info(f"Plan: {plan['reasoning']}")
            
            # Paso 2: Ejecutar herramientas
            tool_results = []
            for tool_call in plan.get("tools_needed", []):
                tool_name = tool_call.get("tool")
                params = tool_call.get("params", {})
                
                result = self.mcp_client.call_tool(tool_name, **params)
                tool_results.append({
                    "tool": tool_name,
                    "params": params,
                    "result": result
                })
            
            # Paso 3: Generar respuesta final
            final_prompt = f"""
CONSULTA ORIGINAL: {user_query}

DATOS OBTENIDOS:
{json.dumps(tool_results, indent=2, ensure_ascii=False)}

Genera una respuesta clara, organizada y útil para el usuario.
Usa emojis para estados (✅ ❌ ⏳).
Si hay errores en logs, analízalos y explícalos.
Proporciona URLs cuando sea relevante.
"""
            
            final_response = self.chat.send_message(final_prompt)
            
            return final_response.text
            
        except Exception as e:
            logger.error(f"Error procesando query: {e}")
            return f"❌ Error: {str(e)}"
    
    def analyze_failure(self, run_id: int) -> str:
        """
        Analiza en detalle por qué falló un workflow
        
        Args:
            run_id: ID del workflow run
            
        Returns:
            Análisis detallado
        """
        try:
            # Obtener detalles del run
            run_details = self.mcp_client.call_tool(
                "get_run_details",
                run_id=run_id
            )
            
            if "error" in run_details:
                return f"❌ Error obteniendo detalles: {run_details['error']}"
            
            # Encontrar jobs que fallaron
            failed_jobs = [
                job for job in run_details.get("jobs", [])
                if job.get("conclusion") == "failure"
            ]
            
            if not failed_jobs:
                return "No se encontraron jobs fallidos en este run"
            
            # Obtener logs del primer job fallido
            job_id = failed_jobs[0]["id"]
            logs_data = self.mcp_client.call_tool("get_logs", job_id=job_id)
            
            # Analizar con Gemini
            analysis_prompt = ERROR_ANALYSIS_PROMPT.format(
                logs=logs_data.get("logs", "")[:5000],  # Limitar tamaño
                errors="\n".join(logs_data.get("errors", [])[:10])
            )
            
            response = self.chat.send_message(analysis_prompt)
            
            # Formatear respuesta
            result = f"""
## Análisis del Workflow Run #{run_details['run_number']}

**Workflow:** {run_details['name']}
**Estado:** {run_details['conclusion']} ❌
**Branch:** {run_details['branch']}
**Commit:** {run_details['commit']['message'][:50]}...

**Jobs fallidos:** {len(failed_jobs)}
- {failed_jobs[0]['name']}

---

{response.text}

**Ver en GitHub:** {run_details['html_url']}
"""
            
            return result
            
        except Exception as e:
            logger.error(f"Error analizando fallo: {e}")
            return f"❌ Error en análisis: {str(e)}"


def main():
    """Función principal - modo interactivo"""
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    mcp_server_url = os.getenv("MCP_SERVER_URL", "http://localhost:8000")
    
    if not gemini_api_key:
        console.print("[red]Error: GEMINI_API_KEY no configurada[/red]")
        return
    
    # Inicializar
    mcp_client = MCPClient(mcp_server_url)
    agent = CICDAgent(gemini_api_key, mcp_client)
    
    # Saludo
    console.print(Markdown(USER_GREETING))
    
    # Loop interactivo
    while True:
        try:
            user_input = console.input("\n[bold cyan]Tú:[/bold cyan] ")
            
            if user_input.lower() in ['salir', 'exit', 'quit']:
                console.print("[yellow]¡Hasta luego! 👋[/yellow]")
                break
            
            if not user_input.strip():
                continue
            
            # Procesar query
            console.print("\n[bold green]🤖 Agente:[/bold green]", end=" ")
            console.print("[dim]Analizando...[/dim]", end="\r")
            
            response = agent.process_query(user_input)
            
            console.print("[bold green]🤖 Agente:[/bold green]")
            console.print(Markdown(response))
            
        except KeyboardInterrupt:
            console.print("\n[yellow]¡Hasta luego! 👋[/yellow]")
            break
        except Exception as e:
            logger.error(f"Error: {e}")
            console.print(f"[red]Error: {e}[/red]")


if __name__ == "__main__":
    main()
```

---

## 🧪 Testing Día 3

### Script de prueba:

```python
# agent/test_agent.py
from agent import CICDAgent, MCPClient
import os
from dotenv import load_dotenv

load_dotenv()

# Inicializar
mcp_client = MCPClient("http://localhost:8000")
agent = CICDAgent(os.getenv("GEMINI_API_KEY"), mcp_client)

# Test 1: Consulta simple
print("="*50)
print("TEST 1: ¿Qué pipelines corrieron hoy?")
print("="*50)
response = agent.process_query("¿Qué pipelines corrieron hoy?")
print(response)

# Test 2: Análisis de fallo
print("\n" + "="*50)
print("TEST 2: Analizar fallo")
print("="*50)
# Primero obtener un run fallido
runs = mcp_client.call_tool("list_workflow_runs", status="completed")
failed_runs = [r for r in runs['runs'] if r.get('conclusion') == 'failure']

if failed_runs:
    run_id = failed_runs[0]['id']
    analysis = agent.analyze_failure(run_id)
    print(analysis)
else:
    print("No hay runs fallidos para analizar")
```

---

## ✅ Checklist Día 3

- [ ] `agent/` estructura creada
- [ ] `prompts.py` con system prompt configurado
- [ ] `agent.py` con CICDAgent funcionando
- [ ] Integración con MCP client
- [ ] Gemini inicializando correctamente
- [ ] Test de consulta simple exitoso
- [ ] Test de análisis de fallo exitoso

---

**Continuará...**

Esto es el Día 0-3 del bootcamp. ¿Quieres que continúe con los Días 4-7? Incluyen:
- Día 4: Herramientas avanzadas (trigger, rollback, métricas DORA)
- Día 5: UI con Streamlit
- Día 6: Testing y optimización
- Día 7: Deploy y monitoreo

¿Sigo con el resto del bootcamp?
