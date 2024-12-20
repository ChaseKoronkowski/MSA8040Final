-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: orion_stores
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `ï»¿Customer_ID` int NOT NULL,
  `Country` text,
  `Gender` text,
  `Personal_ID` text,
  `Customer_Name` varchar(255) DEFAULT NULL,
  `Customer_FirstName` text,
  `Customer_LastName` text,
  `Birth_Date` text,
  `Customer_Address` text,
  `Street_ID` bigint DEFAULT NULL,
  `Street_Number` int DEFAULT NULL,
  `Customer_Type_ID` int DEFAULT NULL,
  PRIMARY KEY (`ï»¿Customer_ID`),
  KEY `idx_customer_name` (`Customer_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (4,'US','M','','James Kvarniq','James','Kvarniq','27JUN1974','4382 Gralyn Rd',9260106519,4382,1020),(5,'US','F','','Sandrina Stephano','Sandrina','Stephano','09JUL1979','6468 Cog Hill Ct',9260114570,6468,2020),(9,'DE','F','','Cornelia Krahl','Cornelia','Krahl','27FEB1974','Kallstadterstr. 9',3940106659,9,2020),(10,'US','F','','Karen Ballinger','Karen','Ballinger','18OCT1984','425 Bryant Estates Dr',9260129395,425,1040),(11,'DE','F','','Elke Wallstab','Elke','Wallstab','16AUG1974','Carl-Zeiss-Str. 15',3940108592,15,1040),(12,'US','M','','David Black','David','Black','12APR1969','1068 Haithcock Rd',9260103713,1068,1030),(13,'DE','M','','Markus Sepke','Markus','Sepke','21JUL1988','Iese 1',3940105189,1,2010),(16,'DE','M','','Ulrich Heyde','Ulrich','Heyde','16JAN1939','Oberstr. 61',3940105865,61,3010),(17,'US','M','','Jimmie Evans','Jimmie','Evans','17AUG1954','391 Greywood Dr',9260123306,391,1030),(18,'US','M','','Tonie Asmussen','Tonie','Asmussen','02FEB1954','117 Langtree Ln',9260112361,117,1020),(19,'DE','M','','Oliver S. FÃ¼ÃŸling','Oliver S.','FÃ¼ÃŸling','23FEB1964','Hechtsheimerstr. 18',3940106547,18,2030),(20,'US','M','','Michael Dineley','Michael','Dineley','17APR1959','2187 Draycroft Pl',9260118934,2187,1030),(23,'US','M','','Tulio Devereaux','Tulio','Devereaux','02DEC1949','1532 Ferdilah Ln',9260126679,1532,3010),(24,'US','F','','Robyn Klem','Robyn','Klem','02JUN1959','435 Cambrian Way',9260115784,435,3010),(27,'US','F','','Cynthia Mccluney','Cynthia','Mccluney','15APR1969','188 Grassy Creek Pl',9260105670,188,3010),(29,'AU','F','','Candy Kinsey','Candy','Kinsey','08JUL1934','21 Hotham Parade',1600103020,21,3010),(31,'US','F','','Cynthia Martinez','Cynthia','Martinez','07AUG1959','42 Arrowood Ln',9260128428,42,2020),(33,'DE','M','','Rolf Robak','Rolf','Robak','24FEB1939','MÃ¼nsterstraÃŸe 67',3940102376,67,1030),(34,'US','M','','Alvan Goheen','Alvan','Goheen','18JAN1984','844 Glen Eden Dr',9260111379,844,1020),(36,'US','M','','Phenix Hill','Phenix','Hill','02APR1964','417 Halstead Cir',9260128237,417,3010),(39,'US','M','','Alphone Greenwald','Alphone','Greenwald','25JUL1984','4386 Hamrick Dr',9260123099,4386,2030),(41,'AU','M','','Wendell Summersby','Wendell','Summersby','02DEC1964','9 Angourie Court',1600101527,9,1030),(42,'DE','M','','Thomas Leitmann','Thomas','Leitmann','09FEB1979','Carl Von Linde Str. 13',3940109715,13,1020),(45,'US','F','','Dianne Patchin','Dianne','Patchin','06MAY1979','7818 Angier Rd',9260104847,7818,2010),(49,'US','F','','Annmarie Leveille','Annmarie','Leveille','16JUL1984','185 Birchford Ct',9260104510,185,2030),(50,'DE','M','','Gert-Gunter Mendler','Gert-Gunter','Mendler','16JAN1934','Humboldtstr. 1',3940105781,1,2030),(52,'US','M','','Yan Kozlowski','Yan','Kozlowski','06APR1969','1233 Hunters Crossing',9260116235,1233,1030),(53,'AU','F','','Dericka Pockran','Dericka','Pockran','20JUN1954','131 Franklin St',1600103258,131,1040),(56,'US','M','','Roy Siferd','Roy','Siferd','01FEB1934','334 Kingsmill Rd',9260111871,334,1030),(60,'US','F','','Tedi Lanzarone','Tedi','Lanzarone','23MAY1969','2429 Hunt Farms Ln',9260101262,2429,1030),(61,'DE','M','','Carsten Maestrini','Carsten','Maestrini','08JUL1944','MÃ¼nzstr. 28',3940108887,28,2030),(63,'US','M','','James Klisurich','James','Klisurich','25DEC1969','25 Briarforest Pl',9260125492,25,2020),(65,'DE','F','','Ines Deisser','Ines','Deisser','20JUL1969','Bahnweg 1',3940100176,1,1020),(69,'US','F','','Patricia Bertolozzi','Patricia','Bertolozzi','13MAY1979','4948 Dargan Hills Dr',9260116402,4948,1020),(71,'US','F','','Viola Folsom','Viola','Folsom','23SEP1969','290 Glenwood Ave',9260124130,290,2020),(75,'US','M','','Mikel Spetz','Mikel','Spetz','18JUN1984','101 Knoll Ridge Ln',9260108068,101,1020),(79,'US','F','','Najma Hicks','Najma','Hicks','22JAN1986','9658 Dinwiddie Ct',9260101874,9658,1030),(88,'US','M','','Attila Gibbs','Attila','Gibbs','19FEB1959','3815 Askham Dr',9260100179,3815,1030),(89,'US','F','','Wynella Lewis','Wynella','Lewis','28SEP1934','2572 Glenharden Dr',9260116551,2572,1040),(90,'US','F','','Kyndal Hooks','Kyndal','Hooks','01AUG1964','252 Clay St',9260111614,252,2030),(92,'US','M','','Lendon Celii','Lendon','Celii','14SEP1944','421 Blue Horizon Dr',9260117676,421,1020),(111,'AU','F','','Karolina Dokter','Karolina','Dokter','28DEC1974','28 Munibung Road',1600102072,28,1030),(171,'AU','M','','Robert Bowerman','Robert','Bowerman','22FEB1974','21 Parliament House c/- Senator t',1600101555,21,1040),(183,'AU','M','','Duncan Robertshawe','Duncan','Robertshawe','25MAR1944','18 Fletcher Rd',1600100760,18,1020),(195,'AU','M','','Cosi Rimmington','Cosi','Rimmington','11NOV1944','4 Burke Street Woolloongabba',1600101663,4,1020),(215,'AU','M','','Ramesh Trentholme','Ramesh','Trentholme','16MAY1949','23 Benjamin Street',1600102721,23,2020),(544,'TR','M','','Avni Argac','Avni','Argac','20MAY1964','A Blok No: 1',9050100008,1,1040),(908,'TR','M','','Avni Umran','Avni','Umran','06DEC1979','Mayis Cad. Nova Baran Plaza Ka 11',9050100023,11,2030),(928,'TR','M','','Bulent Urfalioglu','Bulent','Urfalioglu','11AUG1969','Turkcell Plaza Mesrutiyet Cad. 142',9050100016,142,1020),(1033,'TR','M','','Selim Okay','Selim','Okay','14OCT1979','Fahrettin Kerim Gokay Cad. No. 24',9050100001,24,1020),(1100,'TR','M','','Ahmet Canko','Ahmet','Canko','19JAN1964','A Blok No: 1',9050100008,1,1020),(1684,'TR','M','','Carglar Aydemir','Carglar','Aydemir','17OCT1974','A Blok No: 1',9050100008,1,1020),(2550,'ZA','F','','Sanelisiwe Collier','Sanelisiwe','Collier','07JUL1988','Bryanston Drive 122',8010100009,122,2010),(2618,'ZA','M','','Theunis Brazier','Theunis','Brazier','21MAR1949','Arnold Road 2',8010100125,2,1030),(2788,'TR','M','','Serdar Yucel','Serdar','Yucel','02JAN1944','Fahrettin Kerim Gokay Cad. No. 30',9050100001,30,1040),(2806,'ZA','F','','Raedene Van Den Berg','Raedene','Van Den Berg','16SEP1988','Quinn Street 11',8010100089,11,1030),(3959,'ZA','F','','Rita Lotz','Rita','Lotz','24FEB1964','Moerbei Avenue 120',8010100151,120,2030),(11171,'CA','M','','Bill Cuddy','Bill','Cuddy','16OCT1986','69 chemin Martin',2600100032,69,2010),(12386,'IL','M','','Avinoam Zweig','Avinoam','Zweig','12MAY1959','Mivtza Kadesh St 16',4750100001,16,3010),(14104,'IL','M','','Avinoam Zweig','Avinoam','Zweig','10OCT1964','Mivtza Kadesh St 25',4750100001,25,1030),(14703,'IL','M','','Eyal Bloch','Eyal','Bloch','24SEP1969','Mivtza Boulevard 17',4750100002,17,1040),(17023,'CA','F','','Susan Krasowski','Susan','Krasowski','09JUL1959','837 rue Lajeunesse',2600100021,837,2030),(19444,'IL','M','','Avinoam Zweig','Avinoam','Zweig','28SEP1959','Mivtza Kadesh St 61',4750100001,61,1040),(19873,'IL','M','','Avinoam Tuvia','Avinoam','Tuvia','14JUN1984','Mivtza Kadesh St 18',4750100001,18,2030),(26148,'CA','M','','Andreas Rennie','Andreas','Rennie','18JUL1934','41 Main St',2600100010,41,1030),(46966,'CA','F','','Lauren Krasowski','Lauren','Krasowski','24OCT1986','17 boul Wallberg',2600100011,17,1040),(54655,'CA','F','','Lauren Marx','Lauren','Marx','18AUG1969','512 Gregoire Dr',2600100013,512,3010),(70046,'CA','M','','Tommy Mcdonald','Tommy','Mcdonald','20JAN1959','818 rue Davis',2600100017,818,1020),(70059,'CA','M','','Colin Byarley','Colin','Byarley','20JAN1934','580 Howe St',2600100047,580,1030),(70079,'CA','F','','Lera Knott','Lera','Knott','11JUL1986','304 Grand Lake Rd',2600100039,304,1030),(70100,'CA','F','','Wilma Yeargan','Wilma','Yeargan','23JUN1984','614 Route 199',2600100015,614,1030),(70108,'CA','M','','Patrick Leach','Patrick','Leach','14APR1939','1001 Burrard St',2600100046,1001,1020),(70165,'CA','F','','Portia Reynoso','Portia','Reynoso','11FEB1964','873 rue Bosse',2600100006,873,1020),(70187,'CA','F','','Soberina Berent','Soberina','Berent','27SEP1986','1835 boul Laure',2600100035,1835,1030),(70201,'CA','F','','Angel Borwick','Angel','Borwick','19DEC1969','319 122 Ave NW',2600100012,319,2010),(70210,'CA','M','','Alex Santinello','Alex','Santinello','22APR1986','40 Route 199',2600100015,40,1030),(70221,'CA','M','','Kenan Talarr','Kenan','Talarr','10FEB1964','9 South Service Rd',2600100019,9,1040);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-05 12:03:55
