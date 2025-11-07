/* Author: Lorraine Xu */

function displayGroups(data) {
  // empty old data
  $("#groups_container").empty();

  // insert all new data as cards in a single row
  $.each(data.slice(0, 3), function(i, datum) {
    // Prepare member tags, using ellipsis if there are more than 5 members
    let members = datum.members.slice(0, 5);
    let memberTags = members.map(function(member) {
      return `<span class="badge badge-light-pink">${member}</span>`;
    }).join(' ');

    // Add ellipsis if there are more than 5 members
    if (datum.members.length > 5) {
      memberTags += ' <span class="badge badge-light-pink">...</span>';
    }
    console.log("introduction: ", datum.introduction)

    // Create the card for each group
    let new_group = $(`
      <div class="col-md-4 mb-4">
        <div class="card">
          <img src="${datum.image}" class="card-img-top" alt="${datum["group name"]}">
          <div class="card-body">
            <h5 class="card-title">${datum["group name"]}</h5>
            <p class="card-text">${datum.introduction.substring(0, 100)}...</p>
            <div class="members">
              ${memberTags} <!-- Member tags are displayed here -->
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

    // Add the newly created card to the groups container
    $("#groups_container").append(new_group);
  });
}

$(document).ready(function () {
  displayGroups(data);
});