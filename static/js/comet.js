document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    let trail = [];

    // Create the trail elements
    function createCometTrail(e) {
        const comet = document.createElement('div');
        comet.className = 'comet-trail';
        comet.style.left = e.pageX + 'px';
        comet.style.top = e.pageY + 'px';
        body.appendChild(comet);

        // Push the comet element into the trail array
        trail.push(comet);

        // Remove the comet after 500ms (this will create a trail effect)
        setTimeout(() => {
            comet.remove();
            trail.shift();
        }, 500); // Adjust this time to control the length of the trail
    }

    // Listen for mouse movement and create comet trail
    document.addEventListener('mousemove', createCometTrail);

    // Function to change comet color based on section
    function changeCometColor(color) {
        trail.forEach(comet => {
            comet.style.backgroundColor = color;
            comet.style.boxShadow = `0 0 10px ${color}, 0 0 20px ${color}`; // Adjust glow with new color
        });
    }

    // Example: Change comet color when hovering over different sections
    const sections = document.querySelectorAll('.video-section');
    sections.forEach(section => {
        section.addEventListener('mouseenter', function() {
            if (this.id === 'trending') {
                changeCometColor('#39FF14'); // Neon green for trending
            } else if (this.id === 'newest') {
                changeCometColor('#FF0054'); // Neon pink for newest
            } else if (this.id === 'most-popular') {
                changeCometColor('#00FFFF'); // Cyan for most popular
            } else if (this.id === 'most-viewed') {
                changeCometColor('#FFD700'); // Gold for most viewed
            } else if (this.id === 'straight') {
                changeCometColor('#FF4500'); // Orange for straight
            } else if (this.id === 'gay') {
                changeCometColor('#0000FF'); // Blue for gay
            } else if (this.id === 'trans') {
                changeCometColor('#800080'); // Purple for trans
            }
        });
    });
});


