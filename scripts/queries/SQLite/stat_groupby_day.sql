-- shows data in statistics table for phase1, summed up per day
-- as the statistics table does not hold each value per 5s, but holds the sum per hour, this sum is used to calculate the daily value.
-- the resulting values are slightly different, of course.
-- https://www.sqlite.org/lang_datefunc.html

--SQLite
SELECT id, entity_id,
SUM(statistics.sum) AS 'daily-total',
strftime("%Y-%m-%d", statistics.created) as 'date' 
FROM statistics 
WHERE statistics.entity_id = 'phase1'
GROUP BY strftime("%Y-%m-%d", statistics.created)
ORDER BY created DESC;


