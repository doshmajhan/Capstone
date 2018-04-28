
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

function verify(option_data) {
    var response;

    $.ajax({
        type: "POST",
        url: "/api/verify",
        data: JSON.stringify(option_data),
        contentType: 'application/json',
        success: function(data) {
            response = data;
            // Clear the menu
            $("#exampleFormControlSelect2").empty();
            //$("#vuln").reset();
            $.each(data.additional_roles, function(i, option) {
                $('#exampleFormControlSelect2').append($('<option/>').attr("value", option).text(option));
             });
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

function build() {
    var os_values = $('#exampleFormControlSelect1').val();
    var vuln_values = $('#exampleFormControlSelect2').val();
    var data = {'selected_os': os_values, 'selected_roles': vuln_values}
    
    console.log(data);

    var response;
    $.ajax({
        type: "POST",
        url: "/api/build",
        data:  JSON.stringify(data),
        contentType: 'application/json',
        success: function(data) {
            response = data;
            console.log(data.responseJSON.description);
            alert("Succesfully built!");
        },
        error: function(data) {
            alert("Build did not complete: "+data.responseJSON.description);
        }
    });

    // TODO: Do something with response
    return response;
}

function picked_os(option){
    var data = {'selected_os': option};
    console.log(data)
    verify(data); 
}


os_list();