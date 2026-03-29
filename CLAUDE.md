# AGENTIC RULES — FC Global Group Landing

## SCOPE DE ARCHIVOS (Patrón 34)
- Solo editar archivos dentro del directorio especificado en la tarea
- NUNCA tocar: `.env`, `docker-compose.yml`, archivos de config de Caddy/PostgreSQL
- Si la tarea no especifica ruta → preguntar antes de actuar

## ESTADO DE INICIO Y FIN (Patrones 31-32)
- Antes de ejecutar: confirmar estado inicial (estructura de archivos, workflows existentes)
- Definir estado objetivo exacto: qué archivos/workflows deben existir al terminar
- No asumir nada sobre lo que ya está creado

## CHECKPOINTS OBLIGATORIOS (Patrón 33)
- Después de cada paso completado: `✅ [qué se completó]`
- Al finalizar: resumen completo de cada archivo/workflow modificado

## TRIGGERS DE PAUSA — PEDIR REVISIÓN HUMANA (Patrón 35)
Detener y pedir aprobación antes de:
- Eliminar cualquier archivo o workflow
- Agregar una dependencia nueva (npm package, nodo n8n externo, credencial)
- Integrar un servicio externo no mencionado en la tarea
- Cuando existen dos caminos de implementación válidos que afectan la arquitectura
- Un error no se resuelve en 2 intentos
- La tarea requiere cambios fuera del scope declarado

## ACCIONES PROHIBIDAS POR DEFAULT (Patrón 4)
- NO hacer `git push` sin instrucción explícita
- NO reiniciar servicios Docker sin instrucción explícita
- NO modificar variables de entorno sin instrucción explícita
- NO tomar decisiones de arquitectura unilateralmente

---

## TEMPLATES DE REFERENCIA

### TEMPLATE H — Agente Autónomo (Claude Code / n8n workflows)
```
Objetivo: [meta en una sola oración]
Estado inicial: [estructura actual de archivos o workflows]
Estado objetivo: [qué debe existir al terminar]
Acciones permitidas:
  - [acción específica]
Acciones prohibidas:
  - NO modificar archivos fuera de [directorio]
  - NO hacer deploy ni push a git
Condiciones de pausa:
  - Archivo a eliminar → pausar
  - Nueva dependencia → pausar
  - Error en 2 intentos → pausar
Checkpoints: después de cada paso → ✅ [qué se completó]
```

### TEMPLATE G — Edición de Archivo Específico
```
Archivo: [ruta/exacta/al/archivo]
Función/Componente: [nombre exacto]
Comportamiento actual: [qué hace ahora]
Cambio deseado: [qué debe hacer después]
Scope: solo modificar [función/sección]
NO tocar: [lista de lo que no debe cambiar]
Constraints: [versión, sin dependencias nuevas, preservar nombres]
Listo cuando: [condición exacta que confirma que funcionó]
```

### TEMPLATE F — Few-Shot (formato difícil de describir)
```
[Instrucción de tarea]

Ejemplos del formato exacto:
<examples>
  <example>
    <input>[ejemplo input 1]</input>
    <o>[ejemplo output 1]</o>
  </example>
  <example>
    <input>[ejemplo input 2]</input>
    <o>[ejemplo output 2]</o>
  </example>
</examples>

Aplicar este patrón a: [input real]
```
Regla: si re-prompteaste 2 veces por el mismo error de formato → cambiar a few-shot.

### TEMPLATE L — Deconstruir / Adaptar Prompt Existente
```
Prompt original: [pegar]

Análisis:
- Rol/Identidad: [qué rol tiene asignado y por qué]
- Tarea: [qué acción se pide]
- Constraints: [qué límites hay]
- Formato: [qué output se espera]
- Debilidades: [qué falta o puede causar output incorrecto]

Fix recomendado: [versión reescrita]
```
