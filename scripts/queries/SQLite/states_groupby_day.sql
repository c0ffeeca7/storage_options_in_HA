-- shows data in states table for phase1, summed up per day
-- https://www.sqlite.org/lang_datefunc.html

SELECT entity_id, domain, measurement,
SUM(states.value) AS 'daily-total',
strftime("%Y-%m-%d", states.created) as 'date'

FROM states
WHERE states.entity_id ="phase1" 
GROUP BY strftime("%Y-%m-%d", states.created)
ORDER BY states.created DESC;
