<?php
//this function connect your php code straight to the database, 
//you don't have to write code to connect to the database again.
include("connecting-function.php"); 
// This is for handling manager options
$result = null;
// This is for checking if the form is summited (POST)
if (isset($_POST['action'])) {
    $action = $_POST['action'];
    // List all EOIs
    if ($action == 'list_all') {
        // Query to select all records from the eoi table
        $query = "SELECT * FROM eoi 
                  WHERE FirstName <> '' 
                  AND LastName <> '' 
                  AND EmailAddress <> ''";
        $result = mysqli_query($conn, $query);
    }
    // List EOIs by Job Preference Number
    elseif ($action == 'list_by_job') {
        // Get the job reference number from form input, escape to prevent SQL injection
        $job_ref = mysqli_real_escape_string($conn, $_POST['job_ref']);
        // Query to get all EOIs with the given job reference number
         $query = "SELECT * FROM eoi 
                  WHERE JobReferenceNumber = '$job_ref'
                  AND FirstName <> '' 
                  AND LastName <> '' 
                  AND EmailAddress <> ''";
        $result = mysqli_query($conn, $query);
    }
    // List EOIs by Applicant Name
    elseif ($action == 'list_by_name') {
        // Get first and last name from form input, escaped for safety
        $first = mysqli_real_escape_string($conn, $_POST['first_name']);
        $last = mysqli_real_escape_string($conn, $_POST['last_name']);
        // This is fake condition so the data can be collected flexibly
        $query = "SELECT * FROM eoi WHERE 1=1";
        // If first name is provided, filter by it (partial match using LIKE)
       $query = "SELECT * FROM eoi WHERE 1=1";
        if (!empty($first)) $query .= " AND FirstName LIKE '%$first%'";
        if (!empty($last))  $query .= " AND LastName LIKE '%$last%'";
        $query .= " AND FirstName <> '' AND LastName <> '' AND EmailAddress <> ''";
        $result = mysqli_query($conn, $query);
    }
    // Delete EOIs by Job Preference Number
    elseif ($action == 'delete_by_job') {
        // Get the job reference number to delete EOIs associated with that job
        $job_ref = mysqli_real_escape_string($conn, $_POST['job_ref']);
        // Delete all EOIs where the JobReferenceNumber matches
        $query = "DELETE FROM eoi WHERE JobReferenceNumber = '$job_ref'";
         // Run the query and display a success or error message
        $msg = mysqli_query($conn, $query)
            ? " <p class='success'>All EOIs for job <strong>$job_ref</strong> deleted successfully.</p>"
            : "<p class='error'>Error: " . mysqli_error($conn) . "</p>";
    }
    // Change status of EOIs
    elseif ($action == 'update_status') {
        // Get EOI number and new status from form
        $eoi_id = intval($_POST['eoi_number']);
        $new_status = mysqli_real_escape_string($conn, $_POST['new_status']);
        // Update the status field of the specific EOI
        $query = "UPDATE eoi SET Status = '$new_status' WHERE EOInumber = $eoi_id";
         // Execute query and show confirmation or error
        $msg = mysqli_query($conn, $query)
            ? "<p class='success'>EOI #<strong>$eoi_id</strong> updated to <strong>$new_status</strong>.</p>"
            : "<p class='error'>Error: ".mysqli_error($conn)."</p>";
    }

} 
?>
<?php
// Use to protect manage.php
session_start();
if (!isset($_SESSION['manager_logged_in']) || $_SESSION['manager_logged_in'] !== true) {
    header("Location: login.php");
    exit();
}
?>
<!DOCTYPE html>
<html lang="en">
<head class="dn-hr-html">
    <meta charset="UTF-8">
    <meta name="description" content="HR management page">
    <meta name="author" content="Quang Huy 106212636">
    <title>Doanh Nhan | Manage EOIs</title>
    <link rel="icon" type="image/png" href="../images/image.png">
    <link rel="stylesheet" href="../Styles/styles.css">
    <link rel="stylesheet" href="../Styles/fonts.css">    

</head>
<body class="dn-hr-body-2">
    <header class="dn-hr-header">Doanh Nhan HR Management</header>

    <div class="dn-hr-container">
        <h2>Manage Expressions of Interest (EOI) </h2>

        <?= isset($msg) ? $msg : "" ?>
        
        <form method="post" class="dn-hr-form">
            <h3>1. List all EOIs</h3>
            <button class="dn-hr-button" name="action" value="list_all"> Show ALL EOIs</button>
        </form>
        <form method="post" class="dn-hr-form">
            <h3>2. List EOIs by Job Preference</h3>
            <label class="dn-hr-label">Job Reference Number</label>
            <input class="dn-hr-input" type="text" name="job_ref" placeholder="e.g. DN1" required>
            <button class="dn-hr-button" name="action" value="list_by_job">Search</button>
        </form>
        <form method="post" class="dn-hr-form">
            <h3>3. List EOIs by Applicant</h3>
            <label class="dn-hr-label">First Name</label>
            <input class="dn-hr-input" type="text" name="first_name" placeholder="First name">
            <label class="dn-hr-label">Last Name</label>
            <input class="dn-hr-input" type="text" name="last_name" placeholder="Last name">
            <button class="dn-hr-button" name="action" value="list_by_name">Search</button>
        </form>
        <form method="post" class="dn-hr-form">
            <h3>4. Delete EOIs by Job Preference</h3>
            <label class="dn-hr-label">Job Preference Number</label>
            <input class="dn-hr-input" type="text" name="job_ref" placeholder="e.g DN1" required>
            <button class="dn-hr-button" name="action" value="delete_by_job">Delete</button>
        </form>
        <form method="post" class="dn-hr-form">
            <h3>5. Change Status of an EOI</h3>
            <label class="dn-hr-label">EOI Number</label>
            <input class="dn-hr-input" type="number" name="eoi_number" required>
            <label class="dn-hr-label">New Status</label>
            <select class="dn-hr-select" name="new_status" required>
                <option value="New">New</option>
                <option value="Current">Current</option>
                <option value="Final">Final</option>
            </select>
            <button class="dn-hr-button" name="action" value="update_status">Update Status</button>
        </form>
        <?php 
         if ($result && mysqli_num_rows($result) > 0) {
        echo "<div class='dn-hr-table-wrapper'>";
        echo "<table class='dn-hr-table'><tr>
                <th>EOI Number</th>
                <th>Job Ref</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Status</th>
              </tr>";
        while ($row = mysqli_fetch_assoc($result)) {
            echo "<tr>
                    <td>{$row['EOInumber']}</td>
                    <td>{$row['JobReferenceNumber']}</td>
                    <td>{$row['FirstName']}</td>
                    <td>{$row['LastName']}</td>
                    <td>{$row['EmailAddress']}</td>
                    <td>{$row['PhoneNumber']}</td>
                    <td>{$row['Status']}</td>
                  </tr>";
        }
        echo "</table>";
        echo "</div>";
    } elseif ($result) {
        echo "<p>No records found.</p>";
    }

    mysqli_close($conn);
    ?>  
</div>

 <div class="form-input">
    <form action="logout.php" method="post">
        <button id="submit-button" type="submit">Log Out</button>
    </form>
</div>
</body>
</html>