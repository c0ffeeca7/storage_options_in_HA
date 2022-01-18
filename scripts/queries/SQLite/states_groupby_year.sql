-- shows data in states table for phase1, summed up per year
-- https://www.sqlite.org/lang_datefunc.html

--sqlite
SELECT entity_id, domain, measurement,
SUM(states.value) AS 'yearly-total',
strftime("%Y", states.created) as 'year'
FROM states
WHERE states.entity_id = "phase1"
GROUP BY strftime("%Y", states.created) 
ORDER BY states.created DESC;
