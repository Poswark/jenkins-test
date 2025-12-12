# Bootcamp CI/CD: De Cero a Pipeline Productivo

## Entornos On-Premise con Enfoque Práctico

-----

## Información General

|Aspecto             |Detalle                                           |
|--------------------|--------------------------------------------------|
|**Duración**        |14 semanas                                        |
|**Modalidad**       |Teórico-práctico                                  |
|**Nivel**           |Intermedio                                        |
|**Prerrequisitos**  |Conocimientos básicos de Linux, Git y contenedores|
|**Entorno objetivo**|On-premise (RHEL/CentOS/Rocky Linux)              |

-----

## Filosofía del Bootcamp

Este bootcamp está diseñado con un enfoque **progresivo y práctico**. Cada módulo construye sobre el anterior, permitiendo a los participantes desarrollar competencias reales mientras construyen infraestructura funcional.

El objetivo final es que cada participante termine con un pipeline completo end-to-end funcionando en su propio ambiente, con las habilidades necesarias para replicarlo y adaptarlo en entornos productivos.

-----

## Stack Tecnológico

### Control de Versiones

|Herramienta            |Por qué esta herramienta                                                                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**GitLab CE**          |Solución todo-en-uno para on-premise. Incluye CI/CD nativo, registry de contenedores, gestión de proyectos y wiki. Una sola instalación cubre múltiples necesidades, reduciendo complejidad operativa.|
|**Gitea** (alternativa)|Para entornos con recursos limitados. Ligero, rápido de instalar, compatible con la mayoría de integraciones CI/CD.                                                                                   |

### Servidor CI/CD

|Herramienta  |Por qué esta herramienta                                                                                                                                                     |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Jenkins**  |Estándar de la industria en on-premise. Ecosistema masivo de plugins, documentación abundante, flexibilidad total. Ideal para entornos enterprise con requisitos específicos.|
|**GitLab CI**|Si ya usas GitLab, elimina la necesidad de mantener otro servicio. Configuración como código (.gitlab-ci.yml), integración nativa con el repositorio.                        |
|**Drone CI** |Moderno, basado en contenedores desde su diseño. Configuración simple, pipelines aislados, ideal para equipos que prefieren simplicidad sobre flexibilidad extrema.          |

### Containerización

|Herramienta       |Por qué esta herramienta                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------|
|**Docker**        |Estándar de facto. Documentación extensa, compatibilidad universal, curva de aprendizaje accesible.                                     |
|**Docker Compose**|Orquestación simple para desarrollo y testing. Define ambientes multi-contenedor en un solo archivo.                                    |
|**Podman**        |Alternativa rootless, compatible con RHEL y entornos con restricciones de seguridad. Sintaxis compatible con Docker, no requiere daemon.|
|**Buildah**       |Construcción de imágenes sin daemon, integración natural con Podman, mejor para pipelines seguros.                                      |

### Registry Privado

|Herramienta         |Por qué esta herramienta                                                                                                                                                    |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Harbor**          |Registry enterprise-grade open source. Incluye escaneo de vulnerabilidades (Trivy integrado), replicación, políticas de retención, RBAC granular. Proyecto graduado de CNCF.|
|**Nexus Repository**|Si necesitas gestionar más que imágenes (Maven, npm, PyPI). Solución unificada para todos los artefactos.                                                                   |

### Orquestación de Contenedores

|Herramienta     |Por qué esta herramienta                                                                                                                                                  |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**k3s**         |Kubernetes certificado en un solo binario. Ideal para on-premise con recursos limitados, edge computing, o ambientes de desarrollo. Mantiene compatibilidad total con K8s.|
|**RKE2**        |Kubernetes enfocado en seguridad para producción. Cumple con estándares gubernamentales (FIPS, CIS), ideal para entornos enterprise on-premise.                           |
|**Docker Swarm**|Para equipos que necesitan orquestación simple sin la complejidad de Kubernetes. Curva de aprendizaje mínima, integrado en Docker.                                        |

