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
    <!-- this is group logo and group name section -->
    <?php
    include("header.inc");
    include("nav.inc");
    ?>
    <div>
        <img class="background-image" src="../images/image2.png" alt="">
    </div>
    <!-- overview about our company -->
    <div class="head-information">
        <div class="head-borderline">
            <h2>Welcome to Doanh Nhan</h2>
            <p class="head-information-p">If you love coding, solving problems, and turning ideas into reality, this is where your journey begins.
                At Doanh Nhan, we believe that software engineering is more than just writing code—it's about creating
                solutions
                that impact lives and shape the future.</p>
        </div>
    </div>
    <div class="picture-section-container">
        <!-- high-salary jobs introdution section -->
        <div class="picture-section-1">
            <div class="section-1-information">
                <h3>A Well-Paid Profession</h3>
                <p class="section-1-p">Software engineers are among the most in-demand professionals in today's digital
                    world.
                    With competitive salaries, the job offers financial stability and growth.
                    At Doanh Nhan, we recognize talent and ensure that your efforts are rewarded fairly.</p>
            </div>
            <div class="picture-container">
                <img class="image-section-1" src="../images/image3.png" alt="">
            </div>
        </div>
        <!-- opportunities for promotion section -->
        <div class="picture-section-2">
            <div class="picture-container">
                <img class="image-section-2" src="../images/image4.png" alt="">
            </div>
            <div class="section-1-information">
                <h3>Opportunities for Promotion</h3>
                <p class="section-2-p">In this field, your career path is only limited by your ambition.
                    Starting as a junior developer, you can advance to senior engineer, team leader, or even a project
                    manager.
                    At Doanh Nhan, we encourage continuous learning and provide clear pathways for promotion, so you're
                    always moving forward.</p>
            </div>
        </div>
    </div>
    <!-- hiring section -->
    <div class="hiring-section-container">
        <div class="hiring-section-h2">
            <h2 class="hiring-h2">We are hiring</h2>
        </div>
        <div class="hiring-section">
            <img class="hiring-picture-section" src="../images/image5.png" alt="">
            <div class="hiring-information-section">
                <p>Doanh Nhan is always looking for passionate, skilled, and motivated individuals to join our team.
                    We hold regular hiring sessions for fresh graduates and experienced professionals alike.
                    If you have the passion for coding and the drive to grow, there's a place for you here.</p>
                <a href="apply.php">Join now</a>
            </div>
        </div>
    </div>
    <?php
    include("footer.inc");
    ?>
</body>

</html>