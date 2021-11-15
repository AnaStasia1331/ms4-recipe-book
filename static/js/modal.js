/*!
* This script handles the modal window popping up automatically after user created 3 recipes 
* and tries to add a new one. 
*/

$(document).ready(function(){
    // prevent modal closing by pressing escape or clicking outside
    $("#checkoutModal").modal({
        backdrop: 'static',
        keyboard: false
    });
    // open the modal window automatically
    $('#checkoutModal').modal('toggle')
});

