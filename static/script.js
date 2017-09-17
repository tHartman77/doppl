$(function() {
var submit_form = function(e){ 
  $.getJSON($SCRIPT_ROOT + '/_get_tweet', {
    handle: $('input[name="handle"]').val(),
  }, function(data) {
    make_tweet_ui(data.result);
    //$('#result').text(data.result);
    $('input[name=handle]').focus().select();
  });
  return false;
};
$('#tweetButton').bind('click', submit_form);
$('input[type=text]').bind('keydown', function(e) {
  if (e.keyCode == 13) {
    submit_form(e);
  }
});
$('input[name=handle]').focus();

function make_tweet_ui(tweet_text) {
    console.log("hi");
    twttr.widgets.createTweet(
      
      // Replace this with the Tweet ID
      '909191177810915328', document.getElementById("tweet"))
      .then(function(el) {

        var e = el.contentDocument;

        // Change the tweet text
        var html = e.querySelector(".Tweet-text");
        html.innerHTML = tweet_text;

        
    });
}
});


