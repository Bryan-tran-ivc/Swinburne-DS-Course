<?php
include("header.inc");
include("nav.inc");
include("connecting-function.php");
$msg = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST['username']);
    $password = $_POST['password'];

    // Validation (if username has less than 4 characters --> error)
    if (strlen($username) < 4) {
        $msg = "<p class='error'>Username must be at least 4 characters long.</p>";
    // Validation (if password has less than 8 characters, at least 1 uppercase, 1 lowercase and a number --> error)
    } elseif (!preg_match('/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/', $password)) {
        $msg = "<p class='error'>Password must be at least 8 characters long, with uppercase, lowercase, and a number.</p>";
    } else {
        // Check if username exists
        $check = mysqli_query($conn, "SELECT * FROM managers WHERE username = '$username'");
        if (mysqli_num_rows($check) > 0) {
            $msg = "<p class='error'>Username already exists. Choose another one.</p>";
        } 
        // Save new username to the database with password_hash
        else {
            $hashed = password_hash($password, PASSWORD_DEFAULT);
            $insert = mysqli_query($conn, "INSERT INTO managers (username, password_hash) VALUES ('$username', '$hashed')");
            $msg = $insert ? "<p class='success'>Registration successful! You can <a href='login.php'>login</a> now.</p>" : 
            "<p class='error'>Error: ".mysqli_error($conn)."</p>";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Manager Registration</title>
<link rel="stylesheet" href="../Styles/styles.css">
<link rel="stylesheet" href="../Styles/fonts.css">    
<link rel="icon" type="image/png" href="../images/image.png"> 
</head>
<body class="dn-hr-body">
<div class="dn-hr-container">
    <h2>Manager Registration</h2>
    <?= $msg ?>
    <form method="post" class="dn-hr-form">
        <label>Username</label>
        <input type="text" name="username" required class="dn-hr-input">
        <label>Password</label>
        <input type="password" name="password" required class="dn-hr-input">
        <button type="submit" class="dn-hr-button">Register</button>
    </form>
</div>
</body>
</html>