$(function() {
  if(window.CCPEVE) {
    var trustSwitch = $('.trust-switch .switch');
    if(window.antitrust.trusted)
      trustSwitch.switchbtn('toggle');
    trustSwitch.change(function(active) {
      if(active) {
        CCPEVE.requestTrust(window.antitrust.base_uri);
      }
    });
  }
});
