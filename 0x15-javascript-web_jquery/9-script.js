$.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: (translation) => {
      $('DIV#hello').text(translation.hello);
    }
  });