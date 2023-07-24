-- script that lists the number of records

SELECT score, COUNT(*) AS num_records
FROM second_table
GROUP BY score
ORDER BY score DESC;