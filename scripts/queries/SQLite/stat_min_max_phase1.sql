
--SQLite
SELECT id, entity_id, min, max,
MAX(statistics.created) as 'date'
FROM statistics
WHERE entity_id = 'phase1'
GROUP BY strftime("%Y-%m-%d", statistics.created)
ORDER BY created DESC;
