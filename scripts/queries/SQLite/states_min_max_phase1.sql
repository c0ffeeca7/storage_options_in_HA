
--SQLite
SELECT entity_id, created, value, domain, measurement,
Max(states.value) as max_value,
Min(states.value) as min_value,
strftime("%Y-%m-%d", states.created) as 'date'

FROM states
WHERE states.entity_id = "phase1"
GROUP BY entity_id, strftime("%Y-%m-%d", states.created)
ORDER BY states.created DESC;


