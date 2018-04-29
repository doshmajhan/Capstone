
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
            $("#exampleFormControlSelect2").empty();
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
            alert("Succesfully built!");
        },
        error: function(data) {
            alert("Build did not complete: "+data.responseJSON.description);
        }
    });

    // TODO: Do something with response
    return response;
}

function destroy(machine) {
    var data = {}
    var tr = machine.closest('tr');
    var tds = tr.getElementsByTagName('td');
    for(i = 0; i < tds.length; i++){
        data[tds[i].className] = tds[i].innerHTML;
    }

    console.log(data)
    var response;
    $.ajax({
        type: "POST",
        url: "/api/destroy",
        data:  JSON.stringify(data),
        contentType: 'application/json',
        success: function(data) {
            response = data;
            alert("Succesfully destroyed!");
        },
        error: function(data) {
            alert("Destroy did not complete: "+data.responseJSON.description);
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

function running_machines() {
    $.getJSON("/api/running_machines", function(data){
        console.log(data.machines)
        $('#vm-table tbody').empty();
        $.each(data.machines, function(i, machine) {
            console.log(machine.name)
            
            var tr = ($('<tr>')
                .append($('<td>').addClass("name").append(machine.name))
                .append($('<td>').addClass("os").append(machine.os))
                .append($('<td>').append(machine.ip))
                .append($('<td>').append(machine.ports))
                .append($('<td>').append("UP"))
            );

            var button = $('<button type="button" class="btn btn-primary" onclick="destroy(this)">Destroy</button>')
            tr.append(button);
            $('#vm-table tbody').append(tr);
        });
    })
    return;
}


var poll = setInterval(running_machines, 15000);

os_list();
running_machines();