-- sqlite query
SELECT entity_id, created, value,
domain, measurement, 
SUM(states.value) AS 'total energy (Wh)'
FROM states
WHERE (states.entity_id ="phase1" 
OR entity_id = "phase2" OR entity_id = "phase3")
GROUP BY created
ORDER BY created DESC;
