'''
Date: Feb 02
01 Challenge: Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
'''
select * from CITY where COUNTRYCODE = 'USA' and POPULATION > 100000


'''
02 Challenge: Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
'''
select NAME from CITY where POPULATION > 120000 AND COUNTRYCODE = 'USA'



'''
03 Challenge: Query all columns for a city in CITY with the ID 1661.
'''
select * from CITY
    where ID = 1661;

'''
04 Challenge: Query a list of CITY names from STATION for cities that have an even ID number. 
Print the results in any order, but exclude duplicates from the answer.
'''
select distinct city from station 
    where id % 2 =0;

'''
05 Challenge: Find the difference between the total number of CITY entries in the table 
and the number of distinct CITY entries in the table.
'''
select 
(select count(city) from station) - (select count(distinct city) from station)