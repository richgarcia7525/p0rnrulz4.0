document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById("videoModal");
    const modalVideo = document.getElementById("modal-video");
    const closeModal = document.getElementsByClassName("close")[0];


    // scripts.js

document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('.video-carousel');
    carousel.addEventListener('wheel', (event) => {
        event.preventDefault();
        carousel.scrollBy({
            left: event.deltaY < 0 ? -100 : 100,
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    
    // Handle video hover (play preview)
    document.querySelectorAll('.video-card').forEach(videoCard => {
        const thumbnail = videoCard.querySelector('.video-thumbnail');
        const preview = videoCard.querySelector('.video-preview');

        videoCard.addEventListener('mouseenter', function () {
            preview.play(); // Play the preview when hovering
        });

        videoCard.addEventListener('mouseleave', function () {
            preview.pause(); // Pause the preview when not hovering
            preview.currentTime = 0; // Reset to the beginning
        });
    });

    // Handle video modal popup
    const modal = document.getElementById('videoModal');
    const modalVideo = document.getElementById('modal-video');
    const closeModal = document.getElementsByClassName('close')[0];

    document.querySelectorAll('.video-card').forEach(videoCard => {
        const thumbnail = videoCard.querySelector('.video-thumbnail');
        const videoEmbed = videoCard.querySelector('.video-preview source').src;

        thumbnail.addEventListener('click', function () {
            modalVideo.src = videoEmbed; // Set video src in modal
            modal.style.display = 'block'; // Show modal
        });
    });

    // Close modal on 'x' click
    closeModal.onclick = function () {
        modal.style.display = 'none';
        modalVideo.src = ''; // Stop video playback
    };

    // Close modal if clicked outside video
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
            modalVideo.src = ''; // Stop video playback
        }
    };
})});

