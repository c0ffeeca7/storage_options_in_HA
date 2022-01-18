
--sqlite query
SELECT id, entity_id, created, 
SUM(statistics.sum) AS 'total energy (Wh)'
FROM statistics
WHERE statistics.entity_id ="phase1" OR 
entity_id = "phase2" OR entity_id = "phase3"
GROUP BY created
ORDER BY created DESC;


