/*!
* Start Bootstrap - Modern Business v5.0.7 (https://startbootstrap.com/template-overviews/modern-business)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

// Agrega un evento de clic a la imagen
const imagenContainer = document.querySelector('.imagen-container');
imagenContainer.addEventListener('click', function() {
    // Alternar la clase 'clicked' para agrandar o reducir la imagen
    this.classList.toggle('clicked');
});
