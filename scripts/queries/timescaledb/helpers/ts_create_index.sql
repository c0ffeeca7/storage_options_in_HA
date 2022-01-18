-- DROP INDEX IF EXISTS public.states_created_entity_idx;

CREATE INDEX IF NOT EXISTS states_created_entity_idx
    ON public.states USING btree
    (created DESC NULLS LAST, entity_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
    
-- DROP INDEX IF EXISTS public.states_created_idx;

CREATE INDEX IF NOT EXISTS states_created_idx
    ON public.states USING btree
    (created DESC NULLS FIRST)
    TABLESPACE pg_default;
    
-- DROP INDEX IF EXISTS public.states_entity_created_idx;

CREATE INDEX IF NOT EXISTS states_entity_created_idx
    ON public.states USING btree
    (entity_id COLLATE pg_catalog."default" DESC NULLS LAST, created DESC NULLS LAST)
    TABLESPACE pg_default;
    
-- DROP INDEX IF EXISTS public.states_entity_id_idx;

CREATE INDEX IF NOT EXISTS states_entity_id_idx
    ON public.states USING btree
    (entity_id COLLATE pg_catalog."default" DESC NULLS LAST)
    TABLESPACE pg_default;
    
CREATE INDEX group_by_day_index 
ON public.states USING btree
(date_trunc('day', states.created))
TABLESPACE pg_default;

CREATE INDEX group_by_month_index 
ON public.states USING btree
(date_trunc('month', states.created))
TABLESPACE pg_default;

CREATE INDEX group_by_year_index 
ON public.states USING btree
(date_trunc('year', states.created))
TABLESPACE pg_default;

-- DROP INDEX IF EXISTS public.states_created_day_idx;

CREATE INDEX IF NOT EXISTS states_created_day_idx
    ON public.states USING btree
    (time_bucket('1 day'::interval, created) ASC NULLS LAST)
    TABLESPACE pg_default;
    
CREATE INDEX IF NOT EXISTS states_created_week_idx
    ON public.states USING btree
    (time_bucket('1 week'::interval, created) ASC NULLS LAST)
    TABLESPACE pg_default;
    
-- Index: group_by_month_entity_index
-- DROP INDEX IF EXISTS public.group_by_month_entity_index;

CREATE INDEX IF NOT EXISTS group_by_month_entity_index
    ON public.states USING btree
    (date_trunc('month'::text, created) ASC NULLS LAST, entity_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default
    WHERE entity_id::text = 'phase1'::text;
    
-- Index: group_by_month_entity_index
-- DROP INDEX IF EXISTS public.group_by_month_entity_index;

CREATE INDEX IF NOT EXISTS group_by_year_entity_index
    ON public.states USING btree
    (date_trunc('year'::text, created) ASC NULLS LAST, entity_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default
    WHERE entity_id::text = 'phase1'::text;
    
-- Index: states_created_week_entity_idx
-- DROP INDEX IF EXISTS public.states_created_week_entity_idx;

CREATE INDEX IF NOT EXISTS states_created_week_entity_idx
    ON public.states USING btree
    (time_bucket('7 days'::interval, created) ASC NULLS LAST, entity_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default
    WHERE entity_id::text = 'phase1'::text;
    
-- Index: states_created_day_entity_idx
-- DROP INDEX IF EXISTS public.states_created_day_entity_idx;

CREATE INDEX IF NOT EXISTS states_created_day_entity_idx
    ON public.states USING btree
    (time_bucket('1 day'::interval, created) ASC NULLS LAST, entity_id COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default
    WHERE entity_id::text = 'phase1'::text;
