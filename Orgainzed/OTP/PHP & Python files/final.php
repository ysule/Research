<?php 
require 'core.inc.php';
require 'connection.inc.php';

if(loggedin())
{  
	 $rightvar=$_SESSION['user_id'];
	 $result = mysql_query("SELECT * FROM users WHERE id = $rightvar") or die(mysql_error());  
				   $data = mysql_fetch_array($result);  
	   $username=$data['username'];
	   $userid=$data['id'];
	/*  
	$query    = mysql_query("SELECT max(id) from leave_application where username= '$username'");
	 $data1 = mysql_fetch_array($query);  
	   $leave_id=$data1['id'];
	   
	$query1    = mysql_query("SELECT reason from leave_application where id= '$leave_id'");
	 $data2 = mysql_fetch_array($query1);  
	   $reason=$data2['reason'];
	*/
	
	   echo ' ' . $username . ' your leave form is succesfully submitted <a  href="logout.php"><input type="button"  value="Logout"/></a>';
	
 }


 
 

else
	{
	header('Location: index.php');
	}

?>
