
-- shows data in statistics table for phase1, summed up per year
-- as the statistics table does not hold each value per 5s, but holds the sum per hour, this sum is used to calculate the yearly total.
-- the resulting values are slightly different, of course.
-- https://www.sqlite.org/lang_datefunc.html

SELECT id, entity_id,
SUM(statistics.sum) AS 'yearly-total',
strftime("%Y", statistics.created) as 'year' 

FROM statistics 
WHERE statistics.entity_id = 'phase1'
GROUP BY strftime("%Y", statistics.created)
ORDER BY created DESC;