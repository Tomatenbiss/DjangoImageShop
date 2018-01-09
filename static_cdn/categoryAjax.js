function addToList(response, property) {
    $('#categoryList').append('<li class="list-group-item d-flex justify-content-between align-items-center">' + response[property] + '</li>');
}

function addError(errorResponse) {
    for (var field in errorResponse) {
        var errorList = "";
        for (var error in errorResponse[field]) {
            errorList += '<li>' + errorResponse[field][error] + '</li>';
        }
        $('#' + field + '_errorList').html('<ul>' + errorList + '</ul>');
    }
}

function deleteErrors() {
    $('*[id$=errorList]').html('');
}

$(function () {
    $('#categoryForm').on('submit', function (event) {
        event.preventDefault();
        deleteErrors();
        // send ajax request
        $.ajax({
            url: "/photos/categories/add/",
            method: "POST",
            data: $('#categoryForm').serializeArray()
        }).done(function (data) {
            addToList(data, 'name');
        }).fail(function (data) {
            addError(data.responseJSON);
        })
    })

    /*
    Security - Send the CSRF Token with every request 
    as per: https://github.com/realpython/django-form-fun/blob/master/part1/main.js
    */

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});