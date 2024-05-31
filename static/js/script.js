document.addEventListener('DOMContentLoaded', function() {
    // Select all navigation buttons
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
        inputLat.type = 'hidden';
        inputLat.name = 'latitude';
        inputLat.value = lat;
        form.appendChild(inputLat);
        var inputLon = document.createElement('input');
        inputLon.type = 'hidden';
        inputLon.name = 'longitude';
        inputLon.value = lon;
        form.appendChild(inputLon);
        form.submit();
    }

    // Attach the geolocation function to the location button
    const locationButton = document.querySelector('.location-button');
    if(locationButton) {
        locationButton.addEventListener('click', getLocation);
    }
});
