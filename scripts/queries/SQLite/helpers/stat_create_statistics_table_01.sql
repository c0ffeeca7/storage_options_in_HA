--creates the statistic table

CREATE TABLE statistics (
	id INTEGER NOT NULL,
	entity_id VARCHAR(255),
	created DATETIME, 
	mean FLOAT, 
	min FLOAT, 
	max FLOAT, 
	sum FLOAT, 
	sum_increase FLOAT,
	PRIMARY KEY (id)	
);

CREATE INDEX "stats_entity_id_index" ON "statistics" (
	"entity_id"
);

CREATE INDEX "stats_timestamp_index" ON "statistics" (
	"created"
);