<?php
function connectDatabase(){
    require_once("settings.php");
    $conn = mysqli_connect($hostname,$user,$password,$database);
   if(!$conn){
    die("Connection failed: " . mysqli_connect_error());
   }
   return $conn;
};
$conn = connectDatabase();
?>