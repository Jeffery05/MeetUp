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
  alert("MeetupId: " + meetupId)
  fetch("/new-owner", {
    method: "POST",
    body: JSON.stringify({ newOwner: email, meetupId: meetupId }),
  }).then((_res) => {
    window.location.href = "/view_meetups";
  });
}

function confirmNewOwner(meetupId) {
  var email = document.getElementById("new-owner-name").value;
  fetch("/new-owner", {
    method: "POST",
    body: JSON.stringify({ newOwner: email, meetupId: meetupId }),
  }).then((_res) => {
    window.location.href = "/confirmed";
  });
}

function invite(meetupId, page) {
  alert(page)
  var invite = "invite-user" + String(meetupId)
  var emails = document.getElementById(invite).value;
  fetch("/invite-users", {
    method: "POST",
    body: JSON.stringify({ invites: emails, meetupId: meetupId }),
  }).then((_res) => {
    window.location.href = page;
  });
}
