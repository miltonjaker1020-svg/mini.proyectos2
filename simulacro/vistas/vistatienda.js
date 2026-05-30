
export const proyectosView = `
    <h1>Proyectos</h1>
    <h2>Bienvenido a la sección de proyectos</h2>
    <h3>Proyectos disponibles</h3>
    <form class="project-form hidden" action="">
    <input type="text" id="projectName" placeholder="Nombre del proyecto" required>
    <input type="text" id="projectDescription" placeholder="Descripción del proyecto" required>
    <select id="projectStatus">
        <option value="active">Activo</option>
        <option value="completed">Completado</option>
        <option value="archived">Archivado</option>
    </select>
    <button id="addProject" type="submit">Agregar Proyecto</button>
    </form>
    <ul>
        
        
    </ul>
`;

async function agregarProyecto(event) {
    event.preventDefault();
    
    const name = document.getElementById("projectName").value;
    const description = document.getElementById("projectDescription").value;
    const status = document.getElementById("projectStatus").value;

    try {
        const response = await fetch("http://localhost:3000/projects", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name, description, status })
        });

        if (!response.ok) {
            console.error("Error al agregar el proyecto");
            return;
        }

        const nuevoProyecto = await response.json();
        const listaProyectos = document.querySelector("ul");
        const li = document.createElement("li");
        li.id = `prod-${producto.id}`;
        li.textContent = nuevoProyecto.name + 
        ": " + nuevoProyecto.description 
        + " (Estado: " + nuevoProyecto.status + ")";

        listaProyectos.appendChild(li);
































async function cargarProyectos() {

    try {
        const response = await fetch("http://localhost:3000/projects");
        if (!response.ok) {
            console.error("Error al cargar los proyectos");
            return;
        }


        
        const proyectos = await response.json();
        const listaProyectos = document.querySelector("ul");
        proyectos.forEach(proyecto => {
        
            const li = document.createElement("li");
            li.textContent = proyecto.name + 
            ": " + proyecto.description 
            + " (Estado: " + proyecto.status + ")";

            listaProyectos.appendChild(li);
        });
    } catch (error) {
        console.error("Error al conectar con el servidor", error);
    }
}

cargarProyectos();









/* Función para cargar colaboradores
async function cargarcollab() { 
    try {
        const response = await fetch("http://localhost:3000/users");
        if (!response.ok) {
            console.error("Error al cargar los colaboradores");
            return;
        }
        
        const colaboradores = await response.json();
        const listaColaboradores = document.querySelector("ul");
        colaboradores.forEach(colaborador => {
        
            const li = document.createElement("li");
            li.textContent = colaborador.name + 
            ": " + colaborador.email 
            + " (Rol: " + colaborador.role + ")";

            listaColaboradores.appendChild(li);
        });
    } catch (error) {
        console.error("Error al conectar con el servidor", error);
    }
}
cargarcollab();
*/