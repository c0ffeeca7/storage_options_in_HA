-- shows data in states table for phase1, summed up per month

SELECT entity_id, domain, measurement,
SUM(states.value) AS 'montly-total',
strftime("%Y-%m", states.created) AS 'month'

FROM states
WHERE states.entity_id ="phase1"
GROUP BY strftime("%Y-%m", states.created)
ORDER BY states.created DESC;