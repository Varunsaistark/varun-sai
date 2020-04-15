<?php
include 'dbh.inc.php';
$username=$_POST['uname'];
$pass=$_POST['pass'];
$query="SELECT 'id' FROM 'varun2' WHERE 'uname'='$username'AND 'PASSWORD'='$pass'";

$result=mysqli_query($conn,$query);

  $query_num_rows=mysqli_num_rows($result);
  if($query_num_rows==0)
  {
    echo "omg";
  }
  else {

echo "you are welcome";

  }



 ?>
