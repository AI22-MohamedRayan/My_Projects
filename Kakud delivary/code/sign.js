document.getElementById('cancelButton').addEventListener('click', function() {
    document.getElementById('signupForm').reset();
});

document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match!');
    } else {
        alert('Form submitted successfully!');
        // Add form submission logic here (e.g., send data to the server)
    }
});