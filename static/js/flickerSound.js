document.querySelectorAll('.neon-button').forEach(button => {
    button.addEventListener('mouseenter', () => {
        document.getElementById('flicker-sound').play();
    });
});




