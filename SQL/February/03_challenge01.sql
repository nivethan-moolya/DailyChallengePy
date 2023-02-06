'''
01 Challenge: Query the two cities in STATION with the shortest and longest CITY names, 
as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
'''

select city, length(city) from station where length(city)=
                                (select max(length(city)) from station);
select city, length(city) from station where length(city) = 
                                (select min(length(city)) from station) order by city asc limit 1;

'''
02 Challenge: Query the list of CITY names starting with vowels 
(i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
'''

select distinct city from station where LEFT(CITY, 1) IN ('a','e','i','o','u');

'''
03 Challenge:Query the list of CITY names ending with vowels 
(a, e, i, o, u) from STATION. Your result cannot contain duplicates.
'''
select distinct city from station where RIGHT(CITY, 1) IN('a','e','i','o','u');