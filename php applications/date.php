<!DOCTYPE html>
<html>
<head>
	<title>time</title>
</head>
<body>
<?php
$daysofweek = date("w");

switch ($daysofweek) {
	case 1:
		echo "today is monday";
		break;
	case 0:
	echo "today is sunday";
	break;
	case 2:
	echo "today is tuesday";
	break;
	case 3:
	echo "today is wednesday";
	break;
	case 4:
	echo "today is thursday";
	break;
	case 5:
	echo "today is friday";
	break;

	
	default:
	echo "<script type="text/JavaScript">
	promt("today is sunday");
	</script>"
		break;
}
?>
</body>
</html>