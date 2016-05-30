<?php
$output = exec('python mail.py');
$_SESSION['output'] = $output;
?>