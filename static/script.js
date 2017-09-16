$(function() {
var submit_form = function(e) {
  $.getJSON($SCRIPT_ROOT + '/_get_tweet', {
    handle: $('input[name="handle"]').val(),
  }, function(data) {
    $('#result').text(data.result);
    $('input[name=handle]').focus().select();
  });
  return false;
};
$('a#tweetButton').bind('click', submit_form);
$('input[type=text]').bind('keydown', function(e) {
  if (e.keyCode == 13) {
    submit_form(e);
  }
});
$('input[name=handle]').focus();
});
