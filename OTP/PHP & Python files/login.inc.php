<?php
if(isset($_POST['username'])&&isset($_POST['password']))
{
$username = $_POST['username'];
$password = $_POST['password'];
$password_hash=md5($password);
 
//echo $password_hash;
 
if(!empty($username)&&!empty($password))
{
$query = mysql_query("SELECT * FROM users WHERE username ='".$username."' AND password ='".$password_hash."'") or die(mysql_error()); 
 
$data = mysql_fetch_array($query);
 
$test=$data['password'];
 
$query_run=$query;
$query_num_rows = mysql_num_rows($query_run);
if($query_num_rows==0)
{
echo 'Invadid username/password combination.';
}
else if($query_num_rows==1)
{
$output = exec('python mail.py');
$_SESSION['output'] = $output;
$time_pre = microtime(true);
$_SESSION['time_pre'] = $time_pre;
echo 'ok';
$user_id= mysql_result($query_run,0,'id');
$user_id=$data['id'];
$_SESSION['user_id'] = $user_id;
header("Location:".$_SERVER['PHP_SELF']. " ");
}
{
}
 
}
else
{
echo 'You must supply a username and password';
}
 
}
 
?>
<div align="center">
<form action="<?php echo $current_file; ?>" method="POST">
Username: <input type="text" name="username"> Password: <input type="password" name="password">
<input type="submit" value="Log in">
</form>
</div>