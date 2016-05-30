<?php 
require 'core.inc.php';
require 'connection.inc.php';

$output = $_SESSION['output'];

if(loggedin() && $output == 0)
{  
	 $rightvar=$_SESSION['user_id'];
	 $result = mysql_query("SELECT * FROM users WHERE id = $rightvar") or die(mysql_error());  
				   $data = mysql_fetch_array($result);  
	   $username=$data['username'];
	   $userid=$data['id'];
	
	echo $output;   
	 $query    = mysql_query("select * from leave_application_temp where username= '$username'");
	 $data1 = mysql_fetch_array($query);  
	   $reason=$data1['reason'];
		
	   echo 'Welcome! ' . $username . '<a  href="logout.php"><input type="button"  value="Logout"/></a>';
	   echo ' please enter the reason for levae in the following box. '; 
	?>
	   
		<div align="center">
			<form action="<?php echo $current_file; ?>" method="POST">
			reason: <input type="text" value="<?php echo '' . $reason . ''; ?>" name="reason1">
			<input type="submit" value="submit">
			</form>
		</div>
	   
	<?php 
	if(isset($_POST['reason1']))
		{
			
			$reason1 = $_POST['reason1'];
			$query    = "INSERT INTO leave_application (username, reason) 
            VALUES('$username', '$reason1')";
			mysql_query($query);
			$sql    = "DELETE FROM leave_application_temp where username = '$username'";
			mysql_query($sql);
			header('Location: final.php');
		}
 }


 
 

else
	{
	header('Location: index.php');
	}

?>
