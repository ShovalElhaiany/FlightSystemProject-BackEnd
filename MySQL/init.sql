CREATE DATABASE flight_system_project;

USE flight_system_project;

CREATE TABLE `countries` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) UNIQUE,
    PRIMARY KEY (`id`)
);

CREATE TABLE `user_roles` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `role_name` VARCHAR(255) UNIQUE,
    PRIMARY KEY (`id`)
);

CREATE TABLE `users` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(255) UNIQUE,
    `password` VARCHAR(255),
    `email` VARCHAR(255) UNIQUE,
    `user_role` INT,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_role`) REFERENCES `user_roles`(`id`) ON DELETE CASCADE
);

CREATE TABLE `airline_companies` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) UNIQUE,
    `country_id` INT,
    `user_id` BIGINT UNSIGNED UNIQUE,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`country_id`) REFERENCES `countries`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
);

CREATE TABLE `customers` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(255),
    `last_name` VARCHAR(255),
    `address` VARCHAR(255),
    `phone_no` VARCHAR(255) UNIQUE,
    `credit_card_no` VARCHAR(255) UNIQUE,
    `user_id` BIGINT UNSIGNED UNIQUE,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
);

CREATE TABLE `administrators` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(255),
    `last_name` VARCHAR(255),
    `user_id` BIGINT UNSIGNED UNIQUE,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
);

CREATE TABLE `flights` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `airline_company_id` BIGINT UNSIGNED,
    `origin_country_id` INT,
    `destination_country_id` INT,
    `departure_time` DATETIME,
    `landing_time` DATETIME,
    `remaining_tickets` INT,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`airline_company_id`) REFERENCES `airline_companies`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`origin_country_id`) REFERENCES `countries`(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`destination_country_id`) REFERENCES `countries`(`id`) ON DELETE CASCADE
);

CREATE TABLE `tickets` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `flight_id` BIGINT UNSIGNED,
    `customer_id` BIGINT UNSIGNED,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uq_flight_customer` (`flight_id`, `customer_id`),
    FOREIGN KEY (`flight_id`) REFERENCES `flights`(`id`),
    FOREIGN KEY (`customer_id`) REFERENCES `customers`(`id`)
);

INSERT INTO countries (id, name) VALUES
(1, 'Albania'),
(2, 'Argentina'),
(3, 'Armenia'),
(4, 'Australia'),
(5, 'Austria'),
(6, 'Belarus'),
(7, 'Belgium'),
(8, 'Bosnia and Herzegovina'),
(9, 'Brazil'),
(10, 'Burgess'),
(11, 'Canada'),
(12, 'Chile'),
(13, 'China'),
(14, 'Colombia'),
(15, 'Croatia'),
(16, 'Cyprus'),
(17, 'Czech Republic'),
(18, 'Denmark'),
(19, 'Egypt'),
(20, 'Estonia'),
(21, 'Finland'),
(22, 'France'),
(23, 'Georgia'),
(24, 'Germany'),
(25, 'Greece'),
(26, 'Hungary'),
(27, 'Iceland'),
(28, 'India'),
(29, 'Indonesia'),
(30, 'Ireland'),
(31, 'Italy'),
(32, 'Japan'),
(33, 'Kazakhstan'),
(34, 'Kenya'),
(35, 'Kyrgyzstan'),
(36, 'Latvia'),
(37, 'Lithuania'),
(38, 'Luxembourg'),
(39, 'Macedonia'),
(40, 'Malaysia'),
(41, 'Mexico'),
(42, 'Moldova'),
(43, 'Montenegro'),
(44, 'Morocco'),
(45, 'Netherlands'),
(46, 'New Zealand'),
(47, 'Nigeria'),
(48, 'Norway'),
(49, 'Peru'),
(50, 'Philippines'),
(51, 'Poland'),
(52, 'Portugal'),
(53, 'Israel'),
(54, 'Qatar'),
(55, 'Romania'),
(56, 'Russia'),
(57, 'Saudi Arabia'),
(58, 'Serbia'),
(59, 'Singapore'),
(60, 'Slovakia'),
(61, 'Slovenia'),
(62, 'South Africa'),
(63, 'South Korea'),
(64, 'Spain'),
(65, 'Sweden'),
(66, 'Switzerland'),
(67, 'Thailand'),
(68, 'Turkey'),
(69, 'Turkmenistan'),
(70, 'Ukraine'),
(71, 'United Arab Emirates'),
(72, 'United Kingdom'),
(73, 'United States'),
(74, 'Uzbekistan'),
(75, 'Vietnam'),
(76, 'Algeria'),
(77, 'Azerbaijan'),
(78, 'Bangladesh'),
(79, 'Bulgaria'),
(80, 'Bolivia'),
(81, 'Cambodia'),
(82, 'Cameroon'),
(83, 'Costa Rica'),
(84, 'Cuba'),
(85, 'Dominican Republic'),
(86, 'Ecuador'),
(87, 'El Salvador'),
(88, 'Ethiopia'),
(89, 'Ghana'),
(90, 'Honduras'),
(91, 'Iraq'),
(92, 'Jamaica'),
(93, 'Jordan'),
(94, 'Lebanon'),
(95, 'Maldives'),
(96, 'Mongolia'),
(97, 'Pakistan'),
(98, 'Panama'),
(99, 'Paraguay'),
(100, 'Sri Lanka');

