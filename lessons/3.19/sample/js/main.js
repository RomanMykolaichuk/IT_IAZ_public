document.addEventListener("DOMContentLoaded", function() {
    const images = [
        "path/to/first-image.jpg",
        "path/to/second-image.jpg",
        "path/to/third-image.jpg"
    ];

    let currentImage = 0;

    function changeImage() {
        currentImage = (currentImage + 1) % images.length;
        document.getElementById("galleryImage").src = images[currentImage];
    }

    document.getElementById("nextImageButton").addEventListener("click", changeImage);
});
