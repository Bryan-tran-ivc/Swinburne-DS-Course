<?php
session_start();
include("header.inc");
include("nav.inc");
include("connecting-function.php");
// Storing error notifications
$msg = "";
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST['username']);
    $password = $_POST['password'];
    // Find username in managers table
    $query = "SELECT * FROM managers WHERE username = '$username'";
    $result = mysqli_query($conn, $query);
    //If precisely one matching username found
    if (mysqli_num_rows($result) == 1) {
        $user = mysqli_fetch_assoc($result);

        // Check if the account is currently locked
        if ($user['lockout_time'] && strtotime($user['lockout_time']) > time()) {
            // Account still locked (lockout time is in the future)
            $remaining = ceil((strtotime($user['lockout_time']) - time()) / 60);
            $msg = "<p class='error'>Account locked. Try again in $remaining minute(s).</p>";
        } else {
            // Account not locked --> verify password
            if (password_verify($password, $user['password_hash'])) {
                // Reset failed attempts and clear lockout time
                mysqli_query($conn, "UPDATE managers SET failed_attempts = 0, lockout_time = NULL WHERE id = {$user['id']}");
                // Save login status in session variables
                $_SESSION['manager_logged_in'] = true;
                $_SESSION['username'] = $username;
                // Redirect to the manage page
                header("Location: manage.php");
                exit();
            } else {
                //Password is incorrect --> increment failed attempts
                $attempts = $user['failed_attempts'] + 1;
                // If failed 3 or more times → lock the account for 5 minutes
                if ($attempts >= 3) {
                    $lockout_time = date("Y-m-d H:i:s", strtotime("+5 minutes"));
                    mysqli_query($conn, "UPDATE managers SET failed_attempts = $attempts, lockout_time = '$lockout_time' WHERE id = {$user['id']}");
                    $msg = "<p class='error'>Too many failed attempts. Account locked for 5 minutes.</p>";
                } else {
                    // Not yet locked --> just update failed attempts count
                    mysqli_query($conn, "UPDATE managers SET failed_attempts = $attempts WHERE id = {$user['id']}");
                    $msg = "<p class='error'>Invalid credentials. Attempt $attempts of 3.</p>";
                }
            }
        }
    } else {
        $msg = "<p class='error'>Username not found.</p>";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="description" content="HR Login page">
<meta name="author" content="Quang Huy 106212636">
<title>Doanh Nhan | Login EOIs</title>
<link rel="stylesheet" href="../Styles/styles.css">
<link rel="stylesheet" href="../Styles/fonts.css">   
<link rel="icon" type="image/png" href="../images/image.png"> 
</head>
<body class="dn-hr-body">
<div class="dn-hr-container">
    <h2>Manager Login</h2>
    <?= $msg ?>
    <form method="post" class="dn-hr-form">
        <label>Username</label>
        <input class="dn-hr-input" type="text" name="username" required>
        <label>Password</label>
        <input class="dn-hr-input" type="password" name="password" required>
        <button class="dn-hr-button" type="submit">Login</button>
    </form>
    <p>Don't have an account? <a href="manager_registration.php">Register here</a></p>
</div>
</body>
</html>