### Gestión de Configuración

|Herramienta        |Por qué esta herramienta                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Ansible**        |Agentless (solo necesita SSH), curva de aprendizaje accesible, playbooks legibles. Ideal para provisioning de servidores y configuración de infraestructura.|
|**HashiCorp Vault**|Gestión de secretos enterprise-grade. Rotación automática, auditoría, integración con K8s y pipelines CI/CD. Evita secretos hardcodeados.                   |

### Calidad de Código

|Herramienta  |Por qué esta herramienta                                                                                                                          |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|**SonarQube**|Análisis estático completo. Detecta bugs, vulnerabilidades, code smells. Quality gates permiten bloquear merges que no cumplan estándares.        |
|**Trivy**    |Escaneo de vulnerabilidades para contenedores, código, y configuración. Rápido, fácil de integrar en pipelines, base de datos de CVEs actualizada.|

### Observabilidad

|Herramienta   |Por qué esta herramienta                                                                                        |
|--------------|----------------------------------------------------------------------------------------------------------------|
|**Prometheus**|Estándar para métricas en entornos cloud-native. Modelo pull, PromQL potente, integración nativa con Kubernetes.|
|**Grafana**   |Visualización flexible. Soporta múltiples datasources, dashboards compartibles, alerting integrado.             |
|**Loki**      |Logs agregados con el mismo modelo de Prometheus. Integración perfecta con Grafana, eficiente en storage.       |
|**ELK Stack** |Para necesidades avanzadas de búsqueda y análisis de logs. Más potente pero más complejo de operar.             |

### GitOps

|Herramienta|Por qué esta herramienta                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------|
|**ArgoCD** |GitOps para Kubernetes. UI intuitiva, sincronización declarativa, rollback automático. El repositorio Git es la fuente de verdad.|
|**Flux**   |Alternativa más ligera a ArgoCD. Mejor para equipos que prefieren gestión via CLI, integración nativa con Helm.                  |

-----

## Temario Detallado

-----

## Módulo 1: Fundamentos de CI/CD

**Duración:** 2 semanas

### Por qué este módulo

Antes de usar herramientas, es crucial entender el problema que resuelven. Muchos equipos implementan CI/CD sin comprender sus principios, resultando en pipelines frágiles y difíciles de mantener. Este módulo establece las bases conceptuales que guiarán todas las decisiones técnicas posteriores.

### Temario

#### Semana 1: Conceptos Core

1. **El problema que resuelve CI/CD**
- El ciclo tradicional de desarrollo y sus cuellos de botella
- Costo del feedback tardío
- Casos de estudio: antes y después de CI/CD
1. **Continuous Integration**
- Definición y principios fundamentales
- Integración frecuente vs. integración tardía
- La importancia de la rama principal siempre funcional
- Métricas: frecuencia de integración, tasa de fallos
1. **Continuous Delivery vs Continuous Deployment**
- Diferencias conceptuales y prácticas
- Cuándo usar cada aproximación
- El rol de las aprobaciones manuales
- Madurez organizacional requerida
1. **El Pipeline como Código**
- Infraestructura reproducible
- Versionado de pipelines
- Code review de cambios en CI/CD
- Ventajas sobre configuración manual

#### Semana 2: Infraestructura Base

1. **Ambientes y Promoción**
- Desarrollo, staging, producción
- Paridad entre ambientes
- Estrategias de promoción de artefactos
- Variables por ambiente
1. **Instalación de GitLab CE**
- Requisitos de hardware para on-premise
- Instalación en RHEL/Rocky Linux
- Configuración inicial y seguridad
- Backup y recuperación
1. **Branching Strategies**
- GitFlow: cuándo usarlo y cuándo no
- Trunk-Based Development
- Feature flags como alternativa a branches largos
- Protected branches y merge requests
1. **GitLab Runners**
- Arquitectura de runners
- Shell vs Docker executor
- Runners compartidos vs específicos
- Tags y selección de runners

