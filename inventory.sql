-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 21, 2021 at 06:20 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ims`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `product_id` int(5) NOT NULL,
  `product_name` varchar(150) NOT NULL,
  `product_qty` int(5) NOT NULL,
  `product_price` bigint(5) NOT NULL,
  `threshold` int(5) NOT NULL DEFAULT '10',
  `sales` int(5) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`product_id`, `product_name`, `product_qty`, `product_price`, `threshold`, `sales`) VALUES
(7714, 'Football', 49, 300, 10),
(7920, 'Handball', 30, 200, 10),
(4481, 'Volleyball', 25, 450, 10),
(9050, 'Basketball', 23, 500, 10),
(7648, 'Soft-tennis-ball', 89, 30, 10),
(1352, 'Hard-tennis-ball', 34, 50, 10),
(6857, 'Puck', 5, 100, 10),
(5395, 'Pingpong ball', 9, 25, 10),
(1062, 'Red season ball', 12, 200, 10),
(2446, 'White season ball', 20, 250, 10),
(5368, 'Shuttle cock', 50, 80, 12),
(8950, 'English willow bat', 35, 1000, 5),
(2466, 'Kashmir willow bat', 48, 1500, 5),
(8667, 'Rackets', 48, 450, 10),
(8351, 'Net', 37, 300, 8),
(2390, 'Cricket kit', 27, 3000, 10),
(9796, 'Supporter', 16, 150, 10),
(2075, 'Spikes', 20, 800, 5),
(4606, 'Skipping rope', 49, 140, 5);

-- --------------------------------------------------------

--
-- Table structure for table `sales_bill`
--

CREATE TABLE `sales_bill` (
  `bill_no` int(5) NOT NULL,
  `username` varchar(50) NOT NULL,
  `items` varchar(200) NOT NULL,
  `date` varchar(10) CHARACTER SET latin1 NOT NULL,
  `amount` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` int(10) NOT NULL,
  `f_name` varchar(50) NOT NULL,
  `l_name` varchar(50) NOT NULL,
  `contact` bigint(10) NOT NULL,
  `mail_id` varchar(100) NOT NULL,
  `que` varchar(50) NOT NULL,
  `answer` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `f_name`, `l_name`, `contact`, `mail_id`, `que`, `answer`, `password`, `username`) VALUES
(1, 'Lina', 'Pawar', 9970749700, 'lpawar@gmail.com', 'Your favourite movie', 'Resident evil', '2911', 'lina');

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
