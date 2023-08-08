// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 43.6532, lng: -79.3832 },
      zoom: 13,
      mapTypeControl: false,
    });
    //const card = document.getElementById("pac-card");
    const input = document.getElementById("location");
    //const biasInputElement = document.getElementById("use-location-bias");
    //const strictBoundsInputElement = document.getElementById("use-strict-bounds");
    const options = {
      fields: ["formatted_address", "geometry", "name"]
    };
  
    //map.controls[google.maps.ControlPosition.TOP_CENTER].push(card);
  
    const autocomplete = new google.maps.places.Autocomplete(input, options);
    const latitudeInput = document.getElementById("latitude");
    const longitudeInput = document.getElementById("longitude");
    const fullAddress = document.getElementById("fullAddress");
    const commonNameInput = document.getElementById("locationCommonName");
    // Bind the map's bounds (viewport) property to the autocomplete object,
    // so that the autocomplete requests use the current map bounds for the
    // bounds option in the request.
    //autocomplete.bindTo("bounds", map);
  
    const infowindow = new google.maps.InfoWindow();
    const infowindowContent = document.getElementById("infowindow-content");
  
    infowindow.setContent(infowindowContent);
  
    const marker = new google.maps.Marker({
      map,
      anchorPoint: new google.maps.Point(0, -29),
    });
  
    autocomplete.addListener("place_changed", () => {
      infowindow.close();
      marker.setVisible(false);
  
      const place = autocomplete.getPlace();
      latitudeInput.value = place.geometry.location.lat();
      longitudeInput.value = place.geometry.location.lng();
      fullAddress.value = place.formatted_address;
      commonNameInput.value = place.name;
      console.log("Lat: " + place.geometry.location.lat());
      console.log("Long: " + place.geometry.location.lng());
      console.log("Place: " + place);
      console.log("Place Name: " + place.name);
      console.log("Place Address: " + place.formatted_address);
      if (!place.geometry || !place.geometry.location) {
        // User entered the name of a Place that was not suggested and
        // pressed the Enter key, or the Place Details request failed.
        window.alert("No details available for input: '" + place.name + "'");
        return;
      }
  
      // If the place has a geometry, then present it on a map.
      if (place.geometry.viewport) {
        map.fitBounds(place.geometry.viewport);
      } else {
        map.setCenter(place.geometry.location);
        map.setZoom(17);
      }
  
      marker.setPosition(place.geometry.location);
      marker.setVisible(true);
      infowindowContent.children["place-name"].textContent = place.name;
      infowindowContent.children["place-address"].textContent =
        place.formatted_address;
      infowindow.open(map, marker);
    });
  }
  
  window.initMap = initMap;
  