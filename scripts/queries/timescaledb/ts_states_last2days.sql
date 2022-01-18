--shows last 2 days worth of data in states table for phase 1 
--https://popsql.com/learn-sql/postgresql/how-to-query-date-and-time-in-postgresql

-- timescaledb
SELECT entity_id, domain, measurement, created, value
FROM states
WHERE states.entity_id ='phase1' 
AND (states.created > (SELECT (MAX(states.created)-'2 days'::interval) FROM states))


