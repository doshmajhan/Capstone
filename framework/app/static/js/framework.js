
function get_role(role_title) {
    var response;
    $.ajax({
        type: "GET",
        url: "/api/get_role/" + role_title,
        function(data) {
            response = jQuery.parseJSON(data);
        }
    });

    // TODO: Do something with response
    return response;
}

function verify() {
    var response;
    config = [].forEach.call(  document.querySelectorAll('#os :checked')  , function(elm){
        console.log(elm.value);
    });

    $.ajax({
        type: "POST",
        url: "/api/verify",
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
    $.getJSON("/api/os_list", function(data){
        $.each(data.operating_systems, function(i, option) {
           $('#exampleFormControlSelect1').append($('<option/>').attr("value", option).text(option));
        });
    })
     return;
}

function build(config) {
    var response;
    $.ajax({
        type: "POST",
        url: "/api/build",
        data: JSON.stringify(config),
        contentType: 'application/json',
        function(data) {
            response = jQuery.parseJSON(data);
        }
    });

    // TODO: Do something with response
    return response;
}

function picked_os(){
    console.log("HI");
    return;
}
os_list();