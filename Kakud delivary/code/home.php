<?php
session_start();

// Database connection
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "user_info";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if 'from-location' and 'to-location' are set in $_POST
    if (isset($_POST['from-location']) && isset($_POST['to-location'])) {
        // Retrieve form data
        $fromLocation = $_POST['from-location'];
        $toLocation = $_POST['to-location'];

        // Validate input data
        if (empty($fromLocation) || empty($toLocation)) {
            // Handle empty fields
            header('Location: home.html?error=empty_fields');
            exit;
        }

        // Perform availability check logic
        $availabilityMessage = checkAvailability($fromLocation, $toLocation);

        if ($availabilityMessage === "available") {
            // Insert data into the database
            $query = $conn->prepare("INSERT INTO deliveries (from_location, to_location) VALUES (?, ?)");
            $query->bind_param("ss", $fromLocation, $toLocation);

            if ($query->execute()) {
                // Redirect to a success page or display a success message
                header('Location: size.html');
                exit;
            } else {
                // Handle insert failure
                header('Location: home.html?error=insert_failed');
                exit;
            }

            $query->close();
        } else {
            // Display the availability message
            echo $availabilityMessage;
        }
    } else {
        // If 'from-location' or 'to-location' is not set in $_POST
        echo "Error: Please select both pick-up and delivery locations.";
    }
} else {
    // If someone tries to access this script directly, handle the error
    echo "Error: Access denied.";
}

$conn->close();

// Function to check availability
function checkAvailability($from, $to) {
    // Example: You might have a database query or external API call here
    // For demonstration, we'll simulate availability based on hardcoded conditions
    $availableRoutes = array(
        "Bangalore" => array("Shivamogga", "Mysore", "Belagavi"),
        "Shivamogga" => array("Bangalore", "Mysore"),
        "Mysore" => array("Bangalore", "Shivamogga"),
        // Add more routes as needed
    );

    // Check if the route is available
    if (isset($availableRoutes[$from]) && in_array($to, $availableRoutes[$from])) {
        return "available";
    } else {
        return "Sorry, delivery from $from to $to is not available.";
    }
}
?>
