document.getElementById('payment-form').addEventListener('submit', function(event) {
  event.preventDefault();

  var formData = new FormData(this);

  fetch('process_payment.php', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    var paymentStatus = document.getElementById('payment-status');
    if (data.status === 'success') {
      paymentStatus.innerHTML = '<p>Payment successful!</p>';
    } else {
      paymentStatus.innerHTML = '<p>Error: ' + data.message + '</p>';
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });

  this.reset();
});

// Toggle display of payment method fields based on selection
document.querySelectorAll('input[name="payment-method"]').forEach(function(radio) {
  radio.addEventListener('change', function() {
    document.querySelectorAll('.payment-fields').forEach(function(field) {
      field.style.display = 'none';
    });
    var selectedMethod = document.querySelector('input[name="payment-method"]:checked').value;
    document.getElementById(selectedMethod + '-fields').style.display = 'block';
  });
});

document.getElementById('load-payments').addEventListener('click', function() {
  var userEmail = document.getElementById('user-email').value;
  if (userEmail === '') {
    alert('Please enter your email to view payment history.');
    return;
  }

  fetch('get_payments.php?email=' + encodeURIComponent(userEmail))
    .then(response => response.json())
    .then(data => {
      var paymentHistory = document.getElementById('payment-history');
      if (data.status === 'success') {
        var payments = data.payments;
        var paymentList = '<ul>';
        payments.forEach(function(payment) {
          paymentList += '<li>' + payment.payment_method + ': ' + payment.details + '</li>';
        });
        paymentList += '</ul>';
        paymentHistory.innerHTML = paymentList;
      } else {
        paymentHistory.innerHTML = '<p>Error: ' + data.message + '</p>';
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
