-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Дек 20 2023 г., 18:30
-- Версия сервера: 10.4.10-MariaDB
-- Версия PHP: 7.4.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `sushimarket`
--

-- --------------------------------------------------------

--
-- Структура таблицы `delivers`
--

DROP TABLE IF EXISTS `delivers`;
CREATE TABLE IF NOT EXISTS `delivers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `FIO` text NOT NULL,
  `DateOfBirth` text NOT NULL,
  `Status` text NOT NULL,
  `Job` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `delivers`
--

INSERT INTO `delivers` (`id`, `FIO`, `DateOfBirth`, `Status`, `Job`) VALUES
(4, 'FyodorovAlexander', '20.12.1988', '', 'Courier'),
(3, '3', '', '', '22');

-- --------------------------------------------------------

--
-- Структура таблицы `delivery`
--

DROP TABLE IF EXISTS `delivery`;
CREATE TABLE IF NOT EXISTS `delivery` (
  `ID` int(50) NOT NULL AUTO_INCREMENT,
  `Cost` text NOT NULL,
  `Type` text NOT NULL,
  `Company` text NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=112 DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `delivery`
--

INSERT INTO `delivery` (`ID`, `Cost`, `Type`, `Company`) VALUES
(111, '2', '2', '211'),
(77, '4', '54', '6'),
(44, '44', '44', '44');

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `id` int(50) NOT NULL AUTO_INCREMENT,
  `Name` text NOT NULL,
  `Cost` text NOT NULL,
  `Status` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=556 DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `orders`
--

INSERT INTO `orders` (`id`, `Name`, `Cost`, `Status`) VALUES
(3, '3', '33', 'Stop'),
(555, '555', '3', '455'),
(4, '44', '4', '455'),
(2, '2', '', ''),
(1, '1', '', 'Processing');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