INSERT INTO user_roles (id, role_name) VALUES
(1, 'Administrator'),
(2, 'Customer'),
(3, 'AirlineCompany'),
(4, 'Anonymous');

INSERT INTO users (id, username, password, email, user_role) VALUES
(1, 'user1', 'password1', 'user1@example.com', 1),
(2, 'user2', 'password2', 'user2@example.com', 2),
(3, 'user3', 'password3', 'user3@example.com', 3),
(4, 'user4', 'password4', 'user4@example.com', 1),
(5, 'user5', 'password5', 'user5@example.com', 2),
(6, 'user6', 'password6', 'user6@example.com', 3),
(7, 'user7', 'password7', 'user7@example.com', 1),
(8, 'user8', 'password8', 'user8@example.com', 2),
(9, 'user9', 'password9', 'user9@example.com', 3),
(10, 'user10', 'password10', 'user10@example.com', 1),
(11, 'user11', 'password11', 'user11@example.com', 2),
(12, 'user12', 'password12', 'user12@example.com', 3),
(13, 'user13', 'password13', 'user13@example.com', 1),
(14, 'user14', 'password14', 'user14@example.com', 2),
(15, 'user15', 'password15', 'user15@example.com', 3),
(16, 'user16', 'password16', 'user16@example.com', 1),
(17, 'user17', 'password17', 'user17@example.com', 2),
(18, 'user18', 'password18', 'user18@example.com', 3),
(19, 'user19', 'password19', 'user19@example.com', 1),
(20, 'user20', 'password20', 'user20@example.com', 2),
(21, 'user21', 'password21', 'user21@example.com', 3),
(22, 'user22', 'password22', 'user22@example.com', 1),
(23, 'user23', 'password23', 'user23@example.com', 2),
(24, 'user24', 'password24', 'user24@example.com', 3),
(25, 'user25', 'password25', 'user25@example.com', 1),
(26, 'user26', 'password26', 'user26@example.com', 2),
(27, 'user27', 'password27', 'user27@example.com', 3),
(28, 'user28', 'password28', 'user28@example.com', 1),
(29, 'user29', 'password29', 'user29@example.com', 2),
(30, 'user30', 'password30', 'user30@example.com', 3),
(31, 'user31', 'password31', 'user31@example.com', 1),
(32, 'user32', 'password32', 'user32@example.com', 2),
(33, 'user33', 'password33', 'user33@example.com', 3),
(34, 'user34', 'password34', 'user34@example.com', 1),
(35, 'user35', 'password35', 'user35@example.com', 2),
(36, 'user36', 'password36', 'user36@example.com', 3),
(37, 'user37', 'password37', 'user37@example.com', 1),
(38, 'user38', 'password38', 'user38@example.com', 2),
(39, 'user39', 'password39', 'user39@example.com', 3),
(40, 'user40', 'password40', 'user40@example.com', 1),
(41, 'user41', 'password41', 'user41@example.com', 2),
(42, 'user42', 'password42', 'user42@example.com', 3),
(43, 'user43', 'password43', 'user43@example.com', 1),
(44, 'user44', 'password44', 'user44@example.com', 2),
(45, 'user45', 'password45', 'user45@example.com', 3),
(46, 'user46', 'password46', 'user46@example.com', 1),
(47, 'user47', 'password47', 'user47@example.com', 2),
(48, 'user48', 'password48', 'user48@example.com', 3),
(49, 'user49', 'password49', 'user49@example.com', 1),
(50, 'user50', 'password50', 'user50@example.com', 2),
(51, 'user51', 'password51', 'user51@example.com', 3),
(52, 'user52', 'password52', 'user52@example.com', 1),
(53, 'user53', 'password53', 'user53@example.com', 2),
(54, 'user54', 'password54', 'user54@example.com', 3),
(55, 'user55', 'password55', 'user55@example.com', 1),
(56, 'user56', 'password56', 'user56@example.com', 2),
(57, 'user57', 'password57', 'user57@example.com', 3),
(58, 'user58', 'password58', 'user58@example.com', 1),
(59, 'user59', 'password59', 'user59@example.com', 2),
(60, 'user60', 'password60', 'user60@example.com', 3),
(61, 'user61', 'password61', 'user61@example.com', 1),
(62, 'user62', 'password62', 'user62@example.com', 2),
(63, 'user63', 'password63', 'user63@example.com', 3),
(64, 'user64', 'password64', 'user64@example.com', 1),
(65, 'user65', 'password65', 'user65@example.com', 2),
(66, 'user66', 'password66', 'user66@example.com', 3),
(67, 'user67', 'password67', 'user67@example.com', 1),
(68, 'user68', 'password68', 'user68@example.com', 2),
(69, 'user69', 'password69', 'user69@example.com', 3),
(70, 'user70', 'password70', 'user70@example.com', 1),
(71, 'user71', 'password71', 'user71@example.com', 2),
(72, 'user72', 'password72', 'user72@example.com', 3),
(73, 'user73', 'password73', 'user73@example.com', 1),
(74, 'user74', 'password74', 'user74@example.com', 2),
(75, 'user75', 'password75', 'user75@example.com', 3),
(76, 'user76', 'password76', 'user76@example.com', 1),
(77, 'user77', 'password77', 'user77@example.com', 2),
(78, 'user78', 'password78', 'user78@example.com', 3),
(79, 'user79', 'password79', 'user79@example.com', 1),
(80, 'user80', 'password80', 'user80@example.com', 2),
(81, 'user81', 'password81', 'user81@example.com', 3),
(82, 'user82', 'password82', 'user82@example.com', 1),
(83, 'user83', 'password83', 'user83@example.com', 2),
(84, 'user84', 'password84', 'user84@example.com', 3),
(85, 'user85', 'password85', 'user85@example.com', 1),
(86, 'user86', 'password86', 'user86@example.com', 2),
(87, 'user87', 'password87', 'user87@example.com', 3),
(88, 'user88', 'password88', 'user88@example.com', 1),
(89, 'user89', 'password89', 'user89@example.com', 2),
(90, 'user90', 'password90', 'user90@example.com', 3),
(91, 'user91', 'password91', 'user91@example.com', 1),
(92, 'user92', 'password92', 'user92@example.com', 2),
(93, 'user93', 'password93', 'user93@example.com', 3),
(94, 'user94', 'password94', 'user94@example.com', 1),
(95, 'user95', 'password95', 'user95@example.com', 2),
(96, 'user96', 'password96', 'user96@example.com', 3),
(97, 'user97', 'password97', 'user97@example.com', 1),
(98, 'user98', 'password98', 'user98@example.com', 2),
(99, 'user99', 'password99', 'user99@example.com', 3),
(100, 'user100', 'password100', 'user100@example.com', 1);

