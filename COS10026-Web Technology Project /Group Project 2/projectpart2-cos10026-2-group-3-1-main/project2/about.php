<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../Styles/styles.css">
    <link rel="stylesheet" href="../Styles/fonts.css">
    <link rel="icon" type="image/png" href="../images/image.png">
    <title>About Us</title>
</head>

<body>
    <?php
    include("header.inc");
    include("nav.inc");
    ?>
    <!-- Page Description Section-->

    <div class="block">
        <h2 class="block-banner"> Contact us</h2>
        <p class="block-container">Meet our team and find the right person to contact for your needs.
            Get in touch with us for support, inquiries, or collaboration opportunities.</p>
    </div>
    <!--Group Details Secion-->
    <div class="group-info-section">
        <div class="group-basic-info-table">
            <table>
                <tbody>
                    <tr>
                        <th>Group name</th>
                        <td>DoanhNhan</td>
                    </tr>
                    <tr>
                        <th>Class</th>
                        <td>COS10026.2</td>
                    </tr>
                    <tr>
                        <th>Day &amp; Time</th>
                        <td>Tuesday, 13:00 - 16:00</td>
                    </tr>
                    <tr>
                        <th>Campus</th>
                        <td>HCMC Campus</td>
                    </tr>
                    <tr>
                        <th>Tutor</th>
                        <td>Mr. Hoang Nguyen</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="get-to-know-us-section">
        <div class="member-cards">
            <div class="contribution-container" id='team-leader'>
                <img src="../images/thong.png" alt="Chung Hien Thong">
                <h3>Chung Hien Thong<br>106212681</h3>
                <p>Front-End</p>
                <ul>
                    <li>Home Page</li>
                    <li>CSS file</li>
                    <li>Job Apllication Page</li>
                    <li>Job Description Page</li>
                    <li>Question Poster</li>
                </ul>
                <p>Back-end</p>
                <ul>
                    <li>Enhancement Page</li>
                    <li>Process_eoi.php Page</li>
                    <li>Connect and Setting</li>

                </ul>
            </div>
            <div class="contribution-container">
                <img src="../images/huy.png" alt="Tran Quang Huy">
                <h3>Tran Quang Huy<br>106212636</h3>
                <p>Front-End</p>
                <ul>
                    <li>Job Application Page</li>
                    <li>CSS file</li>
                    <li>Home Page</li>
                    <li>Question Poster</li>
                </ul>
                <p>Back-end</p>
                <ul>
                    <li>Manage.php</li>
                    <li>Login.php</li>
                    <li>Manager_registration</li>
                    <li>Logout.php</li>
                </ul>
            </div>
            <div class="contribution-container">
                <img src="../images/dan.png" alt="Nguyen Nhat Dan">
                <h3>Nguyen Nhat Dan<br>105731402</h3>
                <p>Front-End</p>
                <ul>
                    <li>Group Details Page</li>
                    <li>CSS file</li>
                    <li>Home Page</li>
                    <li>Question Poster</li>
                </ul>
                <p>Back-end</p>
                <ul>
                    <li>About.php Page</li>
                    <li>EOI table creation</li>
                    <li>Enhancement.php</li>

                </ul>
            </div>
            <div class="contribution-container">
                <img src="../images/khang.png" alt="Dang Gia Khang">
                <h3>Dang Gia Khang<br>105992199</h3>
                <p>Front-End</p>
                <ul>
                    <li>Job Description Page</li>
                    <li>Job Application Page</li>
                    <li>CSS file</li>
                    <li>Question Poster</li>
                </ul>
                <p>Back-end</p>
                <ul>
                    <li>Jobs.php Page</li>
                </ul>
            </div>
        </div>
    </div>

    <!--Group Image & Interests Secion-->
    <div class="group-image-interests-container">
        <h2 class="caption-container">Our team and interests</h2>
        <div class="group-image-interests">
            <div class="group-image-container">
                <img class="group-image" src="../images/group-photo.png" alt="group-image">
            </div>
            <table class="group-interests">
                <tbody>
                    <tr>
                        <th>Name</th>
                        <th>Hobby 1</th>
                        <th>Hobby 2</th>
                        <th>Hobby 3</th>
                    </tr>
                    <tr>
                        <th>Thong Chung</th>
                        <td>Playing electric guitar</td>
                        <td>Hiphop/R&B</td>
                        <td>Reading Manga</td>
                    </tr>
                    <tr>
                        <th>Huy Tran</th>
                        <td>Playing triple A games</td>
                        <td>Watching streams</td>
                        <td>Badminton &amp; Football</td>
                    </tr>
                    <tr>
                        <th>Dan Nguyen</th>
                        <td>Gym</td>
                        <td rowspan="2">Basketball</td>
                        <td>Travelling</td>
                    </tr>
                    <tr>
                        <th>Khang Dang</th>
                        <td>Playing Arena of Valor</td>
                        <td>Roblox</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <!--Footer Section-->
    <?php
    include("footer.inc");
    ?>

</body>

</html>