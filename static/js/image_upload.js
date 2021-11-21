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

            if (isExtensionNotAllowed(file)) {
                return false;
            } 

            if (isFileSizeTooLarge(file)) {
                return false;
            }

            if (isInvalidImgOrientation(file)) {
                return false;
            }
        
            // Update the Info modal title, body message, button name and toggle it 
            function updateAndToggleInfoModal(title, message, buttonName) {
                $('.modal-title').text(title);
                $('.modal-body').text(message);
                $('.modal-footer > button').text(buttonName);
                $('#informModal').modal('toggle');
            }

            function isExtensionNotAllowed(file) {
                // Show Info modal when user tries to upload disallowed file extensions 
                // Similar to the source https://javacodepoint.com/file-upload-validations-in-jquery/
                const fileName = file.name;
                const extension = fileName.substr(fileName.lastIndexOf('.'));
                const allowedExtensions =
                    /(\.jpg|\.jpeg|\.png)$/i;
                var isAllowed = allowedExtensions.test(extension);
                if (isAllowed) {
                    return false;
                } else {
                    updateAndToggleInfoModal('Invalid file type', 'Only files with the following extensions are allowed: jpg, jpeg, png.', 'Close');
                    fileInputField.filestyle('clear');
                    return true;
                }
            }

            function isFileSizeTooLarge(file) {
                // Show Info modal when user tries to upload file larger than 4MB 
                // Similar to the source https://www.geeksforgeeks.org/validation-of-file-size-while-uploading-using-javascript-jquery/
                const size = (file.size / 1024 / 1024).toFixed(2);
                const maxSizeMb = 4;
                if (size > maxSizeMb) {
                    updateAndToggleInfoModal('File is too large', 'Maximum file size must be 4MB.', 'Close');
                    fileInputField.filestyle('clear');
                    return true;
                } else {
                    return false;
                }
            }

            function isInvalidImgOrientation(file) {
                // Show Info modal when user tries to upload images of non-landscape orientation 
                // Similar to the source https://stackoverflow.com/a/41063194/10928662
                const img = new Image();
                img.onload = function () {
                    const height = this.height;
                    const width = this.width;
                    URL.revokeObjectURL(this.src);
                    if (height > width || width == height) {
                        updateAndToggleInfoModal('Recommended image orientation',
                            'To ensure your image is best displayed we recommend uploading images in a landscape orientation.',
                            'Okay');
                        return true;
                    }
                    URL.revokeObjectURL(this.src);
                    return false;
                };
                var objectURL = URL.createObjectURL(file);
                img.src = objectURL;
            }
        }
    });
});