$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('INPUT#btn_translate').click(function () {
    const langCode = $('INPUT#language_code').val();
    if (langCode !== '') {
      $.get(url, { lang: langCode }, function (data) {
        $('DIV#hello').html(data.hello);
      });
    }
  });
});