### Práctica del Módulo

- Instalación completa de GitLab CE
- Configuración de primer proyecto con CI básico
- Pipeline “Hello World” con múltiples stages
- Configuración de runners con Docker executor

-----

## Módulo 2: Containerización

**Duración:** 2 semanas

### Por qué este módulo

Los contenedores son la unidad fundamental de deployment moderno. Un pipeline CI/CD efectivo produce artefactos consistentes y reproducibles. Dominar la containerización asegura que lo que funciona en desarrollo, funciona en producción. Además, en entornos RHEL, entender Podman es esencial para cumplir con políticas de seguridad.

### Temario

#### Semana 3: Docker en Profundidad

1. **Anatomía de un Dockerfile**
- Instrucciones y su orden óptimo
- Sistema de capas y caché
- Build context y .dockerignore
- ARG vs ENV
1. **Multi-stage Builds**
- Separación de build y runtime
- Reducción drástica de tamaño de imagen
- Patrones comunes por lenguaje
- Builds reproducibles
1. **Optimización de Imágenes**
- Selección de imagen base (distroless, alpine, slim)
- Reducción de capas
- Usuario no-root
- Escaneo de vulnerabilidades básico
1. **Docker Compose para Desarrollo**
- Definición de servicios
- Redes y volúmenes
- Override files para diferentes ambientes
- Health checks

#### Semana 4: Registry y Alternativas

1. **Podman y Buildah**
- Por qué existen (rootless, daemonless)
- Compatibilidad con Docker
- Integración con systemd
- Cuándo preferir Podman sobre Docker
1. **Harbor: Instalación y Configuración**
- Arquitectura de componentes
- Instalación con Docker Compose
- Certificados y HTTPS
- Configuración inicial
1. **Harbor: Gestión Avanzada**
- Proyectos y RBAC
- Políticas de retención
- Escaneo de vulnerabilidades con Trivy
- Replicación entre registries
1. **Pipeline de Imágenes**
- Build automatizado en CI
- Tagging strategies (semver, git sha, latest)
- Push a registry privado
- Promoción de imágenes entre ambientes

### Práctica del Módulo

- Containerizar aplicación multi-servicio (app + base de datos)
- Multi-stage build optimizado
- Instalación de Harbor
- Pipeline: build → scan → push a Harbor

-----

## Módulo 3: Pipeline de Integración Continua

**Duración:** 2 semanas

### Por qué este módulo

Un pipeline CI bien diseñado es la primera línea de defensa contra bugs y problemas de calidad. Este módulo enseña a construir pipelines que den feedback rápido y confiable, permitiendo a los desarrolladores detectar problemas en minutos en lugar de días.

### Temario

#### Semana 5: Estructura del Pipeline

1. **Anatomía de .gitlab-ci.yml**
- Stages y su orden de ejecución
- Jobs: scripts, before_script, after_script
- Artifacts: qué preservar y por cuánto tiempo
- Dependencies entre jobs
1. **Variables y Secretos**
- Variables predefinidas de GitLab
- Variables de proyecto y grupo
- Variables protegidas y enmascaradas
- Integración con Vault (introducción)
1. **Caching Efectivo**
- Qué cachear (dependencias, no código)
- Cache keys y políticas
- Cache vs artifacts
- Troubleshooting de cache
1. **Paralelización**
- Jobs paralelos
- Matrix builds
- Parallel keyword
- Trade-offs: velocidad vs recursos

#### Semana 6: Calidad Automatizada

1. **Testing en Pipeline**
- Unit tests: rápidos y aislados
- Integration tests: cuándo y cómo
- Coverage reports en merge requests
- Test reports en GitLab
1. **Linting y Formateo**
- Linters por lenguaje
- Pre-commit hooks vs CI checks
- Formateo automático
- Fail fast: linting antes de tests
1. **SonarQube**
- Instalación y configuración
- Integración con GitLab CI
- Quality Gates: definición y umbrales
- Análisis de merge requests
1. **Security Scanning**
- SAST: análisis de código estático
- Dependency scanning
- Secret detection
- Interpretación de resultados

