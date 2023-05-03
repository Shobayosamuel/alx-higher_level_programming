$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#btn_translate, INPUT#language_code').on('click keyup', function (e) {
    if (e.type === 'click' || (e.type === 'keyup' && e.keyCode === 13)) {
      $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
        $('DIV#hello').html(data.hello);
      });
    }
  });
});
