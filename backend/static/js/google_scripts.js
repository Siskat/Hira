	var map;
	var infowindow;
	var bounds;

	function initMap(convergence) {
		addUsersToMap(js_session);
        var convergence  = {lat: latitude, lng: longitude};
		// var convergence  = {lat: latitude , lng: longitude};
		map = new google.maps.Map(document.getElementById('map'), {
			center: convergence ,
			zoom: 15
		});

		background_map = new google.maps.Map(document.getElementById('background-map'), {
			center: convergence ,
			zoom: 15
		});

		infowindow = new google.maps.InfoWindow();
		var service = new google.maps.places.PlacesService(map);
		service.nearbySearch({
			location: convergence ,
			radius: 1000,
			type: place_type
		}, callback);

	}

	//Gets all user locations in a session and adds person marker to the map
	function addUsersToMap(js_session) {
        var image = '../static/images/icon_small.png';

		$.getJSON("/loadUserLocations", {
			js_session: js_session,
	}, function(response) {
		//Iterate through each user location, get it's coordinates and create a marker on the map
		for(var i = 0; i < response.length; i++) {
			var currCoord = response[i];
			var marker = new google.maps.Marker({
			          position: currCoord,
			          map: map,
			          animation: google.maps.Animation.DROP,
			          icon: image
			        });
		}

	});
	}

	//Adds location to results list view
	function addToListView(result) {
		var newText = "{0} - {1}".format(result.name, result.vicinity)
		$('#location_results').prepend(
			"<a href='#'>" +
			"<li class='collection-item'>" + newText +" </li> </a>");

	}

	function callback(results, status) {
		bounds = new google.maps.LatLngBounds();
		if (status === google.maps.places.PlacesServiceStatus.OK) {
			for (var i = 0; i < results.length; i++) {
				createMarker(results[i]);
				addToListView(results[i]);
			}
			map.fitBounds(bounds);

		}
	}

	function createMarker(place) {
		var placeLoc = place.geometry.location;
		var marker = new google.maps.Marker({
			map: map,
			animation: google.maps.Animation.DROP,

			position: place.geometry.location
		});
		bounds.extend(marker.position);


		google.maps.event.addListener(marker, 'click', function() {
			infowindow.setContent(place.name);
			infowindow.open(map, this);
		});
	}
