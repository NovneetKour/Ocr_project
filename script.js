const dropArea = document.getElementById("drop-area");
const inputFile = document.getElementById("img");

inputFile.addEventListener("change", uploadmage);

function uploadmage() {
    let imgLink = URL.createObjectURL(inputFile.files[0]);
    dropArea.style.backgroundImage = `url(${imgLink})`;
}

document.addEventListener("DOMContentLoaded", function(){ 
    const form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Fetch the form data and submit it to the server using Fetch API
        fetch("http://127.0.0.1:5000/process_image", {
            method: "POST",
            body: new FormData(form)
        })
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
            // Handle the response data
            const responseElement = document.getElementById("response");
            responseElement.textContent = JSON.stringify(data, null, 2);
            var uploadedImage = document.getElementById("uploaded-image");
            uploadedImage.innerHTML = `<img src="${data.url}" alt="Uploaded Cheque Image">`;
        })
        .catch(error => {
            // Handle any errors
            console.error(error);
        });
    });
});


