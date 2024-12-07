-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 07, 2024 at 01:12 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `theshoekeepers`
--

-- --------------------------------------------------------

--
-- Table structure for table `record`
--

CREATE TABLE `record` (
  `SHOE_NUMBER` int(11) NOT NULL,
  `SHOE_NAME` varchar(250) NOT NULL,
  `SHOE_SIZE` int(25) NOT NULL,
  `QUANTITY` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `record`
--

INSERT INTO `record` (`SHOE_NUMBER`, `SHOE_NAME`, `SHOE_SIZE`, `QUANTITY`) VALUES
(1, 'asdf', 34, 34),
(4543, 'jordan 1 south korea', 40, 40),
(6453, 'jordan 4 military black', 45, 35),
(7534, 'jordan 1 low marina blue', 44, 87);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`username`, `password`, `email`) VALUES
('anan7575', '1', 'akta@gmail.com'),
('asta', '123', 'asta@gmail.com'),
('doping', '123', 'doping@gmail.com'),
('gilbert', 'lakers', 'gilbert@gmail.cpom'),
('Gohan123', 'last', 'najo@gmail.com'),
('jame', '123', 'jame@gmail.com'),
('jason', 'jason', 'jason@gmail.com'),
('kaldo', 'kaldo', 'alma@gmail.com'),
('lako', 'pol', 'juju@gmail.com'),
('lance', 'water', 'lance@gmail.co,'),
('lebron', 'james', 'lebron@gmail.com'),
('light', 'love', 'light@gmail.com'),
('rey', 'rey', 'rey@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `record`
--
ALTER TABLE `record`
  ADD PRIMARY KEY (`SHOE_NUMBER`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
