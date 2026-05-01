<?php
include("db_connect.php");

$hashed_password = password_hash("admin123", PASSWORD_DEFAULT); // Secure password

$sql = "INSERT INTO admins (username, password) VALUES ('admin', '$hashed_password')";

if ($conn->query($sql) === TRUE) {
    echo "Admin user created successfully!";
} else {
    echo "Error: " . $conn->error;
}

$conn->close();
?>
