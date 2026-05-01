<?php
session_start();
include("db_connect.php");  // Include database connection

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = trim($_POST["username"]);
    $password = trim($_POST["password"]);

    // Check if user exists
    $stmt = $conn->prepare("SELECT id, password FROM admins WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        $stmt->bind_result($id, $hashed_password);
        $stmt->fetch();
        
        // Verify password
        if (password_verify($password, $hashed_password)) {
            $_SESSION['admin_id'] = $id;
            $_SESSION['username'] = $username;
            header("Location: dashboard.php"); // Redirect to dashboard
            exit();
        } else {
            echo "<script>alert('Invalid username or password!'); window.location.href='index.html';</script>";
        }
    } else {
        echo "<script>alert('Invalid username or password!'); window.location.href='index.html';</script>";
    }

    $stmt->close();
}

$conn->close();
?>
