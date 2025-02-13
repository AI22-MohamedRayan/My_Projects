<?php
session_start();

// Initialize session variables if not already set
if (!isset($_SESSION['latitude'])) {
    $_SESSION['latitude'] = 51.5; // Initial latitude
}

if (!isset($_SESSION['longitude'])) {
    $_SESSION['longitude'] = -0.09; // Initial longitude
}

// Simulate updating marker position with random values (replace with your actual logic)
$_SESSION['latitude'] += (rand(-100, 100) / 10000); // Random change in latitude
$_SESSION['longitude'] += (rand(-100, 100) / 10000); // Random change in longitude

// Return JSON response with current marker position
header('Content-Type: application/json');
echo json_encode([
    'latitude' => $_SESSION['latitude'],
    'longitude' => $_SESSION['longitude'],
]);
?>