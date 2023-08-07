function initMap(meetupId) {
    console.log("Ran2")
    meetupId = 'map' + String(meetupId)
    console.log("MeetupId: " + meetupId)
    let location = {lat: -25.344, lng: 131.036};
    map = new google.maps.Map(
        document.getElementById(meetupId), {zoom: 12, center: location}
          )
          //let marker = new google.maps.Marker({position: location, map: meetupMap})
}