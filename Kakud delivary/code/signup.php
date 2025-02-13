<?php
$firstName = $_POST['firstName'];
$lastName = $_POST['lastName'];
$email = $_POST['email'];
$password = $_POST['password'];
$confirmPassword = $_POST['confirmPassword'];

$connection = new mysqli('localhost', 'root', '', 'user_info');

if ($connection->connect_error) {
    die('Connection Failed: ' . $connection->connect_error);
} else {
    $query = $connection->prepare("INSERT INTO users(Uemail,Ufname,Ulname,pass) VALUES (?, ?, ?, ?)");
    $query->bind_param("ssss", $email, $firstName, $lastName,$password);
    $query->execute();
    $query->close();
    $connection->close();
    header('Location: login.html');
}
?>

