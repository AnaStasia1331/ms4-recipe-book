/*!
* This script handles image upload on Add a new recipe page. 
*/

window.addEventListener('DOMContentLoaded', event => {
    // Overwrite the default behavior of bootstrap-filestyle plugin 
    // http://markusslima.github.io/bootstrap-filestyle/
    $(':file').filestyle({
        size: 'lg',
        btnClass: 'btn-warning',
        text: 'Upload',
        'onChange': function (files) {
            const file = files[0];

            // Similar to the source https://javacodepoint.com/file-upload-validations-in-jquery/
            const fileName = file.name;
            const extension = fileName.substr(fileName.lastIndexOf("."));
            const allowedExtensions =
                /(\.jpg|\.jpeg|\.png)$/i;
            var isAllowed = allowedExtensions.test(extension);
            if (!isAllowed) {
                alert("Only files with the following extensions are allowed: jpg, jpeg, png.");
                $(":file").filestyle('clear');
                return false;
            }

            // Similar to the source https://www.geeksforgeeks.org/validation-of-file-size-while-uploading-using-javascript-jquery/
            const size = (file.size / 1024 / 1024).toFixed(2);
            if (size > 4) {
                alert("Maximum upload file size must be 4MB.");
                $(":file").filestyle('clear');
                return false;
            }

            // Similar to the source https://stackoverflow.com/a/41063194/10928662
            var img = new Image();
            img.onload = function () {
                var height = this.height;
                var width = this.width;
                URL.revokeObjectURL(this.src);
                if (height > width || width == height) {
                    alert("To ensure your image display well, we recommended to upload images of ladscape orientation where width is more than height.");
                    return false;
                }
                URL.revokeObjectURL(this.src);
            };
            var objectURL = URL.createObjectURL(file);
            img.src = objectURL;
        }
    });
});