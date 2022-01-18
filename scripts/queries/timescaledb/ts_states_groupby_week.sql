-- shows data in states table for phase1, summed up per week
-- https://popsql.com/learn-sql/postgresql/how-to-group-by-time-in-postgresql
-- query used in timescaledb

SELECT MAX(entity_id), MAX(domain), MAX(measurement),
SUM(states.value) AS dailyTotal,
--date_trunc('week', states.created) as date
time_bucket('1 week', created) AS week_bucket

FROM states
WHERE states.entity_id ='phase1'
--GROUP BY date_trunc('week', states.created);
GROUP BY week_bucket
ORDER BY week_bucket DESC;
