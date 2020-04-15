
<?php
if(isset($_POST['sub']))
{
require 'dbh.inc.php';

$first=$_POST['uname'];
$second=$_POST['email'];
$third=$_POST['pass'];
$fourth=$_POST['number'];
$vkey=md5(time().$first);
if($_POST['pass1']!==$third)
{
  header("location: ../register.php?passwordsdidntmatch&uname=".$first);
}
else
{
  $third=md5($third);
  $sql="SELECT id FROM varun2 WHERE uname=?";
  $stmt=mysqli_stmt_init($conn);
  if(!mysqli_stmt_prepare($stmt,$sql))
  {
    header("Location: ../register.php?error=sqerror");
    exit();
  }
  else {
    mysqli_stmt_bind_param($stmt,"s",$first);
mysqli_stmt_execute($stmt);
mysqli_stmt_store_result($stmt);
$resultcheck=mysqli_stmt_num_rows($stmt);
if($resultcheck>0)
{
  header("Location: ../register.php?error=usernametaken");
  exit();
}

else {
  $sql= "INSERT INTO varun2 (uname,email,PASSWORD,number,vkey)
  VALUES('$first','$second','$third','$fourth','$vkey');";
   mysqli_query($conn,$sql);

$to= $second;
$subject=" email verification";
$message="< a href='http://localhost/registartion/verify.php?vkey=$vkey>register</a>';
$headers=" FROM: varunsai8496@gmail.com";
mail($to,$subject,$message,$headers);
  header("Location: ../mail.php?signupsuccess");
}
  }
}


}

else {
  header("Location: ../register.php");
}

 ?>
