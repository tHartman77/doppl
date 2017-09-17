$(function() {
var submit_form = function(e){ 
  $.getJSON($SCRIPT_ROOT + '/_get_tweet', {
    handle: $('input[name="handle"]').val(),
  }, function(data) {
    var markov_tweet = data.result;
    var rand_id = data.id;
    console.log(data.id);
    make_tweet_ui(markov_tweet, rand_id);
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

function make_tweet_ui(tweet_text, tweet_id) {
    twttr.widgets.createTweet( 
      // Replace this with the Tweet ID
      tweet_id, document.getElementById("tweet"))
      .then(function(el) {

        var e = el.contentDocument;

        // Change the tweet text
        var html = e.querySelector(".Tweet-text");
        
        e.querySelector(".MediaCard-media").style.display = "none";        

        html.innerHTML = tweet_text;
    });
}
});