### Práctica del Módulo

- Pipeline completo: lint → test → coverage → build → scan → push
- Integración con SonarQube y quality gates
- Configuración de notificaciones (email, Slack, Telegram)
- Dashboard de métricas de pipeline

-----

## Módulo 4: Pipeline de Entrega Continua

**Duración:** 2 semanas

### Por qué este módulo

Construir es solo la mitad del trabajo. Entregar de forma confiable y segura es donde muchos equipos fallan. Este módulo cubre las estrategias y herramientas para llevar código a producción con confianza, incluyendo la gestión segura de secretos y configuración.

### Temario

#### Semana 7: Estrategias de Deployment

1. **Ambientes en GitLab**
- Definición de environments
- URLs dinámicas
- Historial de deployments
- Protected environments
1. **Rolling Updates**
- Concepto y flujo
- Configuración de réplicas
- Health checks durante rollout
- Rollback automático
1. **Blue-Green Deployments**
- Arquitectura y flujo
- Cambio de tráfico instantáneo
- Requisitos de infraestructura
- Cuándo usarlo
1. **Canary Deployments**
- Exposición gradual
- Métricas para decisión
- Promoción y rollback
- Herramientas de soporte

#### Semana 8: Configuración y Secretos

1. **Ansible para Preparación de Servidores**
- Inventarios estáticos y dinámicos
- Playbooks para CI/CD
- Roles reutilizables
- Ansible en pipelines de GitLab
1. **HashiCorp Vault: Fundamentos**
- Arquitectura y conceptos
- Instalación on-premise
- Autenticación y políticas
- Secret engines
1. **Vault en Pipelines**
- JWT auth con GitLab CI
- Inyección de secretos en jobs
- Rotación de credenciales
- Auditoría de acceso
1. **Feature Flags**
- Concepto y beneficios
- Desacoplando deploy de release
- Herramientas open source
- Patrones de uso

### Práctica del Módulo

- Deploy automático a staging en cada merge a develop
- Deploy a producción con aprobación manual
- Integración completa con Vault
- Implementación de feature flag básico

-----

## Módulo 5: Kubernetes On-Premise

**Duración:** 2 semanas

### Por qué este módulo

Kubernetes se ha convertido en el estándar para orquestación de contenedores. Para CI/CD moderno, especialmente en entornos on-premise, dominar K8s es esencial. Este módulo cubre desde la instalación hasta el deployment automatizado, con enfoque en soluciones ligeras adecuadas para on-premise.

### Temario

#### Semana 9: Fundamentos de Kubernetes

1. **Arquitectura de Kubernetes**
- Control plane: API server, scheduler, controller manager, etcd
- Worker nodes: kubelet, kube-proxy, container runtime
- Comunicación entre componentes
- Alta disponibilidad
1. **Objetos Fundamentales**
- Pods: la unidad mínima
- Deployments y ReplicaSets
- Services: ClusterIP, NodePort, LoadBalancer
- ConfigMaps y Secrets
1. **Instalación de k3s**
- Por qué k3s para on-premise
- Instalación de server y agents
- Configuración de kubeconfig
- Verificación del cluster
1. **Networking e Ingress**
- Modelo de networking de K8s
- Ingress controllers (Traefik en k3s)
- Configuración de Ingress resources
- TLS termination

#### Semana 10: Deployment a Kubernetes

