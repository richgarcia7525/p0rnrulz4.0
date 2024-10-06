document.addEventListener('DOMContentLoaded', function() {
    const comet = document.querySelector('.comet-trail');
    if (!comet) {
        console.warn('Comet trail element not found.');
        return;
    }

    // Move the comet trail with the mouse
    document.addEventListener('mousemove', function(e) {
        const x = e.pageX;
        const y = e.pageY;
        comet.style.left = `${x}px`;
        comet.style.top = `${y}px`;
    });

    // Change comet color based on page
    function changeCometColor(color) {
        comet.style.backgroundColor = color;
        comet.style.boxShadow = `0 0 15px ${color}, 0 0 30px ${color}`;
    }

    if (window.location.pathname.includes('straight')) {
        changeCometColor('#ff0054');  // Pink for straight page
    } else if (window.location.pathname.includes('gay')) {
        changeCometColor('#00ff00');  // Green for gay page
    } else if (window.location.pathname.includes('trans')) {
        changeCometColor('#ffea00');  // Yellow for trans page
    }
});
