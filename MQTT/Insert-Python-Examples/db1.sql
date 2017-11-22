DATABASE SYSADMIN;

DROP DATABASE if exists db1;
CREATE DATABASE db1 with log;

DATABASE db1;


--
-- Create the table (relational) 
--

create table tab1  
(
   col1 integer,
   col2 integer,
   col3 char(50)
);

