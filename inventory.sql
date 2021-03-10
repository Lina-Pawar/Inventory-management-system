-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 15, 2020 at 06:06 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- Database: `inventory`

CREATE TABLE `inventory` (
  `product_id` int(5) NOT NULL,
  `product_name` varchar(150) NOT NULL,
  `product_qty` int(5) NOT NULL,
  `product_price` bigint(5) NOT NULL,
  `threshold` INT(5) NOT NULL DEFAULT '10',
  `sales` INT(5) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Data for table `inventory`

INSERT INTO `inventory` (`product_id`, `product_name`, `product_qty`, `product_price`) VALUES
(7714, 'Football', 50, 300),
(7920, 'Handball', 49, 200),
(4481, 'Volleyball', 65, 450),
(9050, 'Basketball', 49, 500),
(7648, 'Soft-tennis-ball', 90, 30),
(1352, 'Hard-tennis-ball', 100, 60),
(6857, 'Puck', 100, 100),
(5395, 'Pingpong ball', 200, 20),
(1062, 'Red season ball', 150, 200),
(2446, 'White season ball', 200, 250),
(5368, 'Shuttle cock', 500, 80),
(8950, 'English willow bat', 40, 2500),
(2466, 'Kashmir willow bat', 50, 3000),
(8667, 'Rackets', 50, 450),
(8351, 'Net', 40, 300),
(2390, 'Cricket kit', 30, 3000),
(9796, 'Supporter', 200, 150),
(2075, 'Spikes', 75, 950),
(4606, 'Skipping rope', 50, 160);

-- Table structure for table `sales_bill`

CREATE TABLE `sales_bill` (
  `bill_no` int(5) NOT NULL,
  `username` varchar(50) NOT NULL,
  `items` varchar(200) NOT NULL,
  `date` varchar(10) CHARACTER SET latin1 NOT NULL,
  `amount` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table structure for table `users`

CREATE TABLE `users` (
  `id` int(5) NOT NULL,
  `f_name` varchar(50) NOT NULL,
  `l_name` varchar(50) NOT NULL,
  `contact` bigint(10) NOT NULL,
  `mail_id` varchar(100) NOT NULL,
  `que` varchar(50) NOT NULL,
  `answer` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `users` (`id`, `f_name`, `l_name`, `contact`, `mail_id`, `que`, `answer`, `password`, `username`) VALUES
(1, 'Lina', 'Pawar', 9970749700, 'lpawar@gmail.com', 'Your favourite movie', 'Resident evil', '2911', 'lina');

ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

-- AUTO_INCREMENT for table `users`

ALTER TABLE `users`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
