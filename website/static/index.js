function confirmMeetup(meetupId) {
    fetch("/confirm-meetup", {
      method: "POST",
      body: JSON.stringify({ meetupId: meetupId }),
    }).then((_res) => {
      window.location.href = "/view_meetups";
    });
  }