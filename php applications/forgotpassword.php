<! DOCTYPE html>

<html>

<head>

  <title>
    forgotpassword
  </title>
  <style>
  body
{
  background-image:url("temperature_inversion.jpg");
background-size:100% 100%;
}
.bo
{
  text-align:center;
}
.block{
  background-color: black;

}
a{
    background-color:black;
    color:white;
    text-align:center;
    padding:12px;
    text-decoration:none;
    display:inline-block;

}
a:visited {
    background-color: black;
    color: orange;
    text-align: center;
    padding: 12px;
    text-decoration: none;
    display: inline-block;
}
a:hover {
    background-color: white;
    color: black;
    text-align: center;
    padding: 12px;
    text-decoration: none;
    display: inline-block;
}
    a:active {
        background-color: orange;
        color: black;
        text-align: center;
        padding: 12px;
        text-decoration: none;
        display: inline-block;
    }
  .box
  {
    text-align:center;
    background-color: black;
    margin-left: 650px;
    margin-right: 650px;
    color:white;
    padding: 10px;
  }

  </style>

</head>

<body>
  <div class="bo">
  <h1> Forgot Password</h1>
</div>
<div class="block">
  <a class="n" href="info.html" target="_top">ABOUT</a>
  <a style="margin-left: 80px" href="temperatureanalysis.php" target="_top">HOME</a>
  <a style="margin-left:100px" href="admin.php" target="_self">ADMIN</a>
  <a style="margin-left:120px" href="temperatue.html" target="_self">PRSENT TEMPERATURE</a>
</div>
<br/>
<br/>
</br>
<div class="css">
  <div class="box">
      <h2> LOGIN</h2>
      <form   action="includes/mailer.php" method="POST">
          <div class="inputbox">
            <label> pin sent to your mail</label>
            <br/>
              <input type="text" name="pin" required="" />


          </div>
<input type="submit" name="sub" value="submit" />
</div>
</div>

<?php

 ?>


</body>
</html>
