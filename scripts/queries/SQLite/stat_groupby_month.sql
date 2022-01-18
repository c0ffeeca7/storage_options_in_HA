-- shows data for phase1, summed up per month
-- as the statistics table does not hold each value per 5s, but holds the sum per hour, this sum is used to calculate the monthly value.
-- the resulting values are a bit different, of course.
-- https://www.sqlite.org/lang_datefunc.html

SELECT id, entity_id,
SUM(statistics.sum) AS 'montly-total',
strftime("%Y-%m", statistics.created) as 'month' 

FROM statistics 
WHERE statistics.entity_id = 'phase1'
GROUP BY strftime("%Y-%m", statistics.created)
ORDER BY created DESC;
