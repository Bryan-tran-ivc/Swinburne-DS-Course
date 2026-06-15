<?php
session_start();

include("connecting-function.php");

if ($_SERVER["REQUEST_METHOD"] !== "POST") {
    header("Location: apply.php");
    exit();
}

// Sanitize helper
function sanitize_input($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}
// Define fields and sanitize input
$fields = [
    'job', 'firstname', 'lastname', 'email', 'phonenumber',
    'dateofbirth', 'gender', 'streetaddress', 'town',
    'state', 'postcode'
];
$required_data = [];
$non_required_data = [];
foreach ($fields as $field) { 
    $required_data[$field] = sanitize_input($_POST[$field] ?? '');
};
$non_required_data['others'] = sanitize_input($_POST['others'] ?? '');
$required_data['terms'] = isset($_POST['terms']) ? 1 : 0;

$skills_flags = ['python', 'frontend', 'devop', 'backend',];
$skills = [];

foreach ($skills_flags as $skill) {
    $required_data[$skill] = isset($_POST[$skill]) ? 1 : 0;
    if ($required_data[$skill]) {
        $skills[] = ucfirst($skill);
    }
}
// Validation
$errors = [];
// Required fields
foreach ($fields as $field) {
    if (empty($required_data[$field])) {
        $errors[] = ucfirst($field) . " is required.";
    }
}
// Specific validations
if (!preg_match("/^[a-zA-Z]+$/", $required_data['firstname'])) {
    $errors[] = "First name must contain only letters.";
}
if (!preg_match("/^[a-zA-Z]+$/",$required_data['lastname'])) {
    $errors[] = "Last name must contain only letters.";
};
if (!filter_var($required_data['email'], FILTER_VALIDATE_EMAIL)) {
    $errors[] = "Invalid email format.";
}
if (!preg_match("/^\d{10}$/", $required_data['phonenumber'])) {
    $errors[] = "Phone number must be 10 digits.";
}
if (!empty($required_data['dateofbirth'])) {
    $date = DateTime::createFromFormat('Y-m-d', $required_data['dateofbirth']);
    if (!$date || $date->format('Y-m-d') !== $required_data['dateofbirth']) {
        $errors[] = "Date of birth must be a valid date (MM-DD-YYYY).";
    } else {
        $today = new DateTime();
        $age = $today->diff($date)->y;
        if ($age < 18) { 
            $errors[] = "Applicant must be at least 18 years old.";
        }
    }
}; 
$valid_states = ['VIC', 'NSW', 'QLD', 'WA', 'SA', 'TAS', 'ACT', 'NT'];
if (!in_array($required_data['state'], $valid_states)) {
    $errors[] = "Invalid state.";
}
if (!preg_match("/^\d{4}$/", $required_data['postcode'])) {
    $errors[] = "Postcode must be a 4-digit number.";
}
if (empty($skills)) {
    $errors[] = "At least one skill must be selected.";
}
if ($required_data['terms'] != 1) {
    $errors[] = "You must accept the terms and condidtions.";
}
// Prepare and insert record
$skills_str = implode(", ", $skills); 
$stmt = $conn->prepare("
    INSERT INTO eoi (
        JobReferenceNumber, FirstName, LastName, DateOfBirth, Gender,
        StreetAddress, SuburbTown, State, Postcode, EmailAddress,
        PhoneNumber, Skills, OtherSkills, Terms
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
");
$stmt->bind_param(
    "sssssssssssssi",
    $required_data['job'], $required_data['firstname'], $required_data['lastname'],
    $required_data['dateofbirth'], $required_data['gender'], $required_data['streetaddress'],
    $required_data['town'], $required_data['state'], $required_data['postcode'],
    $required_data['email'], $required_data['phonenumber'], $skills_str, $non_required_data['others'],$required_data['terms']
);
$_SESSION['errors'] = $errors;
if (empty($errors)) {
    $stmt->execute();
    $eoiNumber = $stmt->insert_id;
    $_SESSION['eoiNumber'] = $eoiNumber ?? null;
    header("Location:result.php");
    exit();
} elseif (!empty($errors)) {
    header("Location:result.php");
    exit();
};
?>