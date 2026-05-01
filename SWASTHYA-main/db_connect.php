<?php
$host = "localhost";
$user = "root";  // Default XAMPP username
$password = "";  // Default XAMPP password (leave empty)
$dbname = "admin_db";  // Change to your actual database name

// Create connection
$conn = new mysqli($host, $user, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
