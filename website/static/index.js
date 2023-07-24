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