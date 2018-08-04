
	function queryPatients() {
		$.getJSON("/getAllPatients", {
			
		}, function(response) {	
			console.log(response);		
			var html = "<li class='collection-item' id='{0}'>"
			+"{0} <a href='#' id='removeLocation' class='secondary-content'><i class='material-icons'>remove_circle</i></a></li>"
		}

	}
	$(document).ready(function() {
		$(".button-collapse").sideNav();
		$('select').material_select();
		$('.modal').modal();

	queryPatients();
	$('input.auto-search').autocomplete({
      data: {
        "Dummys Guide to Programming": null,
        "A Primer to C++": null,
        "Design Patterns in Making": null,
        "Memory Management": null
      },
    });

		$('#join_session').on('click', function(event) {
			var session_id = document.getElementById("session_id").value;
			window.location.replace(session_id);

		});

		$('#commit_book').on('click', function(event) {
			var book_name = document.getElementById("book_name").value;
			var author = document.getElementById("author").value;
			var price = document.getElementById("price").value;
			// var subject = document.getElementById("autocomplete-input").value;
			// var condition = document.getElementById("book_det").value;
			$.getJSON("/commitBook", {
				book_name: book_name,
				author: author,
				price: price,
				// subject: subject,
				// condition: condition,
			}, function(response) {
				console.log("Logged");
				window.location.href = response.redirect;

			});

		});

