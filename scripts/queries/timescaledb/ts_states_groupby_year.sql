-- shows data in states table for phase1, summed up per year
-- https://popsql.com/learn-sql/postgresql/how-to-group-by-time-in-postgresql

-- query used in timescaledb
SELECT max(entity_id), max(domain), 
max(measurement),
SUM(states.value) AS dailyTotal,
date_trunc('year', states.created) as date

FROM states
WHERE states.entity_id ='phase1'
GROUP BY date_trunc('year', states.created);