INSERT INTO customers (id, first_name, last_name, address, phone_no, credit_card_no, user_id) VALUES
(1, 'John', 'Doe', '123 Main St', '555-1234', '1234', 1),
(2, 'John', 'Doe', '123 Main St', '555-12134', '** ** **** **** 1234', 11),
(3, 'Jane', 'Smith', '456 Elm St', '555-5678', '** ** **** **** 5678', 2),
(4, 'David', 'Johnson', '789 Oak St', '555-9012', '** ** **** **** 9012', 3),
(5, 'Sarah', 'Williams', '321 Pine St', '555-3456', '** ** **** **** 3456', 4),
(6, 'Michael', 'Brown', '654 Cedar St', '555-7890', '** ** **** **** 7890', 5),
(7, 'Emily', 'Jones', '987 Maple St', '555-2345', '** ** **** **** 2345', 6),
(8, 'Daniel', 'Davis', '210 Birch St', '555-6789', '** ** **** **** 6789', 7),
(9, 'Olivia', 'Miller', '543 Walnut St', '555-0123', '** ** **** **** 0123', 8),
(10, 'Matthew', 'Taylor', '876 Spruce St', '555-4567', '** ** **** **** 4567', 9),
(11, 'Sophia', 'Wilson', '109 Oak St', '555-8901', '** ** **** **** 8901', 10),
(12, 'Sophie', 'Walker', '654 Oak St', '555-2222', '** ** **** **** 2222', 12),
(13, 'Christopher', 'Thomas', '321 Cedar St', '555-3333', '** ** **** **** 3333', 13),
(14, 'Emma', 'Roberts', '789 Pine St', '555-4444', '** ** **** **** 4444', 14),
(15, 'Daniel', 'Lee', '456 Maple St', '555-5555', '** ** **** **** 5555', 15),
(16, 'Olivia', 'Harris', '123 Birch St', '555-6666', '** ** **** **** 6666', 16),
(17, 'Matthew', 'Clark', '210 Walnut St', '555-7777', '** ** **** **** 7777', 17),
(18, 'Emily', 'Lewis', '543 Spruce St', '555-8888', '** ** **** **** 8888', 18),
(19, 'Ryan', 'Young', '876 Oak St', '555-9999', '** ** **** **** 9999', 19),
(20, 'Grace', 'Walker', '109 Elm St', '555-0000', '** ** **** **** 0000', 20),
(21, 'Ethan', 'Hall', '987 Cedar St', '555-1111', '** ** **** **** 1111', 21),
(22, 'James', 'Baker', '321 Maple St', '555-33233', '** ** **** **** 33313', 23),
(23, 'Mia', 'Wright', '789 Birch St', '555-44144', '** ** **** **** 44344', 24),
(24, 'Benjamin', 'Scott', '456 Walnut St', '555-55551', '** ** **** **** 55525', 25),
(25, 'Ava', 'Green', '123 Spruce St', '555-66366', '** ** **** **** 66616', 26),
(26, 'William', 'Adams', '210 Oak St', '555-77177', '** ** **** **** 71777', 27),
(27, 'Charlotte', 'Turner', '543 Elm St', '555-88188', '** ** **** **** 88388', 28),
(28, 'Alexander', 'Parker', '876 Cedar St', '555-99919', '** ** **** **** 99199', 29),
(29, 'Harper', 'Collins', '109 Pine St', '555-00010', '** ** **** **** 01000', 30),
(30, 'Liam', 'Smith', '210 Elm St', '555-11111', '** ** **** **** 11111', 31);

