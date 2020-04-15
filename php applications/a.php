<?php
require_once('PHPMailer/PHPMailerAutoload.php');
$mail=new PHPMailer();
$mail->isSMTP();
$mail->SMTPAuth=true;
$mail->SMTPsecure='ssl';
$mail->Host='smtp.gmail.com';
$mail->Port='587';
$mail->ishtml();
$mail->Username='varunsai8496@gmail.com';
$mail->password='Varunsai@5151';
$mail->setfrom('no-reply@howcode.or');
$mail->Subject='Hello world bro i am just trying ';
$mail->body='a test email';
$mail->AddAddress('mihirabio@gmail.com');

$mail->send();
echo "mail sent ";

?>
