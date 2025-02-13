// script.js
document.getElementById('vehicle-check').addEventListener('submit', function(event) {
    event.preventDefault();
    
    var productName = document.getElementById('product-name').value;
    var productSize = parseFloat(document.getElementById('product-size').value);
    
    var deliveryLink = '';
    if (productSize <= 1) {
      deliveryLink = '<a href="pay.html">Small Truck 1T</a>';
    } else if (productSize <= 5) {
      deliveryLink = '<a href="pay.html">Medium Truck 5T</a>';
    } else {
      deliveryLink = '<a href="pay.html">Heavy Truck </a>';
    }
    
    var resultElement = document.getElementById('vehicle-results');
    resultElement.innerHTML = ''; 
    
    if (deliveryLink !== '') {
      var resultHTML = '<div class="vehicle-result">';
      resultHTML += '<h3>Delivery Option for ' + productName + ' (' + productSize + ' Tons):</h3>';
      resultHTML += '<p>' + deliveryLink + '</p>';
      resultHTML += '</div>';
      
      resultElement.innerHTML = resultHTML;
    } else {
      resultElement.innerHTML = '<p>No delivery options found.</p>';
    }
  });
  