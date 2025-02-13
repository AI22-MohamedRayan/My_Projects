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
    // Check if 'product-name' and 'product-size' are set in $_POST
    if (isset($_POST['product-name']) && isset($_POST['product-size'])) {
        // Retrieve form data
        $productName = $_POST['product-name'];
        $productSize = $_POST['product-size'];

        // Validate input data
        if (empty($productName) || empty($productSize)) {
            // Handle empty fields
            header('Location: size.html?error=empty_fields');
            exit;
        }

        // Insert data into the database
        $query = $conn->prepare("INSERT INTO products (product_name, product_size) VALUES (?, ?)");
        $query->bind_param("sd", $productName, $productSize);

        if ($query->execute()) {
            // Perform logic to find compatible vehicles based on product details
            $compatibleVehicles = findCompatibleVehicles($productSize);

            // Output the results
            if (!empty($compatibleVehicles)) {
                echo "<h2>Compatible Vehicles for $productName ($productSize Tons)</h2>";
                echo "<ul>";
                foreach ($compatibleVehicles as $vehicle) {
                    echo "<li>$vehicle</li>";
                }
                echo "</ul>";
            } else {
                echo "No compatible vehicles found for $productName ($productSize Tons)";
            }
        } else {
            // Handle insert failure
            header('Location: size.html?error=insert_failed');
            exit;
        }

        $query->close();
    } else {
        // If 'product-name' or 'product-size' is not set in $_POST
        echo "Error: Please enter both product name and size.";
    }
} else {
    // If someone tries to access this script directly, handle the error
    echo "Error: Access denied.";
}

$conn->close();

// Function to find compatible vehicles
function findCompatibleVehicles($productSize) {
    // Example: You might have a database query or external API call here
    // For demonstration, we'll simulate compatible vehicles based on hardcoded conditions
    $compatibleVehicles = [];

    if ($productSize <= 3) {
        $compatibleVehicles = ["Small Truck", "Van"];
    } elseif ($productSize > 3 && $productSize <= 10) {
        $compatibleVehicles = ["Medium Truck", "Pickup Truck"];
    } elseif ($productSize > 10) {
        $compatibleVehicles = ["Large Truck", "Trailer"];
    }

    return $compatibleVehicles;
}
?>
