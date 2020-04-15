<?php
include_once 'dbh.inc.php';
$first=$_POST['uname'];
$second=$_POST['pass'];
$sql="SELECT * FROM varun2 WHERE uname=?;";
$stmt=mysqli_stmt_init($conn);
if(!mysqli_stmt_prepare($stmt,$sql))
{
  header("Location: ../admin.php?error=sqerror");
  exit();
}
else {
  mysqli_stmt_bind_param($stmt,"s",$first);
mysqli_stmt_execute($stmt);
mysqli_stmt_store_result($stmt);
$resultcheck=mysqli_stmt_num_rows($stmt);
if($resultcheck==0)
{


echo '<script type="text/javascript">

          window.onload = function () { alert("YOU ARE NOT ALLOWED "); }

</script>';
//header("Location: ../admin.php?error=inalid user");
exit();
}

else {
$sql="SELECT * FROM varun2 WHERE uname=? AND PASSWORD=?;";
$stmt=mysqli_stmt_init($conn);
if(!mysqli_stmt_prepare($stmt,$sql))
{
  header("Location: ../admin.php?error=sqlerror");
  exit();
}
else {
  mysqli_stmt_bind_param($stmt,"ss",$first,$second);
  mysqli_stmt_execute($stmt);
  mysqli_stmt_store_result($stmt);
  $resultcheck=mysqli_stmt_num_rows($stmt);
  if($resultcheck>0)
  {
    echo "welcome boss";
  }
  else {
//    echo "if u have forgotten pass word click this to change your password";
header("Location: ../admin.php?incorrectpassword");

}


}

}


}




 ?>
