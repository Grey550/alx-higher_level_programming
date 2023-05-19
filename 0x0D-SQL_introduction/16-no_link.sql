-- Script that lists all records of the table second_table and list rows without a name value in a descending order.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
