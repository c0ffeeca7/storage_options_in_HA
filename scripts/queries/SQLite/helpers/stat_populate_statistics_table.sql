

-- copies data from states table, 
-- adds precalculated aggregations to statistics table
-- aggregation period: 1 hour, 
--(see https://data.home-assistant.io/docs/statistics/)

INSERT INTO statistics (entity_id, created, mean, min, max, sum)
SELECT states.entity_id, strftime("%Y-%m-%d %H", states.created), 
avg(states.value),
min(states.value),
max(states.value),
sum(states.value)
FROM states 
--WHERE states.created < date("2020-11-16")
GROUP BY entity_id, strftime("%Y-%m-%d %H", states.created)
