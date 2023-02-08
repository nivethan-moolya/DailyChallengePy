'''
Date: Feb 07
Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
'''
select t1.name from CITY t1 JOIN COUNTRY t2 on t1.CountryCode = t2.CODE where t2.continent = 'Africa';