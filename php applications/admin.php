<?php
require 'includes/dbh.inc.php';
 ?>
﻿<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title>admin page</title>
    <link rel="stylesheet" href="stylesheet.css" />
</head>
<body>

      <div class="box">
          <h2> LOGIN</h2>
          <form   action="includes/verify.php" method="POST">
              <div class="inputbox">
                  <input type="text" name="uname" required="" />
                  <label> username</label>

              </div>
              <div class="inputbox">
                  <input type="password" name="pass" required="" />
                  <label>password</label>

              </div>
              <input type="submit" name="sub" value="submit" />
              &nbsp
<a href="register.php"> register </a>


<br/>
<br/>
<a href="forgotpassword.php" target="_top"> i forgot my password </a>

      </div>

</body>
</html>
