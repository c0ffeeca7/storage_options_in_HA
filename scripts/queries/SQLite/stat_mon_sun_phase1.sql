-- shows values in statistics table for phase1 for Sundays and Mondays
-- https://www.sqlite.org/lang_datefunc.html

--SQLite
SELECT id, entity_id, created as 'date',
sum(statistics.sum) as 'value per day (Wh)'
FROM statistics
WHERE (statistics.entity_id ="phase1" )
AND (strftime("%w", statistics.created) IN ("0", "1"))
GROUP BY strftime("%Y-%m-%d", statistics.created)
ORDER BY created DESC;
