// Function to remove the field
function removeField(button) {
    // Get the parent input group (the div containing the input and buttons)
    const inputGroup = button.closest('.input-group');

    // Remove the input group (the entire div with the input and buttons)
    inputGroup.remove();
}

document.addEventListener('DOMContentLoaded', function() {
    // Add new input fields to the respective containers
    window.addField = function(fieldType) {
        let container;

        // Determine which section is being targeted
        if (fieldType === 'members') {
            container = document.getElementById('members-container');
        } else if (fieldType === 'discography') {
            container = document.getElementById('discography-container');
        } else if (fieldType === 'recommended_songs') {
            container = document.getElementById('recommended-songs-container');
        }

        // Create a new input group
        const newInputGroup = document.createElement('div');
        newInputGroup.classList.add('input-group', 'mb-2');

        // Create the input field and buttons
        newInputGroup.innerHTML = `
            <input type="text" name="${fieldType}[]" class="form-control">
            <button type="button" class="btn btn-outline-secondary cute-btn" onclick="addField('${fieldType}')">+</button>
            <button type="button" class="btn btn-outline-secondary cute-btn remove-btn" style="display:none;">-</button>
        `;

        // Append the new input group to the container
        container.appendChild(newInputGroup);
        newInputGroup.querySelector('input').focus();

        // Add event listener to remove button to remove the current input group
        newInputGroup.querySelector('.remove-btn').addEventListener('click', function() {
            newInputGroup.remove();
        });
    };

    // Adding event listeners to input fields to clear error messages on input
    function addInputListeners() {
        const inputs = [
            'group_name', 'debut_year', 'introduction', 'members', 'discography', 'recommended_songs', 'image', 'fandom', 'rating'
        ];

        inputs.forEach(inputId => {
            const input = document.getElementById(inputId);

            if (input) {
                input.addEventListener('input', function() {
                    const errorElement = document.getElementById(inputId + '_error');
                    if (errorElement) {
                        errorElement.textContent = ''; // Clear error message
                        errorElement.style.display = 'none'; // Hide the error message
                    }
                });
            }
        });
    }

    // Call the function to add event listeners
    addInputListeners();

    // Form submission handling
    $("#edit-item-form").on("submit", function(event) {
        event.preventDefault(); // Prevent the default form submission
    
        // Clear previous error messages
        $(".error-message").hide();
    
        // Initialize an empty errors object
        let errors = [];
    
        // Manually gather form data into an object
        const dataObject = {
            group_name: document.getElementById('group_name').value,
            debut_year: document.getElementById('debut_year').value,
            introduction: document.getElementById('introduction').value,
            members: [],
            discography: [],
            recommended_songs: [],
            image: document.getElementById('image').value,
            fandom: document.getElementById('fandom').value,
            rating: document.getElementById('rating').value,
            similar_groups: []  // Initialize for similar groups
        };
    
        // Collect members (and filter out empty values)
        const memberInputs = document.querySelectorAll('[name="members[]"]');
        memberInputs.forEach(input => {
            const value = input.value;  // Keep the raw input value
            if (value.trim()) {  // Check if it's not just whitespace
                dataObject.members.push(value);
            }
        });
    
        // Collect discography (and filter out empty values)
        const discographyInputs = document.querySelectorAll('[name="discography[]"]');
        discographyInputs.forEach(input => {
            const value = input.value;  // Keep the raw input value
            if (value.trim()) {  // Check if it's not just whitespace
                dataObject.discography.push(value);
            }
        });
    
        // Collect recommended songs (and filter out empty values)
        const recommendedSongsInputs = document.querySelectorAll('[name="recommended_songs[]"]');
        recommendedSongsInputs.forEach(input => {
            const value = input.value;  // Keep the raw input value
            if (value.trim()) {  // Check if it's not just whitespace
                dataObject.recommended_songs.push(value);
            }
        });
    
        // Collect similar groups (checkboxes)
        const similarGroups = document.querySelectorAll('[name="similar_groups"]:checked');
        similarGroups.forEach(input => dataObject.similar_groups.push(input.value));
    
        // Validate inputs
        if (!dataObject.group_name) {
            errors.push("Group name is required.");
            $('#group_name_error').text("Group name is required.").show();
        }
    
        if (!dataObject.image) {
            errors.push("Image URL is required.");
            $('#image_error').text("Image URL is required.").show();
        }
    
        if (!dataObject.debut_year || isNaN(dataObject.debut_year)) {
            errors.push("Debut year must be a valid number.");
            $('#debut_year_error').text("Debut year must be a valid number.").show();
        }
    
        if (!dataObject.introduction) {
            errors.push("Introduction cannot be blank.");
            $('#introduction_error').text("Introduction cannot be blank.").show();
        }
    
        if (!dataObject.members.length) {
            errors.push("Members cannot be blank.");
            $('#members_error').text("Members cannot be blank.").show();
        }
    
        if (!dataObject.discography.length) {
            errors.push("Discography cannot be blank.");
            $('#discography_error').text("Discography cannot be blank.").show();
        }
    
        if (!dataObject.fandom) {
            errors.push("Fandom cannot be blank.");
            $('#fandom_error').text("Fandom cannot be blank.").show();
        }
    
        if (!dataObject.rating || isNaN(dataObject.rating)) {
            errors.push("Rating must be a valid number.");
            $('#rating_error').text("Rating must be a valid number.").show();
        }
    
        if (!dataObject.recommended_songs.length) {
            errors.push("Recommended songs cannot be blank.");
            $('#recommended_songs_error').text("Recommended songs cannot be blank.").show();
        }
    
        if (!dataObject.similar_groups.length) {
            errors.push("Please select at least one similar group.");
            $('#similar_groups_error').text("Please select at least one similar group.").show();
        }
    
        // If there are no errors, proceed with the AJAX request
        if (errors.length === 0) {
            $.ajax({
                type: "POST",
                url: "/edit/" + group.id,  // Adjust the URL with the group ID
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(dataObject),  // Send the serialized data
                success: function(result) {
                    // Redirect to the view page after successful submission
                    window.location.href = '/view/' + result.id;
                },
                error: function(request, status, error) {
                    console.log("Error");
                    console.log(request);
                    console.log(status);
                    console.log(error);
                }
            });
        }
    });

    // Modal elements
    const discardModal = document.getElementById('discardModal');
    const confirmDiscardButton = document.getElementById('confirm-discard-btn');

    // When the user clicks on "Discard Changes"
    document.getElementById('discard-btn').addEventListener('click', function() {
        // Show the modal asking for confirmation
        discardModal.style.display = 'block';  // Show the modal
    });

    // If the user clicks "Yes, Discard" in the modal
    confirmDiscardButton.addEventListener('click', function() {
        // Redirect to the view page without saving
        window.location.href = '/view/' + group.id; // Assuming `group.id` is available
    });

    // Close the modal when the "Cancel" button or the close icon is clicked
    const closeButtons = discardModal.querySelectorAll('[data-bs-dismiss="modal"], .btn-close');
    closeButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            discardModal.style.display = 'none';  // Hide the modal
        });
    });

    // For users who click anywhere outside the modal, close it (optional)
    window.addEventListener('click', function(event) {
        if (event.target === discardModal) {
            discardModal.style.display = 'none';  // Hide the modal if clicked outside
        }
    });
});
