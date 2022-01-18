-- calculates and adds sum_increase. The cumulative sum, as used e.g. with energy meters.

--SELECT * FROM statistics

UPDATE statistics
SET sum_increase = (SELECT sum(s2.sum) FROM statistics as s2 WHERE s2.created <= statistics.created AND s2.entity_id = statistics.entity_id);
