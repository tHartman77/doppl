$(function() {
   
var submit_form = function(e){ 
  $.getJSON($SCRIPT_ROOT + '/_get_tweet', {
    handle: $('input[name="handle"]').val(),
  }, function(data) {
  var markov_tweet = data.result;
  var rand_id = data.rand_id;  
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

function pick_random_user()
{
  var users = ['katyperry','justinbieber','realDonaldTrump','BarackObama','rihanna','TheEllenShow','ladygaga','jtimberlake','Cristiano','KimKardashian','britneyspears','selenagomez','ArianaGrande','jimmyfallon'];
  var user = users[Math.floor(Math.random() * users.length)];
  $('#tweetlabel').html("<label>" + user + "</label>");
}
function make_tweet_ui(tweet_text, rand_id) {
    twttr.ready(function(){
    var id = Math.floor(Math.random() * 500);
    $("#tweet").prepend("<div id=" + id + "></div>");
    twttr.widgets.createTweet(
      // Replace this with the Tweet ID
      rand_id, document.getElementById("" + id),
      {
        conversation: 'none',
        cards: 'hidden',
      }).then(function(el) {
        
        var e = el.contentDocument;

        // Change the tweet text
        var html = e.querySelector(".Tweet-text");
        html.innerHTML = tweet_text;
        
    });
});
}
pick_random_user();

});

