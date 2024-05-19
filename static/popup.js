document.addEventListener("DOMContentLoaded", function() {
    // Get the modal
    var modal = document.getElementById("uploadModal");

    // Get the button that opens the modal
    var btn = document.getElementById("openModalBtn");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // Function to open the modal
    function openModal() {
        modal.style.display = "block";
        btn.style.display = "none";  // Hide the button
        span.style.display = "block";  // Show the close button
        var uploadHeader = document.getElementById("uploadHeader");
        if (uploadHeader !== null) {
            uploadHeader.style.display = "none";
        }
    }

    // Function to close the modal
    function closeModal() {
        modal.style.display = "none";
        btn.style.display = "block";
        span.style.display = "none";  // Show the close button
        console.log("Closing modal");
        var uploadHeader = document.getElementById("uploadHeader");
        if (uploadHeader !== null) {
            uploadHeader.style.display = "block";
        }
    }
    // Initially hide the modal
    closeModal();

    // When the user clicks the button, open the modal 
    btn.onclick = openModal;

    // When the user clicks on <span> (x), close the modal
    span.onclick = closeModal;

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            closeModal();
        }
    }
});
