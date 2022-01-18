--shows last 2 days worth of data in statistics table for phase 1
 
-- the statistics table holds the mean per hour. 
--The states table, for comparison, holds values per 5s.
SELECT id, entity_id, created as 'date time',  mean
FROM statistics
WHERE statistics.entity_id ="phase1" 
AND (statistics.created > (SELECT datetime(MAX(statistics.created),'-2 day') FROM statistics))
GROUP BY created
ORDER BY created DESC;

