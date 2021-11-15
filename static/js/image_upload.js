/*!
* This script handles image upload on Add a new recipe page. 
*/

window.addEventListener('DOMContentLoaded', event => {
    // Overwrite the default attributes of filestyle() in bootstrap-filestyle plugin 
    $('#id_image').filestyle({
        size : 'lg',
        btnClass: 'btn-warning',
        text: 'Upload'
    });
});

    