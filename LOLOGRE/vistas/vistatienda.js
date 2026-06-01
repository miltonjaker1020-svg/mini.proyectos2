
export const collaboratorView = `
    <header>
    <nav>
        <ul><button id="logout">Salir</button></ul>
    </nav>
    </header>
    <h1>Proyectos</h1>
    <h2>Bienvenido a la sección de proyectos</h2>
    <h3>Proyectos disponibles</h3>
    <ul>
        
        
    </ul>
`;

export async function cargarProyectos() {

    try {
        const response = await fetch("http://localhost:3000/projects");
        if (!response.ok) {
            console.error("Error al cargar los proyectos");
            return;
        }


        
        const proyectos = await response.json();
        const listaProyectos = document.querySelector("ul");
        const proyectosAsignados = proyectos.filter((proyecto) => proyecto.assignedTo == 2);

        if (proyectosAsignados.length === 0) {
            console.log("No hay proyectos asignados");
            return;
        }
    

        
        proyectosAsignados.forEach(proyecto => {

    const li = document.createElement("li");

    li.textContent =
    `${proyecto.name}: ${proyecto.description}`;

    const select = document.createElement("select");

    select.innerHTML = `
        <option value="In Progress">In Progress</option>
        <option value="Completed">Completed</option>
        <option value="Archived">Archived</option>
    `;

    select.value = proyecto.status;
    const btnGuardar = document.createElement("button");
    btnGuardar.textContent = "Actualizar";
    btnGuardar.addEventListener("click", async () => {
        
        await actualizarEstado(
            proyecto.id,
            select.value
        );

        alert("Estado actualizado");
    });

    li.appendChild(select);
    li.appendChild(btnGuardar);
    listaProyectos.appendChild(li);

});
    } catch (error) {
        console.error("Error al conectar con el servidor", error);
    }
}



export async function actualizarEstado(idProyecto, nuevoEstado) {

    try {

        const response = await fetch(
            `http://localhost:3000/projects/${idProyecto}`,
            {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    status: nuevoEstado
                })
            }
        );

        if (!response.ok) {
            console.error("Error al actualizar estado");
            return;
        }

        const proyectoActualizado = await response.json();

        console.log(
            "Proyecto actualizado:",
            proyectoActualizado
        );

    } catch(error) {
        console.error(
            "Error al conectar con el servidor",
            error
        );
    }
}


