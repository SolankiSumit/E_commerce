-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 07, 2023 at 09:10 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `collegianfootwear_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_login`
--

CREATE TABLE `admin_login` (
  `id` int(100) NOT NULL,
  `username` varchar(20) NOT NULL,
  `Password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_login`
--

INSERT INTO `admin_login` (`id`, `username`, `Password`) VALUES
(2, 'sumit', 'sumit123'),
(3, 'drashti', 'drashti1505');

-- --------------------------------------------------------

--
-- Table structure for table `cart_info`
--

CREATE TABLE `cart_info` (
  `c_id` int(200) NOT NULL,
  `u_id` varchar(200) NOT NULL,
  `p_id` varchar(200) NOT NULL,
  `quantity` text NOT NULL,
  `size_id` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cart_info`
--

INSERT INTO `cart_info` (`c_id`, `u_id`, `p_id`, `quantity`, `size_id`) VALUES
(7, '1', '2', '3', 8);

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `image` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `name`, `image`) VALUES
(2, 'Sports', 'WhatsApp Image 2023-05-03 at 11.14.22 AM.jpeg'),
(3, 'Sneaker', 'WhatsApp Image 2023-04-25 at 6.59.38 PM (1).jpeg'),
(4, 'Flats', 'WhatsApp Image 2023-05-11 at 11.42.27 PM.jpeg'),
(5, 'Loffers', 'WhatsApp Image 2023-05-11 at 11.40.58 PM.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `customer_info`
--

CREATE TABLE `customer_info` (
  `c_id` int(100) NOT NULL,
  `name` varchar(200) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(100) NOT NULL,
  `m_no` varchar(15) NOT NULL,
  `city` text NOT NULL,
  `address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_info`
--

INSERT INTO `customer_info` (`c_id`, `name`, `email`, `password`, `m_no`, `city`, `address`) VALUES
(12, 'sumit', 'solankisumit', '123456', '9033338332', 'rajkot', 'bdiwhdilce'),
(123456, 'sumit', 'sumitsolanki243@gmail.com', '562327283', '9223323222', 'rajkot', 'asbqhiwdiwdw');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `f_id` int(20) NOT NULL,
  `u_id` varchar(20) NOT NULL,
  `subject` text NOT NULL,
  `description` text NOT NULL,
  `f_date` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`f_id`, `u_id`, `subject`, `description`, `f_date`) VALUES
(31, '1', 'home', 'home1', '3/2/21');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` int(5) NOT NULL,
  `name` varchar(150) NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `name`, `password`) VALUES
(1, 'sumit', 'sumit123');

-- --------------------------------------------------------

--
-- Table structure for table `order_item_detail`
--

CREATE TABLE `order_item_detail` (
  `order_item_id` int(200) NOT NULL,
  `order_id` varchar(150) NOT NULL,
  `p_id` varchar(100) NOT NULL,
  `size` varchar(5) NOT NULL,
  `quantity` text NOT NULL,
  `price` varchar(200) NOT NULL,
  `total_price` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_item_detail`
--

INSERT INTO `order_item_detail` (`order_item_id`, `order_id`, `p_id`, `size`, `quantity`, `price`, `total_price`) VALUES
(1, '1', '2', '6', '2', '2100', '4200'),
(2, '1', '4', '7', '3', '3200', '9600'),
(3, '1', '17', '8', '2', '350', '700'),
(4, '2', '11', '8', '3', '1200', '3600'),
(5, '2', '15', '9', '3', '750', '2250'),
(6, '2', '17', '8', '3', '350', '1050');

-- --------------------------------------------------------

--
-- Table structure for table `order_master`
--

CREATE TABLE `order_master` (
  `o_id` int(150) NOT NULL,
  `u_id` varchar(200) NOT NULL,
  `total_qty` varchar(200) NOT NULL,
  `total_price` varchar(150) NOT NULL,
  `adderess` text NOT NULL,
  `o_date` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_master`
--

INSERT INTO `order_master` (`o_id`, `u_id`, `total_qty`, `total_price`, `adderess`, `o_date`) VALUES
(1, '1', '7', '14600', 'Gokul dham society, Powder gali, Goregaun', '01-06-2023'),
(2, '1', '9', '7000', 'rajkot nvjivan school', '01-06-2023');

-- --------------------------------------------------------

--
-- Table structure for table `product_info`
--

CREATE TABLE `product_info` (
  `p_id` int(200) NOT NULL,
  `c_id` bigint(150) NOT NULL,
  `title` varchar(200) NOT NULL,
  `Description` text NOT NULL,
  `color` text NOT NULL,
  `size` varchar(200) NOT NULL,
  `price` varchar(200) NOT NULL,
  `image` text NOT NULL,
  `company` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product_info`
--

INSERT INTO `product_info` (`p_id`, `c_id`, `title`, `Description`, `color`, `size`, `price`, `image`, `company`) VALUES
(2, 2, 'low sneaker', 'abcd', 'green', '8', '2100', 'WhatsApp Image 2023-05-03 at 11.14.22 AM.jpeg', 'air'),
(4, 3, 'bb-1', 'abcdefg', 'blue', '7', '3200', 'WhatsApp Image 2023-04-25 at 6.59.38 PM (1).jpeg', 'border-1'),
(10, 5, 'a-2', 'dwds', 'black', '6 to 10', '650', 'WhatsApp Image 2023-05-11 at 11.41.01 PM (2).jpeg', 'wdqd'),
(11, 2, 'sport', 'jfifiehf', 's-1', '6 to 10', '1200', 'WhatsApp Image 2023-05-11 at 11.40.59 PM.jpeg', 'air'),
(12, 2, 'ccc', 'dwudd', 'white', '8', '1500', 'WhatsApp Image 2023-05-11 at 11.41.00 PM (1).jpeg', 'air'),
(13, 4, 'ccc', 'c-1', 'black', '6 to 10', '250', 'WhatsApp Image 2023-05-11 at 11.42.28 PM (2).jpeg', 'xyz'),
(14, 5, 'a-3', 'wuduwf', 'brown', '6 to 10', '650', 'WhatsApp Image 2023-05-11 at 11.41.01 PM.jpeg', 'wdqd'),
(15, 5, 'l-1', 'lllll', 'brown', '6 to 10', '750', 'WhatsApp Image 2023-05-11 at 11.41.01 PM (2).jpeg', 'wdqd'),
(17, 4, 'c-4', 'vrrfr', 'black', '6 to 10', '350', 'WhatsApp Image 2023-05-11 at 11.42.28 PM (2).jpeg', 'wdqd');

-- --------------------------------------------------------

--
-- Table structure for table `product_size`
--

CREATE TABLE `product_size` (
  `size_id` int(5) NOT NULL,
  `p_id` int(5) NOT NULL,
  `size` varchar(100) NOT NULL,
  `available` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product_size`
--

INSERT INTO `product_size` (`size_id`, `p_id`, `size`, `available`) VALUES
(15, 4, '8', 1),
(16, 2, '6', 1),
(17, 2, '7', 1),
(18, 2, '8', 1),
(19, 4, '7', 1),
(20, 4, '6', 1),
(21, 10, '6', 1),
(22, 10, '7', 1),
(23, 10, '8', 1),
(24, 11, '6', 1),
(25, 11, '7', 1),
(26, 11, '8', 1),
(27, 12, '6', 1),
(28, 12, '7', 1),
(30, 12, '8', 1),
(31, 13, '6', 1),
(32, 13, '7', 1),
(33, 13, '8', 1),
(34, 14, '6', 1),
(35, 14, '7', 1),
(36, 14, '8', 1),
(37, 15, '6', 1),
(38, 15, '7', 1),
(39, 15, '8', 1),
(40, 17, '6', 1),
(41, 17, '7', 1),
(42, 17, '8', 1),
(43, 16, '6', 1),
(44, 16, '7', 1),
(45, 16, '8', 1),
(46, 10, '9', 1),
(47, 15, '9', 1),
(48, 15, '10', 1);

-- --------------------------------------------------------

--
-- Table structure for table `register_tbl`
--

CREATE TABLE `register_tbl` (
  `u_id` int(150) NOT NULL,
  `name` varchar(150) NOT NULL,
  `password` text NOT NULL,
  `e_mail` text NOT NULL,
  `contact` bigint(15) NOT NULL,
  `address` text NOT NULL,
  `city` text NOT NULL,
  `state` text NOT NULL,
  `country` text NOT NULL,
  `pincode` bigint(15) NOT NULL,
  `age` bigint(20) NOT NULL,
  `gender` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register_tbl`
--

INSERT INTO `register_tbl` (`u_id`, `name`, `password`, `e_mail`, `contact`, `address`, `city`, `state`, `country`, `pincode`, `age`, `gender`) VALUES
(1, 'sumit', '1234', 'solankisumit@111', 9033338221, 'sdfghjnbv', 'rajkot', 'gujrat', 'india', 360007, 20, 'male'),
(2, 'meet', '1234', 'meetchavda123@gmail.com', 3747474743, 'frreregegrege', 'regefdfgh', 'hjk', 'rtyui', 360007, 25, 'male');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_login`
--
ALTER TABLE `admin_login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cart_info`
--
ALTER TABLE `cart_info`
  ADD PRIMARY KEY (`c_id`);

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customer_info`
--
ALTER TABLE `customer_info`
  ADD PRIMARY KEY (`c_id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`f_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `order_item_detail`
--
ALTER TABLE `order_item_detail`
  ADD PRIMARY KEY (`order_item_id`);

--
-- Indexes for table `order_master`
--
ALTER TABLE `order_master`
  ADD PRIMARY KEY (`o_id`);

--
-- Indexes for table `product_info`
--
ALTER TABLE `product_info`
  ADD PRIMARY KEY (`p_id`);

--
-- Indexes for table `product_size`
--
ALTER TABLE `product_size`
  ADD PRIMARY KEY (`size_id`);

--
-- Indexes for table `register_tbl`
--
ALTER TABLE `register_tbl`
  ADD PRIMARY KEY (`u_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_login`
--
ALTER TABLE `admin_login`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `cart_info`
--
ALTER TABLE `cart_info`
  MODIFY `c_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `customer_info`
--
ALTER TABLE `customer_info`
  MODIFY `c_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=123457;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `f_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12346;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `order_item_detail`
--
ALTER TABLE `order_item_detail`
  MODIFY `order_item_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `order_master`
--
ALTER TABLE `order_master`
  MODIFY `o_id` int(150) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `product_info`
--
ALTER TABLE `product_info`
  MODIFY `p_id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `product_size`
--
ALTER TABLE `product_size`
  MODIFY `size_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `register_tbl`
--
ALTER TABLE `register_tbl`
  MODIFY `u_id` int(150) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
