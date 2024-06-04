class App {
    constructor() {
        this.init();
    }

    init() {
        document.addEventListener('DOMContentLoaded', () => {
            console.log('DOM fully loaded and parsed');
            this.setupNavButtons();
            this.setupFormSubmission();
            this.exposeGlobalFunctions(); // Expose necessary functions globally
        });
    }

    setupNavButtons() {
        const navButtons = document.querySelectorAll('.nav-button');
        navButtons.forEach((button, index) => {
            button.addEventListener('click', () => {
                console.log(`Navigation Button ${index + 1} clicked`);
                switch (button.id) {
                    case 'home-button':
                        this.navigateTo('/');
                        break;
                    case 'explore-button':
                    case 'explore-button2':
                        this.navigateTo('explore');
                        break;
                    case 'contact-button':
                        this.navigateTo('contact');
                        break;
                    case 'signin-button':
                        this.navigateTo('signin');
                        break;
                }
            });
        });
    }

    navigateTo(url) {
        console.log(`Navigating to ${url}`);
        window.location.href = url;
    }

    setupFormSubmission() {
        const contactForm = document.getElementById('contact-form');
        if (contactForm) {
            contactForm.addEventListener('submit', (event) => {
                console.log('Form is about to be submitted');
                const name = document.getElementById('name').value.trim();
                const email = document.getElementById('email').value.trim();
                const message = document.getElementById('message').value.trim();
                if (!name || !email || !message) {
                    alert('Please ensure all fields have been filled out');
                    event.preventDefault();
                    return;
                }
                console.log('Submitting form');
            });
        }

        const searchButton = document.querySelector('.search-button');
        if (searchButton) {
            searchButton.addEventListener('click', () => {
                document.getElementById('currentLocationUsed').value = 'false';
            });
        }

        const locationButton = document.querySelector('.location-button');
        if (locationButton) {
            locationButton.addEventListener('click', () => {
                this.getLocation();
                document.getElementById('currentLocationUsed').value = 'true';
            });
        }
    }

    getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(this.submitLocation.bind(this));
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    }

    submitLocation(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        const form = document.getElementById('search-form');
        const inputLat = this.createHiddenInput('latitude', lat);
        const inputLon = this.createHiddenInput('longitude', lon);
        const inputCurrentLocation = this.createHiddenInput('currentLocationUsed', 'true');

        form.appendChild(inputLat);
        form.appendChild(inputLon);
        form.appendChild(inputCurrentLocation);

        console.log('Latitude:', lat);
        console.log('Longitude:', lon);
        console.log('Current Location Used:', 'true');

        form.submit();
    }

    createHiddenInput(name, value) {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = name;
        input.value = value;
        return input;
    }

    exposeGlobalFunctions() {
        window.showMoreInfo = App.showMoreInfo;
        window.initMap = App.initMap;
        window.getDirections = App.getDirections;
        window.submitSearch = App.submitSearch;
        window.getLocation = this.getLocation.bind(this); // Ensure this method is accessible globally
    }

    static showMoreInfo(businessId, latitude, longitude, currentLocationUsed) {
        const lat = parseFloat(latitude);
        const lng = parseFloat(longitude);

        if (!isFinite(lat) || !isFinite(lng)) {
            console.error('Invalid coordinates:', latitude, longitude);
            return;
        }

        const detailContainer = document.getElementById('details-' + businessId);
        console.log('Current Location Used:', currentLocationUsed);

        if (detailContainer) {
            detailContainer.style.display = 'block';
            if (currentLocationUsed === 'true') {
                App.getDirections(businessId, lat, lng);
            } else {
                App.initMap(businessId, lat, lng);
            }
        } else {
            console.log('No details found for Business ID:', businessId);
        }
    }

    static initMap(businessId, latitude, longitude) {
        const businessLocation = { lat: latitude, lng: longitude };
        const map = new google.maps.Map(document.getElementById('map-' + businessId), {
            zoom: 15,
            center: businessLocation
        });
        new google.maps.Marker({
            position: businessLocation,
            map: map
        });
    }

    static getDirections(businessId, businessLat, businessLng) {
        const directionsService = new google.maps.DirectionsService();
        const directionsRenderer = new google.maps.DirectionsRenderer();
        const map = new google.maps.Map(document.getElementById('map-' + businessId), {
            zoom: 14,
            center: { lat: businessLat, lng: businessLng }
        });
        directionsRenderer.setMap(map);

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition((position) => {
                const userLocation = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };
                const request = {
                    origin: userLocation,
                    destination: { lat: businessLat, lng: businessLng },
                    travelMode: 'DRIVING'
                };
                directionsService.route(request, (result, status) => {
                    if (status == 'OK') {
                        directionsRenderer.setDirections(result);
                    } else {
                        window.alert('Directions request failed due to ' + status);
                    }
                });
            }, () => {
                window.alert('Geolocation service failed');
            });
        } else {
            window.alert('Your browser doesn\'t support geolocation');
        }
    }

    static submitSearch(element) {
        const location = element.textContent || element.innerText;
        console.log('Clicked on:', location);
        document.getElementById('location').value = location;
        console.log('Input value set to:', location);
        document.getElementById('search-form').submit();
        console.log('Form submitted');
        return false;
    }
}

// Initialize the app
new App();
