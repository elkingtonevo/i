// php registration form

<?php

	// $string = "MAAD";
	// echo htmlspecialchars($string);

	$firstName = $_POST['firstname'];
	$lastName = $_POST['lastname'];

	// if(!empty($_POST['firstname']) && !empty($_POST['lastname']))
	if(isset($_POST['submit']))
	{
		print "<h2>{MAAD City}</h2>";
	}
	else
	{
		print "<h2>{Coming}</h2>";
	}

?>