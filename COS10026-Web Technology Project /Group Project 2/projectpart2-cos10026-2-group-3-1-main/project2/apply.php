<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Job Application Page">
    <meta name="keywords" content="HTML5, tags, forms">
    <meta name="author" content="Quang Huy 106212636">
    <title>The Page For Job Application</title>
    <link rel="icon" type="image/png" href="../images/image.png">
    <link rel="stylesheet" href="../Styles/styles.css">
    <link rel="stylesheet" href="../Styles/fonts.css">    
</head>

<body>
    <?php
    include("header.inc");
    include("nav.inc");
    ?>
    <!--Page Description-->
    <div class="block">
        <h2 class="block-banner">Doanh Nhan Job Application Form</h2>
        <p class="block-container">To indicate your interest, kindly complete the form provided below. All submitted
            information will be
            transmitted directly to management and will not be shared with any external parties.</p>
    </div>
    <!--The information will be transmitted using the POST method and then displayed back with the submitted values.-->
    <form id="form-container" method="post" action="process_eoi.php" novalidate>
        <!--Collecting personal information-->
        <fieldset class="firstsection">
            <div class="form-field">
                <h2>Personal Information</h2>
                <p>Kindly provide some information about yourself. This enables us to become better acquainted with
                    you
                    and
                    facilitates future communication should your application be approved.</p>
            </div>
            <!--First Name-->
            <div class="form-field">

                <label for="firstname" class="form-info">First Name</label>
                <input class="input-text" type="text" name="firstname" id="firstname" class="form-info" pattern="^[A-Za-z]+$"
                    maxlength="20" placeholder="e.g.Thong" required>
            </div>

            <!--Last Name-->
            <div class="form-field">

                <label for="lastname" class="form-info">Last Name</label>
                <input class="input-text" type="text" name="lastname" id="lastname" class="form-info" pattern="^[A-Za-z]+$"
                    maxlength="20" placeholder="e.g.Chung" required>
            </div>

            <!--Email Address-->
            <div class="form-field">

                <label for="email" class="form-info">Email Address</label>
                <input class="input-text" type="email" name="email" id="email" class="form-info"
                     placeholder="e.g. user@gmail.com" required>
            </div>

            <!--Phone number-->
            <div class="form-field">

                <label for="phone" class="form-info">Phone Number</label>
                <input class="input-text" type="text" name="phonenumber" id="phone" class="form-info" pattern="^[\d ]{8,12}$"
                    placeholder="e.g 0123456789" required>
            </div>

            <!--Date of Birth-->
            <div class="form-field">

                <label for="dateofbirth" class="form-info">Date of Birth</label>
                <input class="input-text" type="date" name="dateofbirth" id="dateofbirth" class="form-info"
                    pattern="^(0[1-9]|[12]\d|3[01])\/(0[1-9]|1[0-2])\/\d{4}$" placeholder="DD/MM/YYYYY" required>
            </div>

            <!--Gender-->
            <fieldset>

                <legend>Gender</legend>
                <div class="form-gender">

                    <label for="male" class="form-ratio">Male</label>
                    <input type="radio" name="gender" value="male" id="male" class="ratio" required>
                </div>
                <div class="form-gender">

                    <label for="female" class="form-ratio">Female</label>
                    <input type="radio" name="gender" id="female"value="female" class="ratio" required>
                </div>
                <div class="form-gender">

                    <label for="others" class="form-ratio">Others</label>
                    <input type="radio" name="gender" id="others" value="others" class="ratio" required>
                </div>


            </fieldset>
        </fieldset>
        <fieldset class="form-address">
            <!--Information about Address-->
            <div class="form-add">
                <h2>Address</h2>
                <p>Please provide your place of residence.</p>
            </div>
            <!--Street Address-->
            <div class="form-add">

                <label for="streetaddress">Street Address</label>
                <input class="input-text" type="text" name="streetaddress" id="streetaddress" pattern="^{1,40}$" maxlength="40"
                    placeholder="e.g 48 Argent Street" required>
            </div>
            <!--Town-->
            <div class="form-add">

                <label for="town">Town</label>
                <input class="input-text" type="text" name="town" id="town" pattern="^{1,40}$" maxlength="40" placeholder="e.g BrokenHill">
            </div>

            <!--State-->
            <div class="form-add">

                <label for="state">State</label>
                <select class="select" name="state" id="state" required>
                    <option value="">Please Select a State</option>
                    <option value="VIC">VIC</option>
                    <option value="NSW">NSW</option>
                    <option value="QLD">QLD</option>
                    <option value="NT">NT</option>
                    <option value="WA">WA</option>
                    <option value="SA">SA</option>
                    <option value="TAS">TAS</option>
                    <option value="ACT">ACT</option>

                </select>
            </div>

            <!--Postcode-->
            <div class="form-add">

                <label for="postcode">Postcode</label>
                <input class="input-text" type="text" name="postcode" id="postcode"
                    pattern="^(0[2-9][0-9]{2}|[1-8][0-9]{3}|9[0-8][0-9]{2}|99[0-3][0-9]|994[0-4])$" maxlength="4"
                    placeholder="e.g 1000">
            </div>

        </fieldset>
        <!--Position Selecting-->
        <fieldset class="form-position">
            <!--Position description-->
            <div class="form-pos">
                <h2>Position Information</h2>
                <p>Choose your preferred position and highlight the skills you have developed over your years of
                    experience in the industry.</p>
            </div>
            <!--Job References List-->
            <div class="form-pos">

                <label for="job">Job Preference Number</label>
                <select class="select" name="job" id="job" required>
                    <option value="">Please Select</option>
                    <option value="DN01">DN1-Software Developer</option>
                    <option value="DN02">DN2-Data Engineer</option>
                </select>
            </div>
            <!-- Required Experience List (Checkboxes) -->
            <div class="form-pos">
                <input class="input-checkbox" type="checkbox" name="python" id="python" required>
                <label for="python"><strong>3&#43;</strong> years with <em>Python/Java/C#</em></label>
            </div>
            <!--2 years of Experience with frontend frameworks-->
            <div class="form-pos">

                <input class="input-checkbox" type="checkbox" name="frontend" id="frontend">
                <label class="label" for="frontend"><strong>2&#43;</strong>years of experience with
                    <em>frontend frameworks</em></label>

            </div>
            <!--2 years of experience with CI/CD and DevOps tools-->

            <div class="form-pos">

                <input class="input-checkbox" type="checkbox" name="devop" id="devop">
                <label class="label" for="devop"><strong>2&#43;</strong> years of experience with <em>CI/CD and
                        DevOps tools</em></label>

            </div>
            <!--Backend development with Node.js/Django/.NET-->

            <div class="form-pos">
                <input class="input-checkbox" type="checkbox" name="backend" id="backend">
                <label class="label" for="backend">Backend development with Node.js/Django/.NET</label>
            </div>
            <!--Other Skills-->
            <div class="form-pos">
                <label for="otherskill">Other Skills</label>
                <textarea name="others" id="otherskill" rows="10" cols="105"
                    placeholder="Please enter your relavent skills"></textarea>
            </div>
            <div class="agreement">
                <input class="input-checkbox" type="checkbox" id="terms" name="terms" required>
                <label>I accept the <a href="">Terms and Conditions</a></label>
            </div>
        </fieldset>
        <!--Submit button-->

        <div class="form-input">
            <button id="submit-button" form="form-container">Apply</button>
        </div>
    </form>
    <?php
    include("footer.inc");
    ?>
</body>

</html>