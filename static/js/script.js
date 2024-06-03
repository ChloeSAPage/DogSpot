console.log('script.js is loaded');

document.addEventListener('DOMContentLoaded', function() {
    // Select all navigation buttons
    console.log('DOM fully loaded and parsed');
    const navButtons = document.querySelectorAll('.nav-button');
    
    // Iterate over each button and add a click event listener
    navButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            console.log(`Navigation Button ${index + 1} clicked`);
        });
        if (button.id === 'home-button') {
            button.addEventListener('click', () => {
                console.log('Home button clicked');
                window.location.href = '/';
            });
        }
        if (button.id === 'explore-button') {
            button.addEventListener('click', () => {
                console.log('Explore button clicked');
                window.location.href = 'explore';
            });
        }
        //explore.button2 is the 'explore now' button on the homepage
        if (button.id === 'explore-button2') {
            button.addEventListener('click', () => {
                console.log('Explore button clicked');
                window.location.href = 'explore';
            });
        }
        if (button.id === 'contact-button') {
            button.addEventListener('click', () => {
                console.log('Contact button clicked');
                window.location.href = 'contact';
            });
        }
        if (button.id === 'signin-button') {
            button.addEventListener('click', () => {
                console.log('Sign In button clicked');
                window.location.href = 'signin';
            });
        }
        
    });

    // Function to get the user's location and submit it
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(submitLocation);
        } else { 
            alert("Geolocation is not supported by this browser.");
        }
    }

    function submitLocation(position) {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;
        var form = document.getElementById('search-form');
        var inputLat = document.createElement('input');
        var inputLon = document.createElement('input');
        var inputCurrentLocation = document.createElement('input');
    
        inputLat.type = 'hidden';
        inputLat.name = 'latitude';
        inputLat.value = lat;
    
        inputLon.type = 'hidden';
        inputLon.name = 'longitude';
        inputLon.value = lon;
    
        inputCurrentLocation.type = 'hidden';
        inputCurrentLocation.name = 'currentLocationUsed';
        inputCurrentLocation.value = 'true';
    
        form.appendChild(inputLat);
        form.appendChild(inputLon);
        form.appendChild(inputCurrentLocation);
    
        // Console log the values to be submitted
        console.log('Latitude:', inputLat.value);
        console.log('Longitude:', inputLon.value);
        console.log('Current Location Used:', inputCurrentLocation.value);
    
        // Submit the form
        form.submit();
    }

    const searchButton = document.querySelector('.search-button');
    searchButton.addEventListener('click', function() {
        document.getElementById('currentLocationUsed').value = 'false';
    });

    // Attach the geolocation function to the location button
    const locationButton = document.querySelector('.location-button');
    if(locationButton) {
        locationButton.addEventListener('click', getLocation,document.getElementById('currentLocationUsed').value = 'true');
    }

   

    // Example sign-in event (you would replace this with actual authentication logic)
    signinForm.addEventListener('submit', function(event) {
        event.preventDefault();
        user.signedIn = true;
        user.username = document.getElementById('signin-username').value;
        updateUI();
    });

    // Initial UI update
    updateUI();
});

function showMoreInfo(businessId, latitude, longitude, currentLocationUsed) {
    // Parse latitude and longitude as floats
    var lat = parseFloat(latitude);
    var lng = parseFloat(longitude);

    // Check if the parsed values are finite numbers
    if (!isFinite(lat) || !isFinite(lng)) {
        console.error('Invalid coordinates:', latitude, longitude);
        return;
    }

    // Find the container for the selected business
    const detailContainer = document.getElementById('details-' + businessId);
    console.log('Current Location Used:', currentLocationUsed); // Add this line for debugging

    // Check if the detail container exists
    if (detailContainer) {
        // Display the container with more details for the selected business
        detailContainer.style.display = 'block';

        // Check if current location was used for the search
        if (currentLocationUsed === 'true') {
            // Call a function to show directions
            getDirections(businessId, lat, lng);
        } else {
            // Call a function to just display the business on the map
            initMap(businessId, lat, lng);
        }
    } else {
        console.log('No details found for Business ID:', businessId);
    }
}

function initMap(businessId, latitude, longitude) {
    var businessLocation = {lat: latitude, lng: longitude};
    var map = new google.maps.Map(document.getElementById('map-' + businessId), {
        zoom: 15,
        center: businessLocation
    });
    var marker = new google.maps.Marker({
        position: businessLocation,
        map: map
    });
}

function getDirections(businessId, businessLat, businessLng) {
    var directionsService = new google.maps.DirectionsService();
    var directionsRenderer = new google.maps.DirectionsRenderer();
    var map = new google.maps.Map(document.getElementById('map-' + businessId), {
        zoom: 14,
        center: {lat: businessLat, lng: businessLng}
    });
    directionsRenderer.setMap(map);

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var userLocation = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            var request = {
                origin: userLocation,
                destination: {lat: businessLat, lng: businessLng},
                travelMode: 'DRIVING'
            };
            directionsService.route(request, function(result, status) {
                if (status == 'OK') {
                    directionsRenderer.setDirections(result);
                } else {
                    window.alert('Directions request failed due to ' + status);
                }
            });
        }, function() {
            window.alert('Geolocation service failed');
        });
    } else {
        window.alert('Your browser doesn\'t support geolocation');
    }
}
function submitSearch(element) {
    var location = element.textContent || element.innerText; // Get the location from the text of the clicked element
    console.log('Clicked on:', location);
    document.getElementById('location').value = location; // Set the value of the search input
    console.log('Input value set to:', location);
    document.getElementById('search-form').submit(); // Submit the form
    console.log('Form submitted');
    return false; // Prevent default link action
}
