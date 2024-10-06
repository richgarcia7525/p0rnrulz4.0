let audio; // Declare the audio variable only once

document.addEventListener('DOMContentLoaded', function () {
    // If audio hasn't been initialized yet, initialize it
    if (!audio) {
        audio = new Audio('{{ url_for("static", filename="sounds/electric-noise.mp3") }}'); 
        // Make sure this path is accurate based on Flask's static file serving
    }

    // Example usage: Play the audio on certain actions
    document.addEventListener('click', function () {
        if (audio) {
            audio.play(); // Plays the electric noise sound
        }
    });
});



