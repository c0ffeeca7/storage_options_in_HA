-- shows data in states table for phase1, summed up per day
-- https://popsql.com/learn-sql/postgresql/how-to-group-by-time-in-postgresql

-- query used in timescaledb
SELECT MAX(states.entity_id), max(states.domain), max(states.measurement),
SUM(states.value) AS dailyTotal,
--MAX(date_trunc('day', states.created)) as date
--date_trunc('day', states.created) as date
time_bucket('1 day', created) AS day_bucket

FROM states
WHERE states.entity_id ='phase1'
--GROUP BY date_trunc('day', created);
GROUP BY day_bucket
ORDER BY day_bucket DESC;
