'''
Date: Feb 06
01 Challenge: Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
'''
Select distinct city from station where right(city,1) not in ('a','e','i','o','u');

'''
Date: Feb 06
02 Challenge: Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
'''
select distinct city from station where right(city,1) not in ('a','e','i','o','u') OR left(city,1) not in ('a','e','i','o','u')

'''
Date: Feb 07
03 Challenge: Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. 
If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), 
secondary sort them by ascending ID.
'''
select name from students where marks > 75 order by right(name, 3), id;

'''
Date: Feb 07
05 Challenge: Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
'''
select name from employee order by name asc;

'''
Date: Feb 07
06 Challenge: Write a query that prints a list of employee names (i.e.: the name attribute) 
for employees in Employee having a salary greater than  per month who have been employees for less than  months. Sort your result by ascending employee_id.
'''
select name from employee where salary > 2000 and months<10 order by employee_id asc; 