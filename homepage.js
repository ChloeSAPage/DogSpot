document.addEventListener('DOMContentLoaded', function() {
    // Select all navigation buttons
    const navButtons = document.querySelectorAll('.nav-button');
    
    // Iterate over each button and add a click event listener
    navButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            console.log(`Navigation Button ${index + 1} clicked`);
        });

        if (button.id === 'signin-button') {
            button.addEventListener('click', () => {
                console.log('Sign In button clicked');
                window.location.href = 'signin.html'; // Navigate to the sign-in page
            });
        }
    });

    // Select the 'Explore Now' button
    const exploreButton = document.querySelector('.explore-button');
    
    // Add a click event listener to the 'Explore Now' button
    exploreButton.addEventListener('click', () => {
        console.log('Explore Now button clicked');
        // Add your logic for this button click here

    });
});