$(() => {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
      if (status === 'success') {
        const movies = data.results;
        for (const i in movies) {
          $('#list_movies').append('<li>' + movies[i].title + '</li>');
        }
      }
    });
  });