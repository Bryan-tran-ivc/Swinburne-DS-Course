<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../Styles/styles.css">
    <link rel="stylesheet" href="../Styles/fonts.css">
    <link rel="icon" type="image/png" href="../images/image.png">
    <title>Enhancements</title>
</head>

<body>
    <?php
    include("header.inc");
    include("nav.inc");
    ?>
    <div class="block">
        <h2 class="block-banner"> Enhancements for Project Part 2</h2>
        <p class="block-container">This page lists and explains the enhancements implemented in our PHP Job Application
            System beyond the basic requirements.</p>
    </div>
    <div class="content-section">
        <div class="content-container">
            <h2>Enhanced Database Query Functions</h2>
            <p>
                The manager page was upgraded to handle SELECT, UPDATE, and DELETE SQL queries, enabling efficient EOI
                management.
                Managers can view, update, or remove records directly from the web interface.
                These features were built with PHP and MySQL to ensure secure and dynamic database operations.
            </p>
            <img src="../images/enhancements-db-queries.png" alt="Database Queries Enhancement">
            <p>
                This example code checks if the user selected the list_all action and, if so, runs an SQL query to retrieve all EOIs with non-empty first name, last name, and email fields.
                It then executes the query using <strong> mysqli_query() </strong> to display the results on the manager page.
            </p>
        </div>

        <hr>

        <div class="content-container">
            <h2>Enhanced Security Applications</h2>
            <p>
                Access to <strong> manage.php </strong> is restricted to logged-in managers only, enforced through PHP sessions that verify a user's login status and redirect unauthorized users to <strong> login.php. </strong> 
                To further strengthen security, the system also includes a lockout feature that temporarily blocks access to the login page for five minutes after three failed login attempts, using session variables and timestamps to prevent repeated unauthorized access attempts.
            </p>
            <img src="../images/enhancements-security.png" alt="Code for Security Enhancement">
            <p>
                This code from <strong> login.php </strong> demonstrates the implementation of the account lockout feature.
                It checks the number of failed login attempts and locks the account for five minutes after three unsuccessful tries, providing feedback to the user about the lockout status.
            </p>
        </div>

        <hr>

        <div class="content-container">
            <h2>Server-Side Data Validation and Error Handling</h2>
            <p>
                All form data from <strong> apply.php </strong> and <strong>process_eoi.php </strong> is validated on the server side for correct format for
                name, email, phone number, and job reference.
                Clear error messages are shown when validation fails.
            </p>
            <img src="../images/enhancements-data-validation.png" alt="Code for Data Validation Enhancement">
            <p>
                This code from <strong> process_eoi.php </strong>illustrates the server-side validation checks for various form fields, ensuring that the data meets specified criteria before being processed and stored in the database.
            </p>
        </div>
    </div>

<!--    <div class="conclusion-section">
        <p>
            These enhancements improve the system's security, reliability, and usability, going beyond the basic project requirements.  
        </p>
    </div>-->
    <!--Footer Section-->
    <?php
    include("footer.inc");
    ?>
</body>

</html>