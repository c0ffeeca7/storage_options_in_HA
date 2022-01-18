-- summing up 3 phases to show total enery per 5 seconds.

-- query used in timescaledb
SELECT MAX(entity_id), MAX(domain), MAX(measurement),
SUM(states.value) AS totalEnergy

FROM states
WHERE (states.entity_id ='phase1' 
OR states.entity_id ='phase2' OR states.entity_id ='phase3') 
GROUP BY states.created;
