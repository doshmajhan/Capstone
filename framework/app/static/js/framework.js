
function get_role(role_title) {
    var response;
    $.ajax({
        type: "GET",
        url: window.location.hostname + "/api/get_role/" + role_title,
        function(data) {
            response = jQuery.parseJSON(data);
        }
    });

    // TODO: Do something with response
    return response;
}

function verify(config) {
    var response;
    $.ajax({
        type: "POST",
        url: window.location.hostname + "/api/verify",
        data: JSON.stringify(config),
        contentType: 'application/json',
        function(data) {
            response = jQuery.parseJSON(data);
        }
    });

    // TODO: Do something with response
    return response;
}

function os_list() {
    var response;
    $.ajax({
        type: "GET",
        url: window.location.hostname + "/api/os_list",
        function(data) {
            response = jQuery.parseJSON(data);
        }
    });

     // TODO: Do something with response
     return response;
}

function build(config) {
    var response;
    $.ajax({
        type: "POST",
        url: window.location.hostname + "/api/build",
        data: JSON.stringify(config),
        contentType: 'application/json',
        function(data) {
            response = jQuery.parseJSON(data);
        }
    });

    // TODO: Do something with response
    return response;
}