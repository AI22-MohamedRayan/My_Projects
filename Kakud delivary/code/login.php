<?php
$email = $_POST['username'];
$pass = $_POST['password'];

$con = new mysqli('localhost', 'root', '', 'user_info');

if ($con->connect_error) {
    die('Connection Failed: ' . $con->connect_error);
} else {
    $query = $con->prepare("SELECT * FROM users WHERE Uemail = ?");
    $query->bind_param("s", $email);
    $query->execute();
    $query_result = $query->get_result();
    if ($query_result->num_rows > 0) {
        $data = $query_result->fetch_assoc();
        if ($data['pass'] === $pass) {
            header('Location: home.html');
        } else {
            echo "<div class='er'>Invalid password</div>";
        }
    } else {
        echo "<div class='er'>Invalid email</div>";
    }
}
?>