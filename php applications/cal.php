<!DOCTYPE html>
<html>
<head>
    <title> calculator </title>
</head>
<body>

<form method="GET">

    <input type="number" name="first">
    <input type="text" name="symbol">
    <input type=" number" name="second"> 



<input type="submit" name="submit">



    </form>

    <?php
    $x=$_GET['first'];
    $y=$_GET['symbol'];
    $z=$_GET['second'];
    
	



    if($y=='+')
{
echo $x+$z;
}
else if($y=='-')
{
echo $x-$z;
}
else if($y=='*')
{
echo $x*$z;
}
else if($y=='/')
{
echo $x/$z;
}
else if($y=='%')
{
echo $x%$z;
}
else
{
echo "enter valid symbol";
}


    ?>

</body>
</html>