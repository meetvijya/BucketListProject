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
-- Table structure for table `tbl_user`
--

DROP TABLE IF EXISTS `tbl_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tbl_user` (
  `user_userid` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) DEFAULT NULL,
  `user_username` varchar(45) DEFAULT NULL,
  `user_password` varchar(100) DEFAULT NULL,
  `user_PhotoPath` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`user_userid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='User details';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_user`
--

LOCK TABLES `tbl_user` WRITE;
/*!40000 ALTER TABLE `tbl_user` DISABLE KEYS */;
INSERT INTO `tbl_user` VALUES (2,'aaa','ddd','pbkdf2:sha256:50000$p4fvaL55$26c7cc0a9372741b8e3fdb0c49e89eefcfb4975d6863226b1de8fdb45ae46cbb',NULL),(3,'Vijay Sawant','meetvijya@gmail.com','pbkdf2:sha256:50000$TQFFQk2k$3ec06719b1234504462953d0dbe147871cf8501d9f5fe883475d5116aec1f139','static/UserPhoto/my-passport-photo.jpg'),(4,'Sona','sona@gmail.com','pbkdf2:sha256:50000$VuU0l5eF$7c51d5a5ad2ef2bd85a9c9577b9449bfa50b1d08a2e4b9b75a814b3aaaa5bbed',NULL),(5,'mona p','mona@gmail.com','pbkdf2:sha256:50000$zXVvlIuQ$8666edf5b490ec66d045df882b704d6b56be3c4c73eb792a63b49e4c7f7238d6',NULL),(6,'Anant Patil','AnantPatil@gmail.com','pbkdf2:sha256:50000$DvMfVEKC$dfeea30a1087a433c07e3724c5ca807af71a46005328391f3ef184898990b2cd','static/UserPhoto/IMG_20190310_133124.jpg');
/*!40000 ALTER TABLE `tbl_user` ENABLE KEYS */;
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
