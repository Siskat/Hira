function callback(response) {
   var dictionary = {};
   for (var i = 0; i < response.length; i++) {
       dictionary[response[i].full_name] = null;
    }

  $('input').autocomplete({
      data:dictionary,
    });
}
function queryPatients() {
  var resultList;

  $.getJSON("/getAllPatients", {

  }, function(response) {
    resultList = response;
    callback(resultList)
  });



  return [];
}

$(function () {
  var counter = 0;

  $("#plus").click(function () {
    counter++;
    $("#count").text(counter);
  });

  $("#minus").click(function () {
    counter--;
    $("#count").text(counter);
  });

  $(document).ready(function(){
      // the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
      $('.modal-trigger').leanModal();
  });

});



$(document).ready(function() {
  var patientData = queryPatients();




		});
