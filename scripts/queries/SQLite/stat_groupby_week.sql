-- shows data for phase1, summed up per week
-- https://www.sqlite.org/lang_datefunc.html

SELECT id, entity_id,
SUM(statistics.sum) AS weekly_total_Wh,
strftime("%Y-%m-%W", statistics.created) as 'year-month-week'

FROM statistics
WHERE statistics.entity_id ="phase1"
GROUP BY strftime("%Y-%m-%W", statistics.created)
ORDER BY created DESC;