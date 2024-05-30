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
                console.log('home button clicked');
                window.location.href = '/';
            });
        }
        if (button.id === 'explore-button') {
            button.addEventListener('click', () => {
                console.log('explore button clicked');
                window.location.href = 'explore';
            });
        }
        if (button.id === 'contact-button') {
            button.addEventListener('click', () => {
                console.log('contact button clicked');
                window.location.href = 'contact';
            });
        }
        if (button.id === 'signin-button') {
            button.addEventListener('click', () => {
                console.log('Sign In button clicked');
                window.location.href = 'signin'; // Navigate to the sign-in page
            });
        }
    });

    // Select the 'Explore Now' button
    const exploreButton = document.querySelector('.explore-button');
    
    exploreButton.addEventListener('click', () => {
        console.log('Explore Now button clicked');
        window.location.href = 'explore';
        // Add your logic for this button click here

    });
});