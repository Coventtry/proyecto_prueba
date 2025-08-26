🟢 CRUD sugerido: Gestión de Materias
📋 Campos de la entidad Materia:
id (generado automáticamente)

nombre

docente (nombre del docente a cargo)

año (ej: 1°, 2°, 3°)

🔄 Operaciones CRUD:
Crear materia → POST /materias

Listar materias → GET /materias

Editar materia → PUT /materias/:id

Eliminar materia → DELETE /materias/:id

🧱 Stack propuesto (simple y educativo):
Backend: FastAPI (Python) o Flask si querés que sea aún más directo.

Base de datos: MongoDB

Frontend (opcional): Vue.js, o solo Postman para pruebas.