1. **Storage en Kubernetes**
- PersistentVolumes y PersistentVolumeClaims
- StorageClasses
- Longhorn para storage distribuido
- NFS como alternativa simple
1. **Helm: Package Manager**
- Estructura de un chart
- Values y templating
- Repositorios de charts
- Creación de charts propios
1. **GitOps con ArgoCD**
- Principios de GitOps
- Instalación de ArgoCD
- Configuración de aplicaciones
- Sync policies y auto-healing
1. **Pipeline hacia Kubernetes**
- Actualización de manifiestos/values
- Trigger de ArgoCD desde CI
- Verificación de deployment
- Rollback automatizado

### Práctica del Módulo

- Cluster k3s de 3 nodos
- Aplicación desplegada con Helm chart propio
- ArgoCD sincronizando desde GitLab
- Pipeline completo: código → imagen → manifest update → sync

-----

## Módulo 6: Observabilidad

**Duración:** 1 semana

### Por qué este módulo

No puedes mejorar lo que no mides. La observabilidad permite detectar problemas antes de que impacten a usuarios, entender el comportamiento del sistema, y tomar decisiones basadas en datos. Un pipeline sin observabilidad es un pipeline ciego.

### Temario

#### Semana 11: Stack de Observabilidad

1. **Prometheus**
- Arquitectura y modelo de datos
- Instalación en Kubernetes
- ServiceMonitors y PodMonitors
- PromQL básico y útil
1. **Grafana**
- Instalación y configuración
- Datasources
- Dashboards para aplicaciones y pipelines
- Alerting: reglas y canales
1. **Logging con Loki**
- Arquitectura y diferencias con ELK
- Instalación con Helm
- Promtail como agente
- LogQL para consultas
1. **Observabilidad del Pipeline**
- Métricas de CI/CD
- Tiempos de build, tasa de éxito
- Alertas de pipeline fallido
- Dashboards de productividad

### Práctica del Módulo

- Stack Prometheus + Grafana + Loki en k3s
- Dashboards para aplicación desplegada
- Métricas de pipelines de GitLab
- Alertas a Telegram/Slack

-----

## Módulo 7: Seguridad y Compliance

**Duración:** 1 semana

### Por qué este módulo

La seguridad no puede ser un afterthought. DevSecOps integra seguridad en cada fase del pipeline. En entornos enterprise on-premise, compliance y auditoría son requisitos no negociables. Este módulo enseña a construir pipelines seguros por diseño.

### Temario

#### Semana 12: DevSecOps

1. **Shift-Left Security**
- Concepto y beneficios
- Costo de bugs en cada fase
- Security as Code
- Cultura de seguridad compartida
1. **Container Security**
- Escaneo de imágenes con Trivy
- Políticas de imágenes permitidas
- Firmado de imágenes con Cosign
- SBOM (Software Bill of Materials)
1. **Kubernetes Security**
- Pod Security Standards
- Network Policies
- OPA Gatekeeper: políticas de admisión
- RBAC granular
1. **Auditoría y Compliance**
- Logs de auditoría en GitLab
- Audit logs en Kubernetes
- Trazabilidad de cambios
- Reportes de compliance

### Práctica del Módulo

- Pipeline con gates de seguridad obligatorios
- Políticas de Gatekeeper bloqueando imágenes inseguras
- Firmado y verificación de imágenes
- Generación de SBOM

-----

## Módulo 8: Automatización Avanzada y Agentes

**Duración:** 2 semanas

### Por qué este módulo

La automatización tradicional es reactiva: el pipeline responde a eventos predefinidos. Los agentes y la IA permiten automatización inteligente: sistemas que analizan, aprenden y actúan. Este módulo explora el futuro de DevOps, donde los agentes complementan los pipelines tradicionales.

### Temario

#### Semana 13: ChatOps y Automatización

1. **ChatOps**
- Concepto y beneficios
- Operaciones desde chat
- Visibilidad y colaboración
- Herramientas: bots personalizados
1. **Bots para CI/CD**
- Notificaciones inteligentes
- Comandos de deployment desde chat
- Aprobaciones via bot
- Integración con Telegram/Slack
1. **Self-Healing Pipelines**
- Detección automática de problemas
- Retry strategies inteligentes
- Auto-rollback basado en métricas
- Alertas predictivas
1. **Event-Driven Automation**
- Pipelines triggeados por eventos externos
- Webhooks y APIs
- Respuesta a alertas de monitoreo
- Integración con sistemas externos

