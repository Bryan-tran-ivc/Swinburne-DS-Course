<?php
include("connecting-function.php");
$headers = [
    "banner" => '<h2 id="openings-heading" class="block-banner">Currently opening at The Doanh Nhan Group</h2>
                <p class="block-container">See our open roles below for the full position description and the link to apply.</p>',
    "aside" => '<h3 id="available-positions-heading">Available positions</h3>
                <ul>
                    <li class="job"><a href="#software-developer" title="Click to jump to this job!">Software
                            Developer</a></li>
                    <li class="job"><a href="#data-engineer" title="Click to jump to this job!">Data Engineer</a></li>
                </ul>
            
                <h3>Perks for all roles</h3>
                <ul>
                    <li>Competitive wages</li>
                    <li>1 month paid leave (after a year)</li>
                    <li>Flexible working hours</li>
                    <li>Professional development support</li>
                    <li>Free food</li>
                </ul>

                <h3 id="apply-link"><a href="apply.php">Apply now</a></h3>',
    "first_section" => ' <h2 id="about-heading">More about us</h2>
                <p>DoanhNhan is a forward-looking software engineering group built on creativity, teamwork, and a
                    passion for technology. Founded by a group of students and innovators, our goal has always been to
                    turn ideas into impactful solutions that make a real difference in peoples lives.</p>',
    "second_section" => '<h2 id="mission-heading">Our Mission</h2>
                <p>At DoanhNhan, we believe technology should empower people and businesses to reach their full
                    potential. Our mission is to build scalable, secure, and user-friendly software that creates
                    opportunities and shapes the future of digital innovation.</p>'                
];
$jobs = [
[
"title" => '<article id="software-developer" class="position" aria-labelledby="sd-title"><h2 id="sd-title">Software Developer</h2>',
"reference" => '<h3>Reference number: DN-001</h3>',
"salary" => '<h4>Salary range: $150,000 to $200,000</h4>',
"description" => '<p>As a Software Developer at DoanhNhan you will design, develop, test and maintain features that power our products. You will collaborate with designers, product managers and other engineers to turn requirements into reliable, maintainable code.</p>
<p>You"ll participate in code reviews, write unit and integration tests, and help improve our development processes. We value clean code, pragmatic design choices, and engineers who care about the user experience as much as technical elegance.</p>
<p>This position reports to the <span class="superior">Lead Software Engineer</span>.</p>',
"responsibilities" => '<h3>Key responsibilities</h3>
<ol>
<li>Design and implement new features across the product stack</li>
<li>Write tests and maintain the existing codebase for reliability</li>
<li>Collaborate with cross-functional teams to deliver product goals</li>
</ol>',
"skills" => '<h3>Essential skills</h3>
<ul>
<li>2+ years of software development experience</li>
<li>Proficiency in at least one modern language (JavaScript, Python, Java, etc.)</li>
<li>Understanding of web technologies, REST APIs and databases</li>
</ul>
<h3>Preferable</h3>
<ul>
<li>Experience with cloud platforms (AWS/GCP/Azure)</li>
<li>Familiarity with CI/CD and containerization</li>
<li>Strong communication and teamwork skills</li>
</ul>',
"apply" => '<p class="apply-link"><a href="apply.php">Click here to apply now!</a></p>
<p class="back-to-top"><a href="#top">Back to top</a></p>
</article>'
],
[
"title" => '<article id="data-engineer" class="position" aria-labelledby="de-title"><h2 id="de-title">Data Engineer</h2>',
"reference" => '<h3>Reference number: DN-002</h3>',
"salary" => '<h4>Salary range: $200,000 to $250,000</h4>',
"description" => '<p>The Data Engineer will design and maintain data pipelines, ensuring reliable and scalable data flow between systems. You will be responsible for building efficient data architectures that support analytics, reporting, and business intelligence across the organization.</p>
<p>You"ll collaborate closely with data scientists, analysts, and software engineers to optimize data storage, transformation, and access. This role reports to the <span class="superior">Head of Data and Analytics</span>.</p>',
"responsibilities" => '<h3>Key responsibilities</h3>
<ol>
<li>Develop and maintain ETL/ELT data pipelines and architectures</li>
<li>Ensure data quality, consistency, and security across systems</li>
<li>Collaborate with teams to support data-driven decision-making</li>
</ol>',
"skills" => '<h3>Essential skills</h3>
<ul>
<li>Experience with SQL, Python, or Scala</li>
<li>Knowledge of data warehousing and database design</li>
<li>Familiarity with cloud data platforms (AWS, GCP, or Azure)</li>
</ul>
<h3>Preferable</h3>
<ul>
<li>Experience with tools like Apache Spark, Kafka, or Airflow</li>
<li>Understanding of big data technologies and distributed systems</li>
<li>Strong analytical and problem-solving skills</li>
</ul>',
"apply" => '<p class="apply-link"><a href="apply.php">Click here to apply now!</a></p>
<p class="back-to-top"><a href="#top">Back to top</a></p>'
]];
// Check if data already exists in the table
$check_query = "SELECT COUNT(*) as count FROM jobs";
$result = $conn->query($check_query);
$row = $result->fetch_assoc();

if ($row['count'] == 0) {
$stmt_headers = $conn->prepare("
  INSERT INTO jobs (banner, aside, first_section, second_section)
  VALUES (?, ?, ?, ?)
");
if ($stmt_headers) {
    $stmt_headers->bind_param(
        "ssss",
        $headers["banner"],
        $headers["aside"],
        $headers["first_section"],
        $headers["second_section"]
    );
    $stmt_headers->execute();
    $stmt_headers->close();
};

$stmt_jobs = $conn->prepare("
  INSERT INTO jobs (title, reference, salary, description, responsibilities, skills, apply)
  VALUES (?, ?, ?, ?, ?, ?, ?)
");
if ($stmt_jobs) {
    foreach ($jobs as $job) {
        $stmt_jobs->bind_param(
            "sssssss",
            $job["title"],
            $job["reference"],
            $job["salary"],
            $job["description"],
            $job["responsibilities"],
            $job["skills"],
            $job["apply"]
        );
        $stmt_jobs->execute();
    }   
    $stmt_jobs->close();
}
};

?>