CREATE INDEX "states_created_idx" ON "states" (
	"created"	DESC
);
CREATE INDEX "states_entity_idx" ON "states" (
	"entity_id"
);
CREATE INDEX "states_entity_created_idx" ON "states" (
	"entity_id",
	"created"	DESC
);
CREATE INDEX "stats_created_idx" ON "statistics" (
	"created"	DESC
);

CREATE INDEX "stats_entity_id_index" ON "statistics" (
	"entity_id"
);
CREATE INDEX "statistics_entity_created_idx" ON "statistics" (
	"entity_id",
	"created"	DESC
);
