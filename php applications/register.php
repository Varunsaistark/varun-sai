<?php
include 'includes/dbh.inc.php';
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
          <h2> REGISTER</h2>
          <form   action="includes/signup.inc.php" method="POST">
              <div class="inputbox">
                  <input type="text" name="uname" required="" />
                  <label> username</label>

              </div>
              <div class="inputbox">
                  <input type="email" name="email" required="" />
                  <label> email</label>

              </div>
              <div class="inputbox">
                  <input type="password" name="pass" required="" />
                  <label>password</label>

              </div>
              <div class="inputbox">
                  <input type="password" name="pass1" required="" />
                  <label>re-enterpass </label>

              </div>
              <div class="inputbox">
                  <input type="number" name="number" required="" />
                  <label>number</label>

              </div>
              <input type="submit" name="sub" value="submit" />

                </form>


      </div>

</body>
</html>
