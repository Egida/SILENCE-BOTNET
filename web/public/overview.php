<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

require_once dirname(__DIR__) . '/app/init.php';

if (!User::isAuthenticated()) {
    header('Location:/login.php');
    exit;
}

echo '<h1>Silence Network</h1>';