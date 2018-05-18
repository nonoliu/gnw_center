/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.5.29-log : Database - gnw_center
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`gnw_center` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `gnw_center`;

/*Table structure for table `gnw_routelist` */

DROP TABLE IF EXISTS `gnw_routelist`;

CREATE TABLE `gnw_routelist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `asn` varchar(100) DEFAULT NULL COMMENT '自治区域id',
  `provider` varchar(500) DEFAULT NULL COMMENT '提供者',
  `serverType` varchar(50) DEFAULT NULL COMMENT '设备类型',
  `lng` varchar(50) DEFAULT NULL COMMENT '经度',
  `lat` varchar(50) DEFAULT NULL COMMENT '纬度',
  `serverAddress` varchar(200) DEFAULT NULL COMMENT '设备地址',
  `serverStatus` varchar(500) DEFAULT NULL COMMENT '设备状态',
  `useLogin` varchar(10) DEFAULT NULL COMMENT '是否需要登录',
  `username` varchar(200) DEFAULT 'NULL',
  `passwd` varchar(200) DEFAULT 'NULL',
  `failCount` int(11) DEFAULT NULL COMMENT '连续失败次数',
  `deleteFlag` tinyint(1) DEFAULT '0',
  `note` varchar(1000) DEFAULT NULL,
  `hbtime` datetime DEFAULT NULL COMMENT '心跳时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

/*Data for the table `gnw_routelist` */

insert  into `gnw_routelist`(`id`,`asn`,`provider`,`serverType`,`lng`,`lat`,`serverAddress`,`serverStatus`,`useLogin`,`username`,`passwd`,`failCount`,`deleteFlag`,`note`,`hbtime`) values (1,'286','KPN','Cisco','10.454150','51.164181','route-server.eurorings.net','OK','0','rs','loveAS286',15,0,NULL,'2018-05-16 11:07:59'),(2,'553','BelWue','BIRD','9.0036649','48.6618471','route-server.belwue.de','nonsupport','0','NULL','NULL',448,0,NULL,'2018-05-16 11:07:59'),(3,'852','Telus - Eastern Canada','Cisco','-98.308968','56.954681','route-views.on.bb.telus.com','OK','1','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(4,'852','Telus - Western Canada','Cisco','-98.308968','56.954681','route-views.ab.bb.telus.com','OK','1','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(5,'3257','Tiscali','Cisco','47','15','route-server.ip.tiscali.net','OK','0','public','public',0,0,NULL,'2018-05-16 11:07:59'),(6,'3303','Swisscom','Cisco','8.223950','46.813202','route-server.ip-plus.net','OK','1','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(7,'3549','Global Crossing','Cisco','-95.712891','37.09024','route-server.gblx.net','OK','1','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(8,'3549','Global Crossing - Europe','Cisco','-95.712891','37.09024','route-server.eu.gblx.net','OK','1','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(9,'3741','Internet Solutions','Cisco','24.679930','-28.479330','public-route-server.is.co.za','OK','0','rviews','rviews',0,0,NULL,'2018-05-16 11:07:59'),(10,'4589','Easynet','Juniper','-2.230010','54.314072','rv0.telon.uk.easynet.net','OK','0','public','public',0,0,NULL,'2018-05-16 11:07:59'),(11,'5413','PIPEX','Cisco','-2.230010','54.314072','route-server.as5413.net','OK','1','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(12,'5713','SAIX - South African Internet Exchange','Cisco','24.679930','-28.479330','tpr-route-server.saix.net','OK','0','saix','saix',0,0,NULL,'2018-05-16 11:07:59'),(13,'6447','University of Oregon Route Views Project','Cisco','-123.088539','44.049919','route-views.routeviews.org','OK','0','rviews','',0,0,NULL,'2018-05-16 11:07:59'),(14,'6447','University of Oregon Route Views Project','Quagga','-123.088539','44.049919','route-views2.routeviews.org','nonsupport','0','rviews','',0,0,NULL,'2018-05-16 11:07:59'),(15,'6447','University of Oregon Route Views Project','Quagga','-123.088539','44.049919','route-views3.routeviews.org','nonsupport','0','rviews','',0,0,NULL,'2018-05-16 11:07:59'),(16,'6447','University of Oregon Route Views Project','Quagga','-122.146919','37.391861','route-views.isc.routeviews.org','nonsupport','0','rviews','',0,0,NULL,'2018-05-16 11:07:59'),(17,'6447','University of Oregon Route Views Project','Quagga','37.903950','-0.024350','route-views.kixp.routeviews.org','nonsupport','0','rviews','',0,0,NULL,'2018-05-16 11:07:59'),(18,'6447','University of Oregon Route Views Project','Quagga','-0.127970','51.507702','route-views.linx.routeviews.org','nonsupport','0','rviews','',0,0,NULL,'2018-05-16 11:07:59'),(19,'6447','University of Oregon Route Views Project','Quagga','138.252924','36.204824','route-views.wide.routeviews.org','nonsupport','0','rviews','',0,0,NULL,'2018-05-16 11:07:59'),(20,'6730','sunrise Switzerland','Cisco','47','10','routeserver.sunrise.ch','OK','1','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(21,'6939','Hurricane Electric','Quagga','-121.9885719','37.5482697','route-server.he.net','nonsupport','0','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(22,'7018','AT&T','Juniper','-95.712891','37.09024','route-server.ip.att.net','OK','0','rviews','rviews',0,0,NULL,'2018-05-16 11:07:59'),(23,'7474','Optus Australia','Cisco','133.397995','-24.912100','route-views.optus.net.au','OK','1','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(24,'7920','Comcast','Cisco','-95.712891','37.09024','route-server.newyork.ny.ibone.comcast.net','nonsupport','0','rviews','',0,0,NULL,'2018-05-16 11:07:59'),(25,'8881','Versatel','Cisco','10.454150','51.164181','route-server.versatel.de','OK','1','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(26,'9009','M247','Quagga','-2.233330','53.466702','route-server.m247.com','nonsupport','0','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(27,'11260','Eastlink','Cisco','-98.308968','56.954681','route-server.eastlink.ca','OK','1','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(28,'13645','Host.net','Quagga','-81.5157535','27.6648274','route-server.host.net','nonsupport','0','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59'),(29,'15290','Allstream - Central','Cisco','-98.308968','56.954681','route-server.central.allstream.com','OK','0','rserv','',447,0,NULL,'2018-05-16 11:07:59'),(30,'15290','Allstream - East','Cisco','-98.308968','56.954681','route-server.east.allstream.com','OK','0','rserv','',244,0,NULL,'2018-05-16 11:07:59'),(31,'15290','Allstream - West','Cisco','-98.308968','56.954681','route-server.west.allstream.com','OK','0','rserv','',0,0,NULL,'2018-05-16 11:07:59'),(32,'15763','DOKOM Gesellschaft für Telekommunikation mbH','Cisco','10.454150','51.164181','route-server.dokom.net','OK','1','','',0,0,NULL,'2018-05-16 11:07:59'),(33,'22548','PTT-Metro Sao Paulo','Quagga','-54.387798','-14.242900','lg.sp.ptt.br','nonsupport','0','NULL','NULL',448,0,NULL,'2018-05-16 11:07:59'),(34,'56911','Warian SAS','Quagga','12.573470','42.503819','route-server.warian.net','nonsupport','0','NULL','NULL',0,0,NULL,'2018-05-16 11:07:59');

/*Table structure for table `gnw_serverlist` */

DROP TABLE IF EXISTS `gnw_serverlist`;

CREATE TABLE `gnw_serverlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serverAddress` varchar(20) DEFAULT NULL COMMENT '服务器ip',
  `lng` varchar(50) DEFAULT '0' COMMENT '经度',
  `lat` varchar(50) DEFAULT '0' COMMENT '纬度',
  `zone` varchar(50) DEFAULT NULL COMMENT '所属地区',
  `isAgent` int(11) DEFAULT '1' COMMENT '是否为代理',
  `deleteFlag` tinyint(1) DEFAULT '0',
  `watchZone` int(11) DEFAULT '1' COMMENT '1 全球节点， 0 自己区域节点',
  `hbTime` datetime DEFAULT NULL COMMENT '心跳时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

/*Data for the table `gnw_serverlist` */

insert  into `gnw_serverlist`(`id`,`serverAddress`,`lng`,`lat`,`zone`,`isAgent`,`deleteFlag`,`watchZone`,`hbTime`) values (1,'119.28.106.26','1.29378','103.852997','SGP',1,0,1,'2018-05-17 17:27:04'),(2,'23.248.168.146','0.10974','113.917397','INA',1,0,1,'2018-05-16 19:40:31'),(3,'49.51.132.253','8.68341','50.11208','GER',1,0,1,'2018-05-16 11:10:29'),(4,'128.1.43.72','37.605061 ','55.741638','RUS',1,0,1,'2018-05-16 11:10:29'),(5,'49.51.40.54','-121.886002','37.3386','USA',1,0,1,'2018-05-16 11:10:29'),(6,'54.94.197.93','-46.6333094','-23.5505199','BRA',1,0,1,'2018-05-16 11:10:29'),(7,'118.89.140.128','121.472644','31.231706','CHN-SH',1,0,1,'2018-05-16 11:10:29'),(8,'119.28.60.144','114.109497','22.396428','CHN-HK',1,0,1,'2018-05-16 11:10:29'),(9,'222.73.95.102','121.472644','31.231706','CHN-BJ',1,0,1,'2018-05-16 11:10:29');

/*Table structure for table `gnw_users` */

DROP TABLE IF EXISTS `gnw_users`;

CREATE TABLE `gnw_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `pwd` varchar(50) DEFAULT NULL,
  `note` varchar(100) DEFAULT NULL,
  `createTime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `gnw_users` */

insert  into `gnw_users`(`id`,`username`,`pwd`,`note`,`createTime`) values (1,'admin','*99B8F2E84401245AE6B90C411BD43A848DF41DE8','test','2018-05-17 18:42:50');

/* Procedure structure for procedure `sp_addServerList` */

/*!50003 DROP PROCEDURE IF EXISTS  `sp_addServerList` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`gnw_user`@`122.224.197.37` PROCEDURE `sp_addServerList`(IN _address varchar(20), IN _lng varchar(50), IN _lat varchar(50), IN _zone varchar(50), IN _isagent int,IN _watchZone int)
    SQL SECURITY INVOKER
BEGIN
    DECLARE stats VARCHAR(20);
    IF NOT EXISTS(SELECT 1 FROM `gnw_serverlist` WHERE serverAddress=_address ) THEN
	INSERT INTO `gnw_center`.`gnw_serverlist` (`serverAddress`,`lng`,`lat`,`zone`,`isAgent`,`deleteFlag`,`watchZone`,`hbTime`) 
	VALUES  ( _address,_lng,_lat,_zone,_isagent,0,_watchZone,NOW()) ;
    END IF;
    COMMIT;
END */$$
DELIMITER ;

/* Procedure structure for procedure `sp_setRouteList` */

/*!50003 DROP PROCEDURE IF EXISTS  `sp_setRouteList` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`gnw_user`@`122.224.197.37` PROCEDURE `sp_setRouteList`(IN _asn varchar(100), IN _provider VARCHAR(500), In _serverType varchar(50), IN _serverAddress varchar(200),
	IN _serverStatus VARCHAR(200), In _useLogin varchar(10), IN _failCount int, IN _lng varchar(50), IN _lat varchar(50))
    SQL SECURITY INVOKER
BEGIN
    DECLARE stats VARCHAR(20);
    IF NOT EXISTS(SELECT 1 FROM `gnw_routelist` WHERE serverAddress=_serverAddress ) THEN
	INSERT INTO `gnw_center`.`gnw_routelist` ( `asn`,`provider`,`serverType`,`serverAddress`,`serverStatus`,`useLogin`,`failCount`,`deleteFlag`,`lng`,`lat`) 
	VALUES  ( _asn,_provider,_serverType,_serverAddress,_serverStatus,_useLogin,_failCount,0,_lng,_lat ) ;
    END IF;
    COMMIT;
END */$$
DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
