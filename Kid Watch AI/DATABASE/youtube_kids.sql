-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 03, 2023 at 12:04 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `youtube_kids`
--
CREATE DATABASE IF NOT EXISTS `youtube_kids` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `youtube_kids`;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add userdetails model', 7, 'add_userdetailsmodel'),
(26, 'Can change userdetails model', 7, 'change_userdetailsmodel'),
(27, 'Can delete userdetails model', 7, 'delete_userdetailsmodel'),
(28, 'Can view userdetails model', 7, 'view_userdetailsmodel'),
(29, 'Can add feedback model', 8, 'add_feedbackmodel'),
(30, 'Can change feedback model', 8, 'change_feedbackmodel'),
(31, 'Can delete feedback model', 8, 'delete_feedbackmodel'),
(32, 'Can view feedback model', 8, 'view_feedbackmodel'),
(33, 'Can add video model', 9, 'add_videomodel'),
(34, 'Can change video model', 9, 'change_videomodel'),
(35, 'Can delete video model', 9, 'delete_videomodel'),
(36, 'Can view video model', 9, 'view_videomodel'),
(37, 'Can add comment model', 10, 'add_commentmodel'),
(38, 'Can change comment model', 10, 'change_commentmodel'),
(39, 'Can delete comment model', 10, 'delete_commentmodel'),
(40, 'Can view comment model', 10, 'view_commentmodel');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'mainapp', 'userdetailsmodel'),
(8, 'userapp', 'feedbackmodel'),
(9, 'userapp', 'videomodel'),
(10, 'userapp', 'commentmodel');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-01-02 07:30:11.761672'),
(2, 'auth', '0001_initial', '2023-01-02 07:30:13.591557'),
(3, 'admin', '0001_initial', '2023-01-02 07:30:14.056528'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-01-02 07:30:14.073528'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-01-02 07:30:14.089528'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-01-02 07:30:14.230519'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-01-02 07:30:14.306514'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-01-02 07:30:14.419508'),
(9, 'auth', '0004_alter_user_username_opts', '2023-01-02 07:30:14.436506'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-01-02 07:30:14.575496'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-01-02 07:30:14.652493'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-01-02 07:30:14.784486'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-01-02 07:30:14.896478'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-01-02 07:30:14.997471'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-01-02 07:30:15.083465'),
(16, 'auth', '0011_update_proxy_permissions', '2023-01-02 07:30:15.103464'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-01-02 07:30:15.173496'),
(18, 'sessions', '0001_initial', '2023-01-02 07:30:15.334450'),
(19, 'mainapp', '0001_initial', '2023-01-03 05:50:45.028056'),
(20, 'mainapp', '0002_alter_userdetailsmodel_user_photo', '2023-01-03 06:09:19.551644'),
(21, 'mainapp', '0003_alter_userdetailsmodel_user_email', '2023-01-03 06:09:19.638638'),
(22, 'mainapp', '0004_alter_userdetailsmodel_user_email_and_more', '2023-01-03 06:27:40.590215'),
(23, 'mainapp', '0005_alter_userdetailsmodel_user_photo', '2023-01-03 06:27:40.601214'),
(24, 'mainapp', '0006_alter_userdetailsmodel_user_email', '2023-01-03 06:27:40.610214'),
(25, 'mainapp', '0007_alter_userdetailsmodel_user_email', '2023-01-03 06:36:59.249023'),
(26, 'userapp', '0001_initial', '2023-01-04 07:29:23.381279'),
(27, 'userapp', '0002_videomodel', '2023-01-11 05:56:03.003666'),
(28, 'userapp', '0003_alter_videomodel_vid_comments', '2023-01-11 07:05:01.377947'),
(29, 'userapp', '0004_alter_videomodel_vid_comments', '2023-01-11 07:23:09.468422'),
(30, 'userapp', '0005_remove_videomodel_vid_comments_and_more', '2023-01-11 12:23:16.340744'),
(31, 'userapp', '0002_videomodel_vid_sentiment_delete_commentmodel', '2023-01-17 10:20:02.194192');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5zt2mo0hrv88cdxn4obj3w38r48x2h71', 'eyJ1c2VyX2lkIjozfQ:1pFsJJ:NNhYYzoevRemZrZdIRtK4d-h8K-0S2bYq5wED5PtiP0', '2023-01-26 07:47:41.778989'),
('fvtrbj8gm0nzqeztbocuw9j5mkzoqmsa', 'eyJ1c2VyX2lkIjozfQ:1pHkuF:h6Sj89-ddW5kQYAA6X7NCCDrnRrNhcsasLA_zw0ntmE', '2023-01-31 12:17:35.255327'),
('b5mpu8441aq80lw80qjq5z8ocqvhm6cp', 'eyJ1c2VyX2lkIjo4fQ:1qyhdp:b-cyTuEtPqyilQ3TYji3lMpW4lXxrspaJ6Tvdjij7UE', '2023-11-17 00:02:25.729426');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;
CREATE TABLE IF NOT EXISTS `user_details` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `user_password` varchar(100) NOT NULL,
  `user_contact` bigint(20) NOT NULL,
  `user_city` varchar(100) NOT NULL,
  `user_photo` varchar(100) NOT NULL,
  `datetime_created` datetime(6) NOT NULL,
  `user_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`user_id`, `user_name`, `user_email`, `user_password`, `user_contact`, `user_city`, `user_photo`, `datetime_created`, `user_status`) VALUES
(4, 'Mohd hashwar', 'mohd.hashwar552@gmail.com', '1234', 7878787876, 'hyderabad', 'media/3.png', '2023-01-04 13:53:43.515456', 'pending'),
(3, 'jonny saccramoni', 'jonny@gmail.com', '1234', 7878787876, 'Hyderabad', 'media/admin.jpg', '2023-01-04 12:35:25.336524', 'accepted'),
(5, 'jean', 'jean@gmail.com', '123456', 8528528523, 'Bangalore', 'media/5.jpg', '2023-01-13 15:34:30.475668', 'accepted'),
(6, 'jim helpert', 'jim@gmail.com', '1234', 9511595123, 'chenni', 'media/64-1.jpg', '2023-01-13 21:58:53.093912', 'accepted'),
(7, 'tom hardy', 'hardy@gmail.com', '1234', 7678598457, 'pune', 'media/1.png', '2023-01-17 17:38:53.061498', 'accepted'),
(8, 'fazal', 'fazalsirmail@gmail.com', 'fazal', 8555887986, 'Hyderabad', 'media/face9.jpg', '2023-11-03 04:49:55.131488', 'accepted');

-- --------------------------------------------------------

--
-- Table structure for table `user_feedbacks`
--

DROP TABLE IF EXISTS `user_feedbacks`;
CREATE TABLE IF NOT EXISTS `user_feedbacks` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `review` varchar(500) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `sentiment` varchar(50) DEFAULT NULL,
  `datetime_reviewed` datetime(6) NOT NULL,
  `reviewer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`),
  KEY `user_feedbacks_reviewer_id_b1775847` (`reviewer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_feedbacks`
--

INSERT INTO `user_feedbacks` (`feedback_id`, `review`, `rating`, `sentiment`, `datetime_reviewed`, `reviewer_id`) VALUES
(1, 'this is a great website for detecting offensive comments in urdu ', 5, 'positive', '2023-01-04 07:32:25.601316', 3),
(2, 'this site need more optimization', 2, 'positive', '2023-01-13 08:38:12.478522', 3),
(10, 'its just ok and needs more improvements\r\n', 1, 'positive', '2023-01-13 16:41:27.978013', 6),
(8, 'its not that good just average.', 4, 'negative', '2023-01-13 16:39:06.112451', 6),
(11, 'not bad', 4, 'positive', '2023-01-17 11:57:20.972545', 6),
(12, 'very nice app for kids', 5, 'positive', '2023-11-02 23:27:42.566702', 8);

-- --------------------------------------------------------

--
-- Table structure for table `video_details`
--

DROP TABLE IF EXISTS `video_details`;
CREATE TABLE IF NOT EXISTS `video_details` (
  `vid_id` int(11) NOT NULL AUTO_INCREMENT,
  `vid_url_id` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `datetime_searched` datetime(6) NOT NULL,
  `search_author_id` int(11) DEFAULT NULL,
  `vid_url` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `vid_sentiment` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`vid_id`),
  KEY `video_details_search_author_id_ede4c7b4` (`search_author_id`)
) ENGINE=MyISAM AUTO_INCREMENT=168 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `video_details`
--

INSERT INTO `video_details` (`vid_id`, `vid_url_id`, `datetime_searched`, `search_author_id`, `vid_url`, `vid_sentiment`) VALUES
(154, 'SK2tlXFg8tM', '2023-01-17 10:26:13.726438', 3, 'https://www.youtube.com/watch?v=SK2tlXFg8tM', 'very positive'),
(153, 'SK2tlXFg8tM', '2023-01-17 10:25:47.532003', 3, 'https://www.youtube.com/watch?v=SK2tlXFg8tM', 'very positive'),
(152, 'SK2tlXFg8tM', '2023-01-17 10:21:51.824643', 3, 'https://www.youtube.com/watch?v=SK2tlXFg8tM', 'very positive'),
(155, 'FY7hE4ZNza0', '2023-01-17 10:32:20.265524', 6, 'https://www.youtube.com/watch?v=FY7hE4ZNza0', 'positive'),
(156, 'Qi5gdSN-cQQ', '2023-01-17 10:48:15.982412', 6, 'https://www.youtube.com/watch?v=Qi5gdSN-cQQ', 'neutral'),
(157, '06CbzzSl6uc', '2023-01-17 10:52:21.342102', 6, 'https://www.youtube.com/watch?v=06CbzzSl6uc', 'neutral'),
(158, 'zde2YT9eE7E', '2023-01-17 11:53:15.137796', 6, 'https://www.youtube.com/watch?v=zde2YT9eE7E', 'neutral'),
(159, 'zde2YT9eE7E', '2023-01-17 11:58:09.080239', 6, 'https://www.youtube.com/watch?v=zde2YT9eE7E', 'neutral'),
(160, 'KNdnfDDqZJA', '2023-01-17 12:00:17.199634', 6, 'https://www.youtube.com/watch?v=KNdnfDDqZJA', 'neutral'),
(161, 'q2QvA3wwAe0', '2023-01-17 12:00:40.607187', 6, 'https://www.youtube.com/watch?v=q2QvA3wwAe0', 'neutral'),
(162, 'q2QvA3wwAe0', '2023-01-17 12:05:14.594816', 6, 'https://www.youtube.com/watch?v=q2QvA3wwAe0', 'neutral'),
(163, '5Q0In5GlQHc', '2023-01-17 12:18:30.967023', 3, 'https://www.youtube.com/watch?v=5Q0In5GlQHc', 'neutral'),
(164, '5Q0In5GlQHc', '2023-11-02 23:14:35.423502', 7, 'https://www.youtube.com/watch?v=5Q0In5GlQHc', 'neutral'),
(165, 'jvfr6zG1OyI', '2023-11-02 23:23:10.383619', 8, 'https://www.youtube.com/watch?v=jvfr6zG1OyI', 'neutral'),
(166, 'IBp6R7-v7FQ', '2023-11-02 23:26:08.529410', 8, 'https://www.youtube.com/watch?v=_Thw0-VD7Iw', 'very positive'),
(167, 'IBp6R7-v7FQ', '2023-11-03 00:02:39.415657', 8, 'https://www.youtube.com/watch?v=_Thw0-VD7Iw', 'very positive');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