#### Semana 14: Agentes IA para DevOps

1. **Introducción a Agentes**
- Qué es un agente y cómo funciona
- Diferencia con automatización tradicional
- Casos de uso en DevOps
- Limitaciones y consideraciones
1. **MCP (Model Context Protocol)**
- Arquitectura de MCP
- Servidores y herramientas
- Integración con pipelines
- Ejemplos prácticos
1. **Agente Analizador de Logs**
- Análisis de errores de pipeline
- Sugerencia de causas raíz
- Recomendaciones de fix
- Aprendizaje de patrones
1. **Agente de Documentación**
- Generación automática de changelogs
- Documentación de deployments
- Resúmenes de releases
- Integración con wikis

### Práctica del Módulo

- Bot de Telegram para reportes y comandos de CI/CD
- Prototipo de agente MCP para análisis de pipeline
- Agente que analiza logs de error y sugiere soluciones
- Demo de documentación automática de releases

-----

## Proyecto Final

**Duración:** Integrado en las últimas semanas

### Descripción

Cada participante construirá un pipeline completo end-to-end para una aplicación real, demostrando dominio de todos los conceptos del bootcamp.

### Requisitos

1. **Repositorio**
- Código en GitLab con branching strategy documentada
- README completo
- Contributing guidelines
1. **Pipeline CI**
- Lint, test, coverage
- Análisis con SonarQube
- Build de imagen multi-stage
- Escaneo de seguridad
1. **Registry**
- Imagen en Harbor
- Políticas de retención
- Escaneo de vulnerabilidades
1. **Pipeline CD**
- Deploy a staging automático
- Deploy a producción con aprobación
- Secretos desde Vault
1. **Kubernetes**
- Helm chart propio
- GitOps con ArgoCD
- Ingress configurado
1. **Observabilidad**
- Dashboard de aplicación
- Dashboard de pipeline
- Alertas configuradas
1. **Seguridad**
- Quality gates que bloquean merges
- Políticas de Gatekeeper
- Imagen firmada
1. **Documentación**
- Arquitectura del pipeline
- Runbook de operaciones
- Guía de troubleshooting

### Evaluación

|Criterio                          |Peso|
|----------------------------------|----|
|Pipeline funcional end-to-end     |30% |
|Calidad del código y configuración|20% |
|Seguridad implementada            |15% |
|Observabilidad                    |15% |
|Documentación                     |10% |
|Presentación y demo               |10% |

-----

## Recursos Adicionales

### Documentación Oficial

- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Helm Documentation](https://helm.sh/docs/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [Prometheus Documentation](https://prometheus.io/docs/)
- [HashiCorp Vault Documentation](https://developer.hashicorp.com/vault/docs)

### Libros Recomendados

- “The DevOps Handbook” - Gene Kim, Jez Humble, Patrick Debois
- “Continuous Delivery” - Jez Humble, David Farley
- “Kubernetes Up & Running” - Brendan Burns, Joe Beda, Kelsey Hightower
- “GitOps and Kubernetes” - Billy Yuen, Alexander Matyushentsev

### Certificaciones Relacionadas

- GitLab Certified CI/CD Associate
- Certified Kubernetes Administrator (CKA)
- HashiCorp Certified: Vault Associate

-----

## Sobre el Bootcamp

Este bootcamp está diseñado para profesionales DevOps que buscan dominar CI/CD en entornos on-premise, combinando prácticas tradicionales con automatización inteligente mediante agentes IA.

-----

## Licencia

Este material está disponible bajo licencia Creative Commons Attribution 4.0 International (CC BY 4.0).

-----

*Última actualización: Diciembre 2024*