-- shows data in states table for phase1, summed up per month
-- https://popsql.com/learn-sql/postgresql/how-to-group-by-time-in-postgresql

-- query used in timescaledb

SELECT MAX(entity_id), MAX(domain), MAX(measurement),
SUM(states.value) AS dailyTotal,
--note: time_bucket(month) is not supported
date_trunc('month', states.created) AS date
FROM states
WHERE states.entity_id ='phase1' 
GROUP BY date_trunc('month', states.created);

