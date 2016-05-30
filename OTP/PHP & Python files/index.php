<?php 
require 'core.inc.php';
require 'connection.inc.php';

if(loggedin())
{  
	 $rightvar=$_SESSION['user_id'];
	 $output = $_SESSION['output'];
	 echo $output;
	 $time_pre = $_SESSION['time_pre'];
	 #echo $time_pre;
	 $result = mysql_query("SELECT * FROM users WHERE id = $rightvar") or die(mysql_error());  
				   $data = mysql_fetch_array($result);  
	   $username=$data['username'];
	   $userid=$data['id'];
		
	   echo 'Welcome! ' . $username . '<a  href="logout.php"><input type="button"  value="Logout"/></a>';
	?>
	   
	<div align="center">
		<form action="<?php echo $current_file; ?>" method="POST">
		OTP: <input type="text" name="otp">
		<input type="submit" value="submit">
		</form>
	</div>
	
	<?php 
	 if(isset($_POST['otp']))
		{
			$time_post = microtime(true);
			$exec_time = $time_post - $time_pre;
			if($exec_time>1800)
			{
				header('Location: logout.php');
			}
			else
			{
				$otp = $_POST['otp'];
				if($otp == $output)
				{
				$output = 0;
				$_SESSION['output'] = $output;
				header('Location: verify.php');
				}
				else
				{
					header('Location: index.php');
				}
				
			}
			
		}
 }


 
 

else
	{
	include 'login.inc.php';
	}

?>
