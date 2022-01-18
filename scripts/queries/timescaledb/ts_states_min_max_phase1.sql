--show min, max values per day
--https://popsql.com/learn-sql/postgresql/how-to-query-date-and-time-in-postgresql

-- timescaledb
SELECT MAX(entity_id), MAX(domain), MAX(measurement),
MAX(states.value) AS maxValue,
MIN(states.value) AS minValue,
--date_trunc('day', states.created) as date
time_bucket('1 day', created) AS day_bucket

FROM states
WHERE states.entity_id ='phase1'
--GROUP BY date_trunc('day', states.created)
--ORDER BY date_trunc('day', states.created) DESC;
GROUP BY day_bucket
ORDER BY day_bucket DESC


