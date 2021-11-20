/*!
* This script handles image upload on Add a new recipe page. 
*/

window.addEventListener('DOMContentLoaded', event => {
    // Overwrite the default behavior of bootstrap-filestyle plugin 
    // http://markusslima.github.io/bootstrap-filestyle/
    const fileInputField = $(':file');
    fileInputField.filestyle({
        size: 'lg',
        btnClass: 'btn-warning',
        text: 'Upload',
        'onChange': function (files) {
            const file = files[0];

            // Show Info modal when user tries to upload disallowed file extensions 
            // Similar to the source https://javacodepoint.com/file-upload-validations-in-jquery/
            const fileName = file.name;
            const extension = fileName.substr(fileName.lastIndexOf('.'));
            const allowedExtensions =
                /(\.jpg|\.jpeg|\.png)$/i;
            var isAllowed = allowedExtensions.test(extension);
            if (!isAllowed) {
                updateAndToggleInfoModal('Invalid file type', 'Only files with the following extensions are allowed: jpg, jpeg, png.');
                fileInputField.filestyle('clear');
                return false;
            }

            // Show Info modal when user tries to upload file larger than 4MB 
            // Similar to the source https://www.geeksforgeeks.org/validation-of-file-size-while-uploading-using-javascript-jquery/
            const size = (file.size / 1024 / 1024).toFixed(2);
            if (size > 4) {
                // alert('Maximum upload file size must be 4MB.');
                updateAndToggleInfoModal('File is too large', 'Maximum upload file size must be 4MB.');
                fileInputField.filestyle('clear');
                return false;
            }

            // Show Info modal when user tries to upload images of non-landscape orientation 
            // Similar to the source https://stackoverflow.com/a/41063194/10928662
            var img = new Image();
            img.onload = function () {
                var height = this.height;
                var width = this.width;
                URL.revokeObjectURL(this.src);
                if (height > width || width == height) {
                    updateAndToggleInfoModal('Recommended image orientation', 'To ensure your image display well, we recommend to upload images of ladscape orientation where width is more than height.');
                    return false;
                }
                URL.revokeObjectURL(this.src);
            };
            var objectURL = URL.createObjectURL(file);
            img.src = objectURL;

            // Update the Info modal title and body message and toggle it 
            function updateAndToggleInfoModal(title, message) {
                $('.modal-title').text(title);
                $('.modal-body').text(message);
                $('#informModal').modal('toggle');
            }
        }
    });
});