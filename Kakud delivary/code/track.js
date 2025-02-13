// script.js
function initMap() {
    // Default coordinates for initial map view (Bangalore, India)
    var myLatLng = { lat: 12.9716, lng: 77.5946 };
  
    // Create a map object and specify the DOM element for display
    var map = new google.maps.Map(document.getElementById('map'), {
      center: myLatLng,
      zoom: 8 // Adjust the initial zoom level as needed
    });
  
    // Example: Add a marker for a vehicle's current location (can be dynamically updated)
    var marker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      title: 'Current Location'
    });
  }
  