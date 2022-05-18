 SET NAMES utf8 ;
DROP TABLE IF EXISTS `Utilisateur`;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Utilisateur` (
  `user` varchar(255) DEFAULT NULL,
  `mdp` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `Utilisateur` WRITE;

UNLOCK TABLES;
