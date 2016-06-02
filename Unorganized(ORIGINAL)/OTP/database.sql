-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Apr 14, 2016 at 03:30 PM
-- Server version: 10.1.10-MariaDB
-- PHP Version: 5.6.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test-login`
--
CREATE DATABASE IF NOT EXISTS `test-login` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `test-login`;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_webmail` varchar(30) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_webmail`, `password`) VALUES
('gowd', '39370a54d0f081e3e122fa09e7cf18d1'),
('pamu', '6eaf7b3b24c9a453e8f88a607b484763');

-- --------------------------------------------------------

--
-- Table structure for table `leave_application`
--

CREATE TABLE `leave_application` (
  `id` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `reason` varchar(9999) NOT NULL,
  `dep_date` date NOT NULL,
  `address` varchar(1000) NOT NULL,
  `mode` text NOT NULL,
  `train` varchar(20) NOT NULL,
  `contact` int(15) NOT NULL,
  `s` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `leave_application`
--

INSERT INTO `leave_application` (`id`, `username`, `reason`, `dep_date`, `address`, `mode`, `train`, `contact`, `s`) VALUES
(10, 'bedapudi', '', '0000-00-00', '', '', '', 0, 0),
(11, 'bedapudi', 'bbbb', '0000-00-00', '', '', '', 0, 0),
(12, 'bedapudi', 'kakaka', '0000-00-00', '', '', '', 0, 0),
(13, 'bedapudi', 'aaaaaaabbb', '0000-00-00', '', '', '', 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `leave_application_temp`
--

CREATE TABLE `leave_application_temp` (
  `username` varchar(50) NOT NULL,
  `reason` varchar(9999) NOT NULL,
  `dep_date` date NOT NULL,
  `address` varchar(1000) NOT NULL,
  `mode` text NOT NULL,
  `train` varchar(20) NOT NULL,
  `contact` int(15) NOT NULL,
  `s` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(130101014, 'bedapudi', '10526ea4f233e8a39b218fc7c29c2a9d'),
(130101026, 'j.bharath', '7616b81196ee6fe328497da3f1d9912d'),
(130101037, 'kodali', '507250b947cc397023a9595001fcf167');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_webmail`);

--
-- Indexes for table `leave_application`
--
ALTER TABLE `leave_application`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `leave_application_temp`
--
ALTER TABLE `leave_application_temp`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `leave_application`
--
ALTER TABLE `leave_application`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
