<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "user_info";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $payment_method = $_POST['payment-method'];
    $user_email = $_POST['user-email'];

    if (isset($payment_method) && isset($user_email)) {
        $user_result = $conn->query("SELECT Uemail FROM users WHERE Uemail = '$user_email'");

        if ($user_result->num_rows > 0) {
            switch ($payment_method) {
                case 'credit-card':
                    $card_number = $_POST['card-number'];
                    $card_expiry = $_POST['card-expiry'];
                    $card_cvv = $_POST['card-cvv'];
                    $stmt = $conn->prepare("INSERT INTO payments (Uemail, payment_method, card_number, card_expiry, card_cvv) VALUES (?, ?, ?, ?, ?)");
                    $stmt->bind_param("sssss", $user_email, $payment_method, $card_number, $card_expiry, $card_cvv);
                    break;

                case 'paypal':
                    $paypal_email = $_POST['paypal-email'];
                    $stmt = $conn->prepare("INSERT INTO payments (Uemail, payment_method, paypal_email) VALUES (?, ?, ?)");
                    $stmt->bind_param("sss", $user_email, $payment_method, $paypal_email);
                    break;

                case 'bank-transfer':
                    $bank_account = $_POST['bank-account'];
                    $stmt = $conn->prepare("INSERT INTO payments (Uemail, payment_method, bank_account) VALUES (?, ?, ?)");
                    $stmt->bind_param("sss", $user_email, $payment_method, $bank_account);
                    break;

                default:
                    echo json_encode(array('status' => 'error', 'message' => 'Invalid payment method.'));
                    exit();
            }

            if ($stmt->execute()) {
                echo json_encode(array('status' => 'success', 'message' => 'Payment successful.'));
            } else {
                echo json_encode(array('status' => 'error', 'message' => 'Payment failed.'));
            }

            $stmt->close();
        } else {
            echo json_encode(array('status' => 'error', 'message' => 'User not found.'));
        }
    } else {
        echo json_encode(array('status' => 'error', 'message' => 'Missing required parameters.'));
    }
}

$conn->close();
?>
