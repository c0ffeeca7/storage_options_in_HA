-- shows values in states table for phase 1 for Sundays and Mondays

-- query used in timescaledb
SELECT MAX(entity_id), MAX(domain), 
MAX(measurement),
SUM(states.value) AS valuePerDay, 
time_bucket('1 day', created) AS day_bucket

FROM states
WHERE states.entity_id ='phase1' 
AND extract(DOW FROM states.created) IN (0,1)
GROUP BY day_bucket
ORDER BY day_bucket DESC;
