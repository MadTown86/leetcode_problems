*/ https://leetcode.com/problems/combine-two-tables/

SELECT Person.firstName, Person.LastName, Address.city, Address.state
FROM Person
LEFT JOIN Address
ON Person.personId = Address.personId