-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 12, 2021 at 08:19 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.3.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hpcl_showcase`
--

-- --------------------------------------------------------

--
-- Table structure for table `announcements_file`
--

CREATE TABLE `announcements_file` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `caption` text NOT NULL,
  `filename` varchar(100) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `announcements_file`
--

INSERT INTO `announcements_file` (`sno`, `title`, `caption`, `filename`, `date`) VALUES
(2, 'Urology webinar', '', 'FW_ Webinar - Common Urological Problems by Dr. Aman Gupta.eml', '2021-03-10 20:44:52'),
(3, 'Covid-19 Antibody testing', '', 'LPL Antibody Testing.pptx', '2021-03-10 20:45:48');

-- --------------------------------------------------------

--
-- Table structure for table `announcements_img`
--

CREATE TABLE `announcements_img` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `caption` text DEFAULT NULL,
  `filename` varchar(100) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `announcements_img`
--

INSERT INTO `announcements_img` (`sno`, `title`, `caption`, `filename`, `date`) VALUES
(12, 'DocTalk on Heart diseases', 'none', 'Sample4.jpg', '2021-03-11 13:08:25'),
(14, 'Artemis Hospital', 'none', 'Sample1.jpg', '2021-03-10 23:11:58');

-- --------------------------------------------------------

--
-- Table structure for table `healthcheck_file`
--

CREATE TABLE `healthcheck_file` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `caption` text NOT NULL,
  `filename` varchar(100) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `healthcheck_file`
--

INSERT INTO `healthcheck_file` (`sno`, `title`, `caption`, `filename`, `date`) VALUES
(1, 'Maxscene', '', 'MAXSCENE.pdf', '2021-03-10 20:44:02'),
(2, 'Urology webinar', '', 'FW_ Webinar - Common Urological Problems by Dr. Aman Gupta.eml', '2021-03-10 20:44:52'),
(3, 'Covid-19 Antibody testing', '', 'LPL Antibody Testing.pptx', '2021-03-10 20:45:48');

-- --------------------------------------------------------

--
-- Table structure for table `healthcheck_img`
--

CREATE TABLE `healthcheck_img` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `caption` text DEFAULT NULL,
  `filename` varchar(100) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `healthcheck_img`
--

INSERT INTO `healthcheck_img` (`sno`, `title`, `caption`, `filename`, `date`) VALUES
(1, 'Artemis hospital', 'None', 'Sample1.jpg', '2021-03-11 13:29:19'),
(13, 'Fortis Hospital', 'none', 'Sample2.jpg', '2021-03-10 20:38:46');

-- --------------------------------------------------------

--
-- Table structure for table `knowledge_file`
--

CREATE TABLE `knowledge_file` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `caption` text NOT NULL,
  `filename` varchar(100) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `knowledge_file`
--

INSERT INTO `knowledge_file` (`sno`, `title`, `caption`, `filename`, `date`) VALUES
(1, 'Maxscene', '', 'MAXSCENE.pdf', '2021-03-10 20:44:02'),
(2, 'Urology webinar', '', 'FW_ Webinar - Common Urological Problems by Dr. Aman Gupta.eml', '2021-03-10 20:44:52'),
(3, 'Covid-19 Antibody testing', '', 'LPL Antibody Testing.pptx', '2021-03-10 20:45:48');

-- --------------------------------------------------------

--
-- Table structure for table `knowledge_img`
--

CREATE TABLE `knowledge_img` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `caption` text DEFAULT NULL,
  `filename` varchar(100) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `knowledge_img`
--

INSERT INTO `knowledge_img` (`sno`, `title`, `caption`, `filename`, `date`) VALUES
(1, 'Artemis Hospital', NULL, 'Sample1.jpg', '2021-03-10 20:35:18'),
(12, 'Doctalk on Heart diseases', 'none', 'Sample4.jpg', '2021-03-10 20:37:38'),
(13, 'Fortis Hospital', 'none', 'Sample2.jpg', '2021-03-10 20:38:46');

-- --------------------------------------------------------

--
-- Table structure for table `opentalks_file`
--

CREATE TABLE `opentalks_file` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `caption` text NOT NULL,
  `filename` varchar(100) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `opentalks_file`
--

INSERT INTO `opentalks_file` (`sno`, `title`, `caption`, `filename`, `date`) VALUES
(1, 'Maxscene', '', 'MAXSCENE.pdf', '2021-03-10 20:44:02'),
(2, 'Urology webinar', '', 'FW_ Webinar - Common Urological Problems by Dr. Aman Gupta.eml', '2021-03-10 20:44:52'),
(3, 'Covid-19 Antibody testing', '', 'LPL Antibody Testing.pptx', '2021-03-10 20:45:48');

-- --------------------------------------------------------

--
-- Table structure for table `opentalks_img`
--

CREATE TABLE `opentalks_img` (
  `sno` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `caption` text DEFAULT NULL,
  `filename` varchar(100) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `opentalks_img`
--

INSERT INTO `opentalks_img` (`sno`, `title`, `caption`, `filename`, `date`) VALUES
(1, 'Artemis Hospital', NULL, 'Sample1.jpg', '2021-03-10 20:35:18'),
(12, 'Doctalk on Heart diseases', 'none', 'Sample4.jpg', '2021-03-10 20:37:38');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `announcements_file`
--
ALTER TABLE `announcements_file`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `announcements_img`
--
ALTER TABLE `announcements_img`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `healthcheck_file`
--
ALTER TABLE `healthcheck_file`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `healthcheck_img`
--
ALTER TABLE `healthcheck_img`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `knowledge_file`
--
ALTER TABLE `knowledge_file`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `knowledge_img`
--
ALTER TABLE `knowledge_img`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `opentalks_file`
--
ALTER TABLE `opentalks_file`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `opentalks_img`
--
ALTER TABLE `opentalks_img`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `announcements_file`
--
ALTER TABLE `announcements_file`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `announcements_img`
--
ALTER TABLE `announcements_img`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `healthcheck_file`
--
ALTER TABLE `healthcheck_file`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `healthcheck_img`
--
ALTER TABLE `healthcheck_img`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `knowledge_file`
--
ALTER TABLE `knowledge_file`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `knowledge_img`
--
ALTER TABLE `knowledge_img`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `opentalks_file`
--
ALTER TABLE `opentalks_file`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `opentalks_img`
--
ALTER TABLE `opentalks_img`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