INSERT INTO airline_companies (id, name, country_id, user_id) VALUES
(1, 'Airline Company 1', 1, 1),
(2, 'Airline Company 2', 2, 2),
(3, 'Airline Company 3', 3, 3),
(4, 'Airline Company 4', 4, 4),
(5, 'Airline Company 5', 5, 5),
(6, 'Airline Company 6', 6, 6),
(7, 'Airline Company 7', 7, 7),
(8, 'Airline Company 8', 8, 8),
(9, 'Airline Company 9', 9, 9),
(10, 'Airline Company 10', 10, 10),
(11, 'Airline Company 11', 11, 11),
(12, 'Airline Company 12', 12, 12),
(13, 'Airline Company 13', 13, 13),
(14, 'Airline Company 14', 14, 14),
(15, 'Airline Company 15', 15, 15),
(16, 'Airline Company 16', 16, 16),
(17, 'Airline Company 17', 17, 17),
(18, 'Airline Company 18', 18, 18),
(19, 'Airline Company 19', 19, 19),
(20, 'Airline Company 20', 20, 20),
(21, 'Airline Company 21', 21, 21),
(22, 'Airline Company 22', 22, 22),
(23, 'Airline Company 23', 23, 23),
(24, 'Airline Company 24', 24, 24),
(25, 'Airline Company 25', 25, 25),
(26, 'Airline Company 26', 26, 26),
(27, 'Airline Company 27', 27, 27),
(28, 'Airline Company 28', 28, 28),
(29, 'Airline Company 29', 29, 29),
(30, 'Airline Company 30', 30, 30);

