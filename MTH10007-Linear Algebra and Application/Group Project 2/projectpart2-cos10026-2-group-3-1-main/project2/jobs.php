<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../Styles/styles.css">
    <link rel="stylesheet" href="../Styles/fonts.css">
    <link rel="icon" type="image/png" href="../images/image.png">
    <title>Document</title>
</head>
<body>
    <?php
    include("header.inc");
    include("nav.inc");
    include("jobs-html.php");
    ?>
    <!-- php section -->
     <?php
        $header = mysqli_query($conn,"SELECT banner,aside,first_section,second_section FROM jobs");
        $row = mysqli_fetch_assoc($header);
        echo '<div class="block" aria-labelledby="openings-heading">' . $row['banner'] .'</div>';
        echo '<aside class="aside" aria-labelledby="available-positions-heading">' .$row['aside'] . '</aside>';
        echo '<section id="about" aria-labelledby="about-heading">'.$row['first_section'].'</section>';
        echo '<section id="our-mission" aria-labelledby="mission-heading">'.$row['second_section']. '</section>';
     for ($i = 2; $i < (count($jobs) + 2); $i++) {
        $job = mysqli_query($conn,"SELECT title,reference,salary,description,responsibilities,skills,apply FROM jobs WHERE id = $i");
        $row = mysqli_fetch_assoc($job); 
        echo $row['title'];
        echo $row['reference'];
        echo $row['salary'];
        echo '<div class="job-basic-info">'.$row['description'].'</div>';
        echo '<div class="responsibilities">'.$row['responsibilities'].'</div>';
        echo '<div class="skills">'.$row['skills'].'</div>';
        echo $row['apply'].'</article>';
     };
     ?>
    <?php
    include("footer.inc");
    ?>
</body>
</html>