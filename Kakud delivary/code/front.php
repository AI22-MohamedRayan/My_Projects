<!DOCTYPE html>
<html>
<body>
<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    // Validate email (optional)
    $email = filter_var($_POST["email"], FILTER_VALIDATE_EMAIL);
    
    if ($email === false) {
        // Invalid email
        echo "Please enter a valid email address.";
    } else {
        // Valid email, you can process/save it as needed
        
        // Example: save to a text file
        $file = 'emails.txt';
        
        // Check if the file exists, create it if not
        if (!file_exists($file)) {
            // Create a new file
            file_put_contents($file, "");
        }
        
        // Check if the email already exists in the file
        $emails = file_get_contents($file);
        if (strpos($emails, $email) !== false) {
            echo "This email address is already subscribed.";
        } else {
            // Append the email to the file
            $current = $emails . $email . "\n";
            file_put_contents($file, $current);
            
            // Or you can send it via email
            // mail("your_email@example.com", "New Email Subscription", "Email: " . $email);
            
            // Redirect back to the form page with a success message
            header("Location: front.html?status=success");
            exit();
        }
    }
} else {
    // Redirect to index.html if accessed directly
    header("Location: front.html");
    exit();
}
?>
</body>
</html>