INSERT INTO administrators (id, first_name, last_name, user_id) VALUES
(1, 'John', 'Doe', 1),
(2, 'Jane', 'Smith', 2),
(3, 'Michael', 'Johnson', 3),
(4, 'Emily', 'Williams', 4),
(5, 'David', 'Brown', 5),
(6, 'Olivia', 'Miller', 6),
(7, 'James', 'Taylor', 7),
(8, 'Sophia', 'Anderson', 8),
(9, 'Daniel', 'Thomas', 9),
(10, 'Ava', 'Jackson', 10);

INSERT INTO flights (id, airline_company_id, origin_country_id, destination_country_id, departure_time, landing_time, remaining_tickets) VALUES
(1, 1, 1, 2, '2023-06-20 10:00:00', '2023-06-20 12:00:00', 150),
(2, 2, 3, 4, '2023-06-21 14:30:00', '2023-06-21 16:30:00', 200),
(3, 3, 5, 6, '2023-06-22 09:15:00', '2023-06-22 11:15:00', 100),
(4, 4, 7, 8, '2023-06-23 18:45:00', '2023-06-23 20:45:00', 50),
(5, 5, 9, 10, '2023-06-24 11:30:00', '2023-06-24 13:30:00', 120),
(6, 6, 11, 12, '2023-06-25 16:00:00', '2023-06-25 18:00:00', 80),
(7, 7, 13, 14, '2023-06-26 08:45:00', '2023-06-26 10:45:00', 90),
(8, 8, 15, 16, '2023-06-27 13:15:00', '2023-06-27 15:15:00', 70),
(9, 9, 17, 18, '2023-06-28 17:30:00', '2023-06-28 19:30:00', 110),
(10, 10, 19, 20, '2023-06-29 12:00:00', '2023-06-29 14:00:00', 160),
(11, 11, 21, 22, '2023-06-30 15:45:00', '2023-06-30 17:45:00', 130),
(12, 12, 23, 24, '2023-07-01 10:30:00', '2023-07-01 12:30:00', 180),
(13, 13, 25, 26, '2023-07-02 14:00:00', '2023-07-02 16:00:00', 90),
(14, 14, 27, 28, '2023-07-03 09:45:00', '2023-07-03 11:45:00', 140),
(15, 15, 29, 30, '2023-07-04 16:30:00', '2023-07-04 18:30:00', 100),
(16, 16, 31, 32, '2023-07-05 08:15:00', '2023-07-05 10:15:00', 70),
(17, 17, 33, 34, '2023-07-06 13:45:00', '2023-07-06 15:45:00', 120),
(18, 18, 35, 36, '2023-07-07 18:00:00', '2023-07-07 20:00:00', 80),
(19, 9, 17, 18, '2023-06-28 17:30:00', '2023-06-28 19:30:00', 110),
(20, 10, 19, 20, '2023-06-29 12:00:00', '2023-06-29 14:00:00', 160),
(21, 11, 21, 22, '2023-06-30 15:45:00', '2023-06-30 17:45:00', 130),
(22, 12, 23, 24, '2023-07-01 10:30:00', '2023-07-01 12:30:00', 180),
(23, 13, 25, 26, '2023-07-02 14:00:00', '2023-07-02 16:00:00', 90),
(24, 14, 27, 28, '2023-07-03 09:45:00', '2023-07-03 11:45:00', 140),
(25, 15, 29, 30, '2023-07-04 16:30:00', '2023-07-04 18:30:00', 100),
(26, 16, 31, 32, '2023-07-05 08:15:00', '2023-07-05 10:15:00', 70),
(27, 17, 33, 34, '2023-07-06 13:45:00', '2023-07-06 15:45:00', 120),
(28, 18, 35, 36, '2023-07-07 18:00:00', '2023-07-07 20:00:00', 80),
(29, 19, 37, 38, '2023-07-08 11:30:00', '2023-07-08 13:30:00', 110),
(30, 20, 39, 40, '2023-07-09 15:00:00', '2023-07-09 17:00:00', 60),
(31, 22, 43, 44, '2023-07-11 14:30:00', '2023-07-11 16:30:00', 90),
(32, 23, 45, 46, '2023-07-12 18:15:00', '2023-07-12 20:15:00', 120),
(33, 24, 47, 48, '2023-07-13 11:45:00', '2023-07-13 13:45:00', 80),
(34, 25, 49, 50, '2023-07-14 16:30:00', '2023-07-14 18:30:00', 110),
(35, 26, 51, 52, '2023-07-15 09:15:00', '2023-07-15 11:15:00', 70),
(36, 27, 53, 54, '2023-07-16 13:45:00', '2023-07-16 15:45:00', 100),
(37, 28, 55, 56, '2023-07-17 17:30:00', '2023-07-17 19:30:00', 130),
(38, 29, 57, 58, '2023-07-18 12:00:00', '2023-07-18 14:00:00', 90),
(39, 30, 59, 60, '2023-07-19 15:45:00', '2023-07-19 17:45:00', 120),
(40, 1, 61, 62, '2023-07-20 09:15:00', '2023-07-20 11:15:00', 70),
(41, 2, 63, 64, '2023-07-21 13:45:00', '2023-07-21 15:45:00', 100),
(42, 3, 65, 66, '2023-07-22 17:30:00', '2023-07-22 19:30:00', 130),
(43, 4, 67, 68, '2023-07-23 12:00:00', '2023-07-23 14:00:00', 90),
(44, 5, 69, 70, '2023-07-24 15:45:00', '2023-07-24 17:45:00', 120),
(45, 6, 71, 72, '2023-07-25 09:15:00', '2023-07-25 11:15:00', 80),
(46, 7, 73, 74, '2023-07-26 13:45:00', '2023-07-26 15:45:00', 110),
(47, 8, 75, 76, '2023-07-27 18:30:00', '2023-07-27 20:30:00', 70),
(48, 9, 77, 78, '2023-07-28 11:00:00', '2023-07-28 13:00:00', 100),
(49, 10, 79, 80, '2023-07-29 15:15:00', '2023-07-29 17:15:00', 200),
(50, 21, 1, 2, '2023-08-09 09:45:00', '2023-08-09 11:45:00', 80);

INSERT INTO tickets (id, flight_id, customer_id) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 2, 2),
(4, 3, 2),
(5, 3, 3),
(6, 4, 2),
(7, 4, 4),
(8, 5, 5),
(9, 6, 6),
(10, 7, 7),
(11, 8, 8),
(12, 9, 9),
(13, 10, 10),
(14, 11, 11),
(15, 12, 12),
(16, 13, 13),
(17, 14, 14),
(18, 15, 15),
(19, 16, 16),
(20, 17, 17),
(21, 18, 18),
(22, 19, 19),
(23, 20, 20),
(24, 21, 21),
(25, 22, 22),
(26, 23, 23),
(27, 24, 24),
(28, 25, 25),
(29, 26, 26),
(30, 27, 27),
(31, 28, 28),
(32, 29, 29),
(33, 30, 30);