function displaySearchResults(results, query) {
    // Empty the old data
    $("#search_results_container").empty();

    // Display the search query used
    $("#search_results_container").append("<h4>Search Results for: '" + query + "'</h4>");

    // Display the number of results
    let resultCount = results.length;
    $("#search_results_container").append("<p class='result-count'>Found " + resultCount + " result(s).</p>");

    // If no results, show a message
    if (resultCount === 0) {
        $("#search_results_container").append("<p>No results found.</p>");
    } else {
        // Insert all new data as cards in a single row
        let row = $("<div class='row'></div>");  // Create a row to hold the cards

        $.each(results, function(i, datum) {
            let members = datum.members;
            let memberTags = members.map(function(member) {
                // Highlight the member's name if it matches the query
                let highlightedMember = member.replace(new RegExp(query, 'gi'), function(match) {
                    return `<span class="member-highlight">${match}</span>`;
                });
                return `<span class="badge badge-light-pink">${highlightedMember}</span>`;
            }).join(' ');

            if (!memberTags.includes('<span class="member-highlight">')) {
                members = members.slice(0, 5);

                memberTags = members.map(function(member) {
                    return `<span class="badge badge-light-pink">${member}</span>`;
                }).join(' ');

                if (datum.members.length > 5) {
                    memberTags += ' <span class="badge badge-light-pink">...</span>';
                }
            }
            else {
                let currentMember = 0;

                while (currentMember < members.length) {
                    let subMembers = members.slice(currentMember, currentMember + 5);
                    let highlightedSubMembers = subMembers.map(function(member) {
                        // Highlight the member's name if it matches the query
                        let highlightedMember = member.replace(new RegExp(query, 'gi'), function(match) {
                            return `<span class="member-highlight">${match}</span>`;
                        });
                        return `<span class="badge badge-light-pink">${highlightedMember}</span>`;
                    }).join(' ');

                    // Check if the substring contains any highlighted text (assuming highlighted text is wrapped in <mark> tags)
                    if (highlightedSubMembers.includes('<span class="member-highlight">')) {
                        if (currentMember != 0) {
                            memberTags = '<span class="badge badge-light-pink">...</span> ' + highlightedSubMembers;
                        }
                        else {
                            memberTags = highlightedSubMembers; // Save the highlighted portion
                        }
                        if (currentMember + subMembers.length < members.length) {
                            memberTags += ' <span class="badge badge-light-pink">...</span>';
                        }
                        break; // Exit the loop when highlighted text is found
                    } else {
                        currentMember += 5;
                    }
                }
            }

            // Highlight group name and introduction
            let groupName = datum["group name"];
            let highlightedGroupName = groupName.replace(new RegExp(query, 'gi'), function(match) {
                return `<span class="highlight">${match}</span>`;
            });

            let introText = datum["introduction"];
            let highlightedIntro = introText.replace(new RegExp(query, 'gi'), function(match) {
                return `<span class="highlight">${match}</span>`;
            });
            let introToShow;

            if (!highlightedIntro.includes('<span class="highlight">')) {
                introToShow = introText.substring(0, 100) + "...";
            }
            else {
                let currentPosition = 0;

                while (currentPosition < introText.length) {
                    // Extract the substring from currentPosition to currentPosition + 100
                    let subText = introText.slice(currentPosition, currentPosition + 100);
                    let highlightedSubText = subText.replace(new RegExp(query, 'gi'), function(match) {
                        return `<span class="highlight">${match}</span>`;
                    });

                    // Check if the substring contains any highlighted text (assuming highlighted text is wrapped in <mark> tags)
                    if (highlightedSubText.includes('<span class="highlight">')) {
                        if (currentPosition != 0) {
                            introToShow = "..." + highlightedSubText;
                        }
                        else {
                            introToShow = highlightedSubText; // Save the highlighted portion
                        }
                        if (currentPosition + subText.length < introText.length) {
                            introToShow += "...";
                        }
                        break; // Exit the loop when highlighted text is found
                    } else {
                        currentPosition += 100; // Move to the next 100 characters
                    }
                }
            }

            // Create the card for each group
            let new_group = $(`
                <div class="col-md-4 mb-4">
                    <div class="card card-fixed-height">
                        <img src="${datum.image}" class="card-img-top" alt="${datum["group name"]}">
                        <div class="card-body">
                            <h5 class="card-title">${highlightedGroupName}</h5>
                            <p class="card-text">${introToShow}</p>
                            <div class="members">
                                ${memberTags} <!-- Member tags with highlighting are displayed here -->
                            </div>
                            <div class="rating mt-2">
                                <strong>Rating: </strong>${datum.rating}
                            </div>
                        </div>
                    </div>
                </div>
            `);

            // Make the entire card clickable
            new_group.on('click', function() {
                // Redirect to the 'view/<id>' page using the item's id
                window.location.href = "/view/" + datum["id"];
            });

            // Change the cursor to "pointer" when hovering over the card
            new_group.css('cursor', 'pointer');

            // Append the card to the row
            row.append(new_group);
        });

        // Add the row of results to the container
        $("#search_results_container").append(row);
    }
}

$(document).ready(function () {
    displaySearchResults(results, query);
});