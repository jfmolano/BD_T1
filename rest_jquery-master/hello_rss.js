$(document).ready(function() {

    $("#Suma").click(function(){
	var A = $('#txt_A').val();
	console.log("A " + A)
        url_get = "http://localhost:5000/api/rss/"+A
	trHTML = ''
        console.log(url_get)
        $('#resultado_text').text('');
        $.ajax({
	type: "GET",
        url: url_get
        }).then(function(data) {
            console.log("data: ")
            console.log(data)
		$.each(data, function (i, item) {
        	console.log(i)
        	console.log(item)
        trHTML += '<div>' + item["titulo"] + '</div>';
    });
    $('#resultado_text').append(trHTML);
    });
    });
});
