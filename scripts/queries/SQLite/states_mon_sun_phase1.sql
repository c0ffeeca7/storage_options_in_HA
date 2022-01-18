-- shows values in states table for phase 1 for Sundays and Mondays
-- https://www.sqlite.org/lang_datefunc.html

--SQLite query
SELECT MAX(entity_id), created as 'date time', 
domain, measurement,
sum(value) as 'value per day (Wh)'

FROM states
WHERE (states.entity_id ="phase1" )
AND (strftime("%w", states.created) IN ("0", "1"))  	
GROUP BY strftime("%Y-%m-%d", states.created)
ORDER BY states.created DESC;
