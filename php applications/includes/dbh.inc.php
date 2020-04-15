<?php
$dbservername ="localhost";
$dbusername = "root";
$dbpassword = "";
$dbname="jarvis";
$conn= mysqli_connect($dbservername,$dbusername,$dbpassword,$dbname);
if(!$conn)
{
  die(mysqli_error());
}

?>
