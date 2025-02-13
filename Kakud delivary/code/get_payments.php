<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "user_info";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if (isset($_GET['email'])) {
    $user_email = $_GET['email'];
    $stmt = $conn->prepare("SELECT payment_method, CASE WHEN payment_method = 'credit-card' THEN CONCAT('Card ending in ', SUBSTRING(card_number, -4)) WHEN payment_method = 'paypal' THEN CONCAT('PayPal: ', paypal_email) WHEN payment_method = 'bank-transfer' THEN CONCAT('Bank Transfer to account ending in ', SUBSTRING(bank_account, -4)) END as details FROM payments WHERE Uemail = ?");
    $stmt->bind_param("s", $user_email);
    $stmt->execute();
    $result = $stmt->get_result();

    $payments = array();
    while ($row = $result->fetch_assoc()) {
        $payments[] = $row;
    }

    if (count($payments) > 0) {
        echo json_encode(array('status' => 'success', 'payments' => $payments));
    } else {
        echo json_encode(array('status' => 'error', 'message' => 'No payments found.'));
    }

    $stmt->close();
} else {
    echo json_encode(array('status' => 'error', 'message' => 'Missing email parameter.'));
}

$conn->close();
?>
