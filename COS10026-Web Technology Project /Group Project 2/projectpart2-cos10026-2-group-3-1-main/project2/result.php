<?php
session_start();
include("header.inc");   
include("nav.inc");
// Receive session data
$errors = [];
$eoiNumber = null;

if (isset($_SESSION['errors'])) {
    $errors = $_SESSION['errors'];
}

if (isset($_SESSION['eoiNumber'])) {
    $eoiNumber = $_SESSION['eoiNumber'];
}
// Clear session data
unset($_SESSION['errors']);
unset($_SESSION['eoiNumber']);
?>
<!DOCTYPE html>
<html lang ='en'>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Application Result</title>
    <link rel="icon" type="image/png" href="../images/image.png">
    <link rel="stylesheet" href="../Styles/styles.css">
    <link rel="stylesheet" href="../Styles/fonts.css">
    <link rel="icon" type="image/png" href="../images/image.png"> 
</head>
<body class="result_page">
     <div class="block-result">
        <h2 class="block-banner">Result</h2>
    </div>
    <?php
    if (count($errors) > 0) {
        echo '<div class="container">';
        echo '<div class="result-container">';
        echo '<h1 class="Uncuccess"> Apply unsuccessful</h1>';
        echo '<div class="left-container">';
        echo '<h2 class="result_h2">There were issues with your application:</h2>';
        foreach ($errors as $error) {
            echo '<div class="error_list_container">';
            echo '<ul class="result-ul">';
            echo '<li class="error_list">' . htmlspecialchars($error) . '</li></div>';
        }
        echo '</ul>';
        echo '</div><a href="apply.php"><button class="result-button">back</button></a>';
        echo '</div></div>';
    } else {
        echo '<div class="container">';
        echo '<div class="result-container">';
        echo '<h1 class="successfull">Apply successful</h1>';
        echo '<div class="left-container">';
        echo '<h2 class="result_h2">Application Submitted Successfully!</h2>';
        echo '<p>Your EOI Number is: <strong> <span style = "color:blue;">' . htmlspecialchars(str_pad($eoiNumber, 5, "0", STR_PAD_LEFT)) . '</span></strong></p>';
        echo '</div><a href="apply.php"><button class="result-button">back</button></a>';
        echo '</div></div>';
    }
    include("footer.inc");
    ?>

</body>
</html>


