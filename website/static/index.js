function confirmMeetup(meetupId) {
    fetch("/confirm-meetup", {
      method: "POST",
      body: JSON.stringify({ meetupId: meetupId }),
    }).then((_res) => {
      window.location.href = "/view_meetups";
    });
}

function declineMeetup(meetupId, page) {
    fetch("/decline-meetup", {
      method: "POST",
      body: JSON.stringify({ meetupId: meetupId }),
    }).then((_res) => {
      window.location.href = page;
    });
}

function deleteMeetup(meetupId, page) {
  fetch("/delete-meetup", {
    method: "POST",
    body: JSON.stringify({ meetupId: meetupId }),
  }).then((_res) => {
    window.location.href = page;
  });
}

function newOwner(meetupId, page) {
  var inputId = "new-owner" + String(meetupId)
  var email = document.getElementById(inputId).value;
  fetch("/new-owner", {
    method: "POST",
    body: JSON.stringify({ newOwner: email, meetupId: meetupId }),
  }).then((_res) => {
    window.location.href = page;
  });
}

function invite(meetupId, page) {
  var invite = "invite-user" + String(meetupId)
  var emails = document.getElementById(invite).value;
  fetch("/invite-users", {
    method: "POST",
    body: JSON.stringify({ invites: emails, meetupId: meetupId }),
  }).then((_res) => {
    window.location.href = page;
  });
}
