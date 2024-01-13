$(function(){
    $.ajax({
        type: "GET",
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        success: function(films){
            var film = ('success', films.results)
            $.each(film, function(i, output){
                $("#list_movies").append('<li>'+output.title+'</li>')
            })
            
            
        }
    })
})
