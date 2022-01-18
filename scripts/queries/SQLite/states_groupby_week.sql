-- shows data in states table for phase1, summed up per week
-- https://www.sqlite.org/lang_datefunc.html

SELECT entity_id, domain, measurement,
SUM(states.value) AS 'weekly-total',
strftime("%Y-%m-%W", states.created) as 'year-month-week'

FROM states
WHERE states.entity_id ="phase1"
GROUP BY strftime("%Y-%m-%W", states.created) 
ORDER BY states.created DESC;