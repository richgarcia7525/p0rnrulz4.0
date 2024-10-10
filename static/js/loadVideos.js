async function loadAllVideos() {
    try {
        // Fetch the videos from the server
        const response = await fetch('/videos');
        const videos = await response.json();

        // Get the container where the videos will be displayed
        let container = document.getElementById('videos-container');
        container.innerHTML = '';

        // Iterate through the videos and add each to the container
        videos.forEach(video => {
            let videoElement = `
                <div class="video-item">
                    <h3>${video.Title}</h3>
                    <p>Duration: ${video.Duration} sec</p>
                    <img src="${video.Thumbnail}" alt="Thumbnail">
                    <div class="video-embed">${video.Embed}</div>
                    <p>Tags: ${video.Tags}</p>
                </div>
            `;
            container.innerHTML += videoElement;
        });
    } catch (error) {
        console.error("Error loading videos:", error);
    }
}

// Load the videos once the document is ready
document.addEventListener('DOMContentLoaded', loadAllVideos);

            