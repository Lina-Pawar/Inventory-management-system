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

--
-- Database: `inventory`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `product_id` int(50) NOT NULL,
  `product_name` varchar(150) NOT NULL,
  `product_qty` int(100) NOT NULL,
  `product_price` bigint(100) NOT NULL,
  `total` bigint(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`product_id`, `product_name`, `product_qty`, `product_price`, `total`) VALUES
(7714, 'Football', 50, 300, 15000),
(7920, 'Handball', 49, 200, 10000),
(4481, 'Volleyball', 65, 450, 33750),
(9050, 'Basketball', 49, 500, 25000),
(7648, 'Soft-tennis-ball', 90, 30, 3000),
(1352, 'Hard-tennis-ball', 100, 60, 6000),
(6857, 'Puck', 100, 100, 10000),
(5395, 'Pingpong ball', 200, 20, 4000),
(1062, 'Red season ball', 150, 200, 30000),
(2446, 'White season ball', 200, 250, 50000),
(5368, 'Shuttle cock', 500, 80, 40000),
(8950, 'English willow bat', 40, 2500, 100000),
(2466, 'Kashmir willow bat', 50, 3000, 150000),
(8667, 'Rackets', 50, 450, 27000),
(8351, 'Net', 40, 300, 15000),
(2390, 'cricket kit', 30, 7000, 210000),
(9796, 'Supporter', 200, 150, 30000),
(2075, 'Spikes', 75, 950, 71250),
(4606, 'Skipping rope', 50, 160, 8000);

-- --------------------------------------------------------

--
-- Table structure for table `sales_bill`
--

CREATE TABLE `sales_bill` (
  `username` varchar(50) NOT NULL,
  `items` varchar(200) NOT NULL,
  `date` varchar(10) CHARACTER SET latin1 NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sales_stocks`
--

CREATE TABLE `sales_stocks` (
  `inv_id` int(11) NOT NULL,
  `item_no` int(11) NOT NULL,
  `qty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sales_stocks`
--

INSERT INTO `sales_stocks` (`inv_id`, `item_no`, `qty`) VALUES
(8889, 2248, 10),
(4368, 12, 90),
(9507, 2248, 8),
(7111, 11, 10),
(8505, 58, 1),
(8505, 12, 2),
(8505, 2248, 2),
(8505, 2248, 3),
(2295, 58, 1),
(2295, 12, 1),
(5451, 12, 6),
(6029, 2248, 1),
(3800, 12, 10),
(3800, 2248, 10),
(6043, 9348, 10),
(9822, 9348, 10),
(9822, 9348, 10),
(5108, 9348, 10),
(9360, 9348, 1),
(9891, 9348, 10),
(9936, 9348, 1),
(9691, 9348, 10),
(2502, 9348, 10),
(3620, 9348, 1),
(6988, 8564, 10),
(2651, 8564, 10),
(3398, 4481, 10),
(3398, 7648, 10),
(9968, 8667, 10),
(9968, 8351, 10),
(2115, 7920, 1),
(2568, 9050, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(10) NOT NULL,
  `f_name` varchar(50) NOT NULL,
  `l_name` varchar(50) NOT NULL,
  `mail_id` varchar(100) NOT NULL,
  `que` varchar(50) NOT NULL,
  `answer` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `f_name`, `l_name`, `mail_id`, `que`, `answer`, `password`, `username`) VALUES
(1, 'Lina', 'Pawar', 'lpawar@gmail.com', 'Your favourite movie', 'Resident evil', '2911', 'lina');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` bigint(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
