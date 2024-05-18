$(document).ready(function() {
    // Function to fetch and fill the form
    function fillForm() {
        fetch('http://127.0.0.1:5000//processed_data')
            .then(response => response.json())
            .then(data => {
                console.log("Data received from server:", data); // Check the entire data object

                if (data && data.name && data.amount) {
                    console.log("Name:", data.name); // Check the name value
                    console.log("Amount:", data.amount); 
                    // Check the amount value
                    console.log("Amount In Words:", data.amount_in_words); // Check the name value
                    console.log("Account:", data.account); 
                    // Set form field values
                    $('#name').val(data.name);
                    $('#amount').val(data.amount);
                    $('#amount_in_words').val(data.amount_in_words);
                    $('#account').val(data.account);
                } else {
                    console.error("Data received from server is invalid or incomplete.");
                }
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    }

    // Click event handler for the form fill button
    $('#fillFormButton').click(fillForm);
});
