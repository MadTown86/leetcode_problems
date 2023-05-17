--https://leetcode.com/problems/delete-duplicate-emails/

DELETE p1.id
FROM person p1, person p2
WHERE p1.id > p2.id AND p1.email = p2.email;


