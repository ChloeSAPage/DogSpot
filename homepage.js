document.addEventListener('DOMContentLoaded', function() {
    // Select all navigation buttons
    const navButtons = document.querySelectorAll('.nav-button');
    
    // Iterate over each button and add a click event listener
    navButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            console.log(`Navigation Button ${index + 1} clicked`);
            // Add your logic for each button click here
        });
    });

    // Select the 'Explore Now' button
    const exploreButton = document.querySelector('.explore-button');
    
    // Add a click event listener to the 'Explore Now' button
    exploreButton.addEventListener('click', () => {
        console.log('Explore Now button clicked');
        // Add your logic for this button click here
    });
});