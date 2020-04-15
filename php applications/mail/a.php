<?php
require_once('PHPMailerAutoload');
$mail=new PHPMailer();
$mail->issmtp();
$mail->SMTPAuth=true;
$mail->SMTPsecure='ssl';
$mail->Host='smtp.gmail.com';
$mail->Port='465';
$mail->ishtml();
$mail->Username='varunsai8496@gmail.com';
$mail->password='Varunsai@8496';
$mial->setfrom('no-reply@howcode.org');
$mail->Subject='Hello world bro i am just trying ';
$mail->body='a test email';
$mail->AddAddress('mihirabio@gmail.com');

$mail->send();

?>
