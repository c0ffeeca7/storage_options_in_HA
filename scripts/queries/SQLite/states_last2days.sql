--shows last 2 days worth of data in states table for phase 1 

--SQLite
SELECT entity_id, domain, measurement, created, value

FROM states
WHERE states.entity_id ="phase1" 
AND (states.created > (SELECT datetime(MAX(states.created),'-2 day') FROM states))
GROUP BY entity_id, states.created
ORDER BY states.created DESC;


