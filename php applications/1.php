<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
<form method="GET">
<input type="text" name="person">
<button> SUBMIT </button>
</form>

    <?php
    $name = $_GET['person'];
    echo $name." is a handsome boy";

    ?>

</body>
</html>