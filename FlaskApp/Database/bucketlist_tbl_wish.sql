-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: bucketlist
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_wish`
--

DROP TABLE IF EXISTS `tbl_wish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tbl_wish` (
  `wish_id` int(11) NOT NULL AUTO_INCREMENT,
  `wish_title` varchar(45) NOT NULL,
  `wish_description` varchar(5000) DEFAULT NULL,
  `wish_user_id` int(45) DEFAULT NULL,
  `wish_date` datetime DEFAULT NULL,
  `wish_file_path` varchar(200) DEFAULT NULL,
  `wish_accomplished` int(11) DEFAULT '0',
  `wish_private` int(11) DEFAULT '0',
  PRIMARY KEY (`wish_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_wish`
--

LOCK TABLES `tbl_wish` WRITE;
/*!40000 ALTER TABLE `tbl_wish` DISABLE KEYS */;
INSERT INTO `tbl_wish` VALUES (2,'Goa Trip','Anjuna Beach Curleys ',3,'2018-11-28 17:00:05','static/uploads/AnjunaBeach.jpg',0,1),(3,'Trekking','Leh Ladhak trekking',3,'2018-11-29 14:56:13','static/uploads/LehTrekking.jpg',0,0),(5,'Foreign trip','Bali / Indonesia',3,'2019-01-23 12:40:46','static/uploads/Bali_Image.jpg',0,1),(6,'Dubai trip','Dubai trip with Anant',3,'2019-01-25 15:43:30','static/Uploads/Dubai.jpg',0,0),(7,'Rajasthan Tour','Jaipur trip',3,'2019-02-13 16:08:14','static/Uploads/Jaipur.jpg',0,0),(8,'Ooty Tour','Trip to tamilnandu - Ooty',3,'2019-02-13 16:16:03','static/Uploads/Ooty.jpg',0,0),(9,'Agara Visit','Tajmahal',3,'2019-02-13 16:22:21','static/Uploads/Tajmahal.jpg',0,0),(10,'Kerala tour','Kerla trip',3,'2019-02-13 16:23:46','static/Uploads/Kerla.jpg',0,0),(11,'Thailand','Wanted to visit Thailand',3,'2019-03-19 16:46:50','static/Uploads/Thailand.jpg',0,1);
/*!40000 ALTER TABLE `tbl_wish` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-19 17:24:02
