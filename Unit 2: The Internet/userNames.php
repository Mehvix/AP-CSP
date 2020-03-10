<?php
$link = mysqli_connect("localhost", "root", "", "mysql");

if($link == false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}

$sql = "INSERT INTO names (firstName, lastName) VALUES ('$_POST[firstName]', '$_POST[lastName]')";

if(mysqli_query($link, $sql)){
    echo "Records inserted successfully.";
} else {
    echo "ERROR: Could not exectute $sql. " . mysqli_error($link);
}

mysqli_close($link);
?>
<hr>
<a href="userName.html">Back</a>
