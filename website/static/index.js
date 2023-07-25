function confirmMeetup(meetupId) {
    fetch("/confirm-meetup", {
      method: "POST",
      body: JSON.stringify({ meetupId: meetupId }),
    }).then((_res) => {
      window.location.href = "/view_meetups";
    });
}

function viewDeclineMeetup(meetupId) {
    fetch("/decline-meetup", {
      method: "POST",
      body: JSON.stringify({ meetupId: meetupId }),
    }).then((_res) => {
      window.location.href = "/view_meetups";
    });
}

function confirmDeclineMeetup(meetupId) {
    fetch("/decline-meetup", {
      method: "POST",
      body: JSON.stringify({ meetupId: meetupId }),
    }).then((_res) => {
      window.location.href = "/confirmed";
    });
}

function viewDeleteMeetup(meetupId) {
  fetch("/delete-meetup", {
    method: "POST",
    body: JSON.stringify({ meetupId: meetupId }),
  }).then((_res) => {
    window.location.href = "/view_meetups";
  });
}

function confirmDeleteMeetup(meetupId) {
  fetch("/delete-meetup", {
    method: "POST",
    body: JSON.stringify({ meetupId: meetupId }),
  }).then((_res) => {
    window.location.href = "/confirmed";
  });
}

function viewNewOwner(meetupId) {
  var email = document.getElementById("new-owner-name").value;
  fetch("/new-owner", {
    method: "POST",
    body: JSON.stringify({ newOwner: email, meetupId: meetupId }),
  }).then((_res) => {
    window.location.href = "/view_meetups";
  });
}

$('#ownerModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  //var recipient = button.data('whatever') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-title').text('Transfer Ownership')
})