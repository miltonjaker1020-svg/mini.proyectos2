
export const managerView  = `
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
    <select id="assignedTo">
        <option value="1">Manager</option>
        <option value="2">Collaborator</option>
    </select>
    <button id="addProject" type="submit">Agregar Proyecto</button>
    </form>
    <ul>
        
        
    </ul>
`;







export async function cargarproyectomanager() {

    try {
        const response = await fetch("http://localhost:3000/projects");
        if (!response.ok) {
            console.error("Error al cargar los proyectos");
            return;
        }


        
        const proyectos = await response.json();
        const listaProyectos = document.querySelector("ul");

        
        proyectos.forEach(proyecto => {
        
        
        console.log("Proyecto encontrado:", proyecto);
        const li = document.createElement("li");
        const contenedorBotones = document.createElement('div');
        const button = document.createElement("button");

        button.textContent = "Eliminar";
        button.addEventListener("click", async () => {

        const confirmar = confirm(
            "¿Seguro que deseas eliminar este proyecto?"
        );
        
        if (!confirmar) return;
        await eliminarProyecto(proyecto.id);
        li.remove();
});

        const editButton = document.createElement("button");
        editButton.textContent = "Editar";
        contenedorBotones.appendChild(button);
        editButton.addEventListener("click", () => {
            editar(proyecto);
        });
        
        const texto = document.createElement("span");
        texto.textContent =
        `${proyecto.name}: ${proyecto.description} (Estado: ${proyecto.status})`;

        li.appendChild(texto);
        li.appendChild(editButton);
        li.appendChild(button);
        listaProyectos.appendChild(li);
        
        
        });
    } catch (error) {
        console.error("Error al conectar con el servidor", error);
    }
}
















export async function agregarProyecto(event) {
    event.preventDefault();
    
    const id = document.getElementById("assignedTo").value;
    const name = document.getElementById("projectName").value;
    const description = document.getElementById("projectDescription").value;
    const status = document.getElementById("projectStatus").value;

    try {
        const response = await fetch("http://localhost:3000/projects", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name, description, status , assignedTo: id})
        });

        if (!response.ok) {
            console.error("Error al agregar el proyecto");
            return;
        }

        const nuevoProyecto = await response.json();
        const listaProyectos = document.querySelector("ul");
        const li = document.createElement("li");
        li.id = `prod-${nuevoProyecto.id}`;
        li.textContent = nuevoProyecto.name + 
        ": " + nuevoProyecto.description 
        + " (Estado: " + nuevoProyecto.status + ")";

        listaProyectos.appendChild(li);

    } catch (error) {
        console.error("Error al conectar con el servidor", error);
    }
}




export async function editar(proyecto) {

    const nuevoNombre = prompt(
        "Nuevo nombre:",
        proyecto.name
    );

    const nuevaDescripcion = prompt(
        "Nueva descripción:",
        proyecto.description
    );

    const nuevoEstado = prompt(
        "Nuevo estado:",
        proyecto.status
    );

    try {

        const response = await fetch(
            `http://localhost:3000/projects/${proyecto.id}`,
            {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    name: nuevoNombre,
                    description: nuevaDescripcion,
                    status: nuevoEstado,
                    assignedTo: proyecto.assignedTo
                })
            }
        );

        if (!response.ok) {
            console.error("Error al editar");
            return;
        }

        alert("Proyecto actualizado");

        location.reload();
        

    } catch(error) {
        console.error(error);
    }
}


export async function eliminarProyecto(id) {

    try {

        const response = await fetch(
            `http://localhost:3000/projects/${id}`,
            {
                method: "DELETE"
            }
        );

        if (!response.ok) {
            throw new Error("No se pudo eliminar");
        }

        console.log("Proyecto eliminado");

    } catch(error) {
        console.error(error);
    }
}