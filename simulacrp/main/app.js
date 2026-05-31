import { loginView } from "../vistas/vistalogin.js";

import {
    managerView,
    cargarproyectomanager,
    agregarProyecto
}
from "../vistas/managerview.js";

import {
    collaboratorView,
    cargarProyectos
}
from "../vistas/vistatienda.js";



    const app = document.getElementById("app");
    app.innerHTML = loginView;
    let proyectos = [];



    const contenedorMensaje = document.getElementById("contenedorMensaje");

    const mostrarMensaje = (texto, tipo) => {
        contenedorMensaje.textContent = texto;
        contenedorMensaje.className = `mensaje ${tipo}`;
        contenedorMensaje.style.display = 'block';
        
        // Ocultar el mensaje automáticamente después de 3 segundos
        setTimeout(() => {
            contenedorMensaje.style.display = 'none';
        }, 3000);
    };


    async function login() {
    const email = document.getElementById("emailinput").value;
    const password = document.getElementById("passwordinput").value;
        try {
            const response = await fetch("http://localhost:3000/users")

            if (!response.ok) {
                mostrarMensaje("Error al conectar con el servidor", "error");
                return;
            }

            const data = await response.json();
            
            const user = data.find((user) => user.email === email && user.password === password);

            if (user.role === "manager") {
                renderManager();
            } else if (user.role === "collaborator") {
                renderCollaborator();
            } else {
                mostrarMensaje("Credenciales incorrectas", "error");
            }
    } catch (error) {
        mostrarMensaje("Error al conectar con el servidor", "error");
    }

    };


    const sing = document.querySelector("#init");
    sing.addEventListener("click", (e) => {
        e.preventDefault();
        login();
    });



function renderLogin() {

    app.innerHTML = loginView;

    const form =
        document.querySelector(".login-form");

    form.addEventListener(
        "submit",
        (e) => {
        e.preventDefault();
        login();
    }
);
}


function renderManager() {

    app.innerHTML = managerView;

    cargarProyectoManager();

    document
        .querySelector(".project-form")
        .addEventListener(
            "submit",
            agregarProyecto
        );
}


function renderCollaborator() {

    app.innerHTML = collaboratorView;

    cargarProyectos();

}