# define chart titles, boxplot titles and data sources required to create the boxplot charts in draw_boxplot_perGraph.py

graph_groupByWeek_CPU = {
    "chart_title": "Group by week - CPU Time (s)",
    "svg_name": "graph_groupByWeek_CPU",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/groupby_week_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_groupby_week_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_groupby_week_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_groupby_week_sql_log.csv',
            "column": 2,
        }
    ]
}

graph_groupByWeek_Memory_hwm = {
    "chart_title": "Group by week - Memory HWM (MiB)",
    "svg_name": "graph_groupByWeek_Memory_hwm",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/groupby_week_influx_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_groupby_week_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_groupby_week_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_groupby_week_sql_log.csv',
            "column": 3,
        }
    ]
}

graph_groupByWeek_io = {
    "chart_title": "Group by week - Disk I/O (MiB)",
    "svg_name": "graph_groupByWeek_io",
    "boxplots": [
        {
            "title of boxplot": "Influx DB reads",
            "filename": 'measurements/groupby_week_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads",
            "filename": 'measurements/states_groupby_week_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite Statistics reads",
            "filename": 'measurements/stat_groupby_week_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "Influx DB writes",
            "filename": 'measurements/groupby_week_influx_log.csv',
            "column": 5,
        },        
        {
            "title of boxplot": "SQLite States writes",
            "filename": 'measurements/states_groupby_week_sql_log.csv',
            "column": 5,
        },
        
        {
            "title of boxplot": "SQLite Statistics writes",
            "filename": 'measurements/stat_groupby_week_sql_log.csv',
            "column": 5,
        }
    ]
}

graph_minMax_CPU = {
    "chart_title": "Daily min/max - CPU Time (s)",
    "svg_name": "graph_minMax_CPU",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/min_max_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_min_max_phase1_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_min_max_phase1_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_min_max_phase1_sql_log.csv',
            "column": 2,
        }
    ]
}

graph_minMax_realtime = {
    "chart_title": "Daily min/max - Actual Time (s)",
    "svg_name": "graph_minMax_realtime",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/min_max_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_min_max_phase1_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_min_max_phase1_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_min_max_phase1_sql_log.csv',
            "column": 6,
        }
    ]
}

graph_minMax_Memory_hwm = {
    "chart_title": "Daily min/max - Memory HWM (MiB)",
    "svg_name": "graph_minMax_Memory_hwm",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/min_max_influx_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_min_max_phase1_sql_log.csv',
            "column": 3,
            "factor": 0.001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_min_max_phase1_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_min_max_phase1_sql_log.csv',
            "column": 3,
        }
    ]
}

graph_minMax_io = {
    "chart_title": "Daily min/max - Disk I/O (MiB)",
    "svg_name": "graph_minMax_io",
    "boxplots": [
        {
            "title of boxplot": "Influx DB reads",
            "filename": 'measurements/min_max_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads",
            "filename": 'measurements/states_min_max_phase1_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite Statistics reads",
            "filename": 'measurements/stat_min_max_phase1_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "Influx DB writes",
            "filename": 'measurements/min_max_influx_log.csv',
            "column": 5,
        },
        
        {
            "title of boxplot": "SQLite States writes",
            "filename": 'measurements/states_min_max_phase1_sql_log.csv',
            "column": 5,
        },
        
        {
            "title of boxplot": "SQLite Statistics writes",
            "filename": 'measurements/stat_min_max_phase1_sql_log.csv',
            "column": 5,
        }
    ]
}

graph_monSun_CPU = {
    "chart_title": "Daily total for Mondays and Sundays - CPU Time (s)",
    "svg_name": "graph_monSun_CPU",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/groupby_sun_mon_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_mon_sun_phase1_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_mon_sun_phase1_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_mon_sun_phase1_sql_log.csv',
            "column": 2,
        }
    ]
}

graph_monSun_realtime = {
    "chart_title": "Daily total for Mondays and Sundays - Actual Time (s)",
    "svg_name": "graph_monSun_realtime",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/groupby_sun_mon_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_mon_sun_phase1_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_mon_sun_phase1_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_mon_sun_phase1_sql_log.csv',
            "column": 6,
        }
    ]
}

graph_monSun_Memory_hwm = {
    "chart_title": "Daily total for Mondays and Sundays - Memory HWM (MiB)",
    "svg_name": "graph_monSun_Memory_hwm",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/groupby_sun_mon_influx_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_mon_sun_phase1_sql_log.csv',
            "column": 3,
            "factor": 0.001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_mon_sun_phase1_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_mon_sun_phase1_sql_log.csv',
            "column": 3,
        }
    ]
}

graph_monSun_io = {
    "chart_title": "Daily total for Mondays and Sundays- Disk I/O (MiB)",
    "svg_name": "graph_monSun_io",
    "boxplots": [
        {
            "title of boxplot": "Influx DB reads",
            "filename": 'measurements/groupby_sun_mon_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads",
            "filename": 'measurements/states_mon_sun_phase1_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite Statistics reads",
            "filename": 'measurements/stat_mon_sun_phase1_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "Influx DB writes",
            "filename": 'measurements/groupby_sun_mon_influx_log.csv',
            "column": 5,
        },
        
        {
            "title of boxplot": "SQLite States writes",
            "filename": 'measurements/states_mon_sun_phase1_sql_log.csv',
            "column": 5,
        },
        
        {
            "title of boxplot": "SQLite Statistics writes",
            "filename": 'measurements/stat_mon_sun_phase1_sql_log.csv',
            "column": 5,
        }
    ]
}

graph_last2_CPU = {
    "chart_title": "2 days worth of data - CPU Time (s)",
    "svg_name": "graph_last2_CPU",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/last2days_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_last2days_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_last2days_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_last2days_sql_log.csv',
            "column": 2,
        }
    ]
}

graph_last2_realtime = {
    "chart_title": "2 days worth of data - Actual time (s)",
    "svg_name": "graph_last2_realtime",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/last2days_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_last2days_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_last2days_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_last2days_sql_log.csv',
            "column": 6,
        }
    ]
}

graph_last2_Memory_hwm = {
    "chart_title": "2 days worth of data - Memory HWM (MiB)",
    "svg_name": "graph_last2_Memory_hwm",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/last2days_influx_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_last2days_sql_log.csv',
            "column": 3,
            "factor": 0.001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_last2days_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_last2days_sql_log.csv',
            "column": 3,
        }
    ]
}

graph_last2_io = {
    "chart_title": "2 days worth of data - Disk I/O (MiB)",
    "svg_name": "graph_last2_io",
    "boxplots": [
        {
            "title of boxplot": "Influx DB reads",
            "filename": 'measurements/last2days_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads",
            "filename": 'measurements/states_last2days_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite Statistics reads",
            "filename": 'measurements/stat_last2days_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "Influx DB writes",
            "filename": 'measurements/last2days_influx_log.csv',
            "column": 5,
        },
        
        {
            "title of boxplot": "SQLite States writes",
            "filename": 'measurements/states_last2days_sql_log.csv',
            "column": 5,
        },
        
        {
            "title of boxplot": "SQLite Statistics writes",
            "filename": 'measurements/stat_last2days_sql_log.csv',
            "column": 5,
        }
    ]
}

graph_sum_CPU = {
    "chart_title": "Sum of 3 phases to calculate total energy- CPU Time (s)",
    "svg_name": "graph_sum_CPU",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/sum_phases_using_pivot_01_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_sum_phase1_3_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_sum_phase1_3_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_sum_phase1_3_sql_log.csv',
            "column": 2,
        }
    ]
}

graph_sum_realtime = {
    "chart_title": "Sum of 3 phases to calculate total energy- Actual time (s)",
    "svg_name": "graph_sum_realtime",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/sum_phases_using_pivot_01_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_sum_phase1_3_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_sum_phase1_3_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_sum_phase1_3_sql_log.csv',
            "column": 6,
        }
    ]
}

graph_sum_Memory_hwm = {
    "chart_title": "Sum of 3 phases to calculate total energy - Memory HWM (MiB)",
    "svg_name": "graph_sum_Memory_hwm",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/sum_phases_using_pivot_01_influx_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_sum_phase1_3_sql_log.csv',
            "column": 3,
            "factor": 0.001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_sum_phase1_3_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_sum_phase1_3_sql_log.csv',
            "column": 3,
        }
    ]
}

graph_sum_io = {
    "chart_title": "Sum of 3 phases to calculate total energy - Disk I/O (MiB)",
    "svg_name": "graph_sum_io",
    "boxplots": [
        {
            "title of boxplot": "Influx DB reads",
            "filename": 'measurements/sum_phases_using_pivot_01_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads",
            "filename": 'measurements/states_sum_phase1_3_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite Statistics reads",
            "filename": 'measurements/stat_sum_phase1_3_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "Influx DB writes",
            "filename": 'measurements/sum_phases_using_pivot_01_influx_log.csv',
            "column": 5,
        },
        
        {
            "title of boxplot": "SQLite States writes",
            "filename": 'measurements/states_sum_phase1_3_sql_log.csv',
            "column": 5,
        },        
        {
            "title of boxplot": "SQLite Statistics writes",
            "filename": 'measurements/stat_sum_phase1_3_sql_log.csv',
            "column": 5,
        }
    ]
}


graph_groupByMonth_CPU = {
    "chart_title": "Group by month - CPU Time (s)",
    "svg_name": "graph_groupByMonth_CPU",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/groupby_month_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_groupby_month_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_groupby_month_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_groupby_month_sql_log.csv',
            "column": 2,
        }
    ]
}

graph_groupByMonth_Memory_hwm = {
    "chart_title": "Group by month - Memory HWM (MiB)",
    "svg_name": "graph_groupByMonth_Memory_hwm",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/groupby_month_influx_log.csv',
            "column": 3,
        },
         {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_groupby_month_sql_log.csv',
            "column": 3,
            "factor": 0.001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_groupby_month_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_groupby_month_sql_log.csv',
            "column": 3,
        }
    ]
}

graph_groupByMonth_io = {
    "chart_title": "Group by month - Disk I/O (MiB)",
    "svg_name": "graph_groupByMonth_io",
    "boxplots": [
        {
            "title of boxplot": "Influx DB reads",
            "filename": 'measurements/groupby_month_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads",
            "filename": 'measurements/states_groupby_month_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite Statistics reads",
            "filename": 'measurements/stat_groupby_month_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "Influx DB writes",
            "filename": 'measurements/groupby_month_influx_log.csv',
            "column": 5,
        },
        
        {
            "title of boxplot": "SQLite States writes",
            "filename": 'measurements/states_groupby_month_sql_log.csv',
            "column": 5,
        },        
        {
            "title of boxplot": "SQLite Statistics writes",
            "filename": 'measurements/stat_groupby_month_sql_log.csv',
            "column": 5,
        }
    ]
}

graph_groupByYear_CPU = {
    "chart_title": "Group by year - CPU Time (s)",
    "svg_name": "graph_groupByYear_CPU",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/groupby_year_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_groupby_year_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_groupby_year_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_groupby_year_sql_log.csv',
            "column": 2,
        }
    ]
}

graph_groupByYear_Memory_hwm = {
    "chart_title": "Group by year - Memory HWM (MiB)",
    "svg_name": "graph_groupByYear_Memory_hwm",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/groupby_year_influx_log.csv',
            "column": 3,
            "factor": 0.001,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_groupby_year_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_groupby_year_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_groupby_year_sql_log.csv',
            "column": 3,
        }
    ]
}

graph_groupByYear_io = {
    "chart_title": "Group by year - Disk I/O (MiB)",
    "svg_name": "graph_groupByYear_io",
    "boxplots": [
        {
            "title of boxplot": "Influx DB reads",
            "filename": 'measurements/groupby_year_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads",
            "filename": 'measurements/states_groupby_year_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite Statistics reads",
            "filename": 'measurements/stat_groupby_year_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "Influx DB writes",
            "filename": 'measurements/groupby_year_influx_log.csv',
            "column": 5,
        },
       
        {
            "title of boxplot": "SQLite States writes",
            "filename": 'measurements/states_groupby_year_sql_log.csv',
            "column": 5,
        },
        
        {
            "title of boxplot": "SQLite Statistics writes",
            "filename": 'measurements/stat_groupby_year_sql_log.csv',
            "column": 5,
        }
    ]
}

graph_groupByDay_CPU = {
    "chart_title": "Group by day - CPU Time (s)",
    "svg_name": "graph_groupByDay_CPU",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/groupby_day_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_groupby_day_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_groupby_day_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_groupby_day_sql_log.csv',
            "column": 2,
        }
    ]
}

graph_groupByDay_Memory_hwm = {
    "chart_title": "Group by day - Memory HWM (MiB)",
    "svg_name": "graph_groupByDay_Memory_hwm",
    "boxplots": [
        {
            "title of boxplot": "Influx DB",
            "filename": 'measurements/groupby_day_influx_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_groupby_day_sql_log.csv',
            "column": 3,
            "factor": 0.001,
        },
        {
            "title of boxplot": "SQLite States",
            "filename": 'measurements/states_groupby_day_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics",
            "filename": 'measurements/stat_groupby_day_sql_log.csv',
            "column": 3,
        }
    ]
}

graph_groupByDay_io = {
    "chart_title": "Group by year - Disk I/O (MiB)",
    "svg_name": "graph_groupByDay_io",
    "boxplots": [
        {
            "title of boxplot": "Influx DB reads",
            "filename": 'measurements/groupby_day_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads",
            "filename": 'measurements/states_groupby_day_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite Statistics reads",
            "filename": 'measurements/stat_groupby_day_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "Influx DB writes",
            "filename": 'measurements/groupby_day_influx_log.csv',
            "column": 5,
        },        
        {
            "title of boxplot": "SQLite States writes",
            "filename": 'measurements/states_groupby_day_sql_log.csv',
            "column": 5,
        },        
        {
            "title of boxplot": "SQLite Statistics writes",
            "filename": 'measurements/stat_groupby_day_sql_log.csv',
            "column": 5,
        }
    ]
}

graph_AllGroupBy_CPU = {
    "chart_title": "Group by day/week/month/year - CPU Time (s)",
    "svg_name": "graph_AllGroupBy_CPU",
    "boxplots": [
        {
            "title of boxplot": "Influx DB - day",
            "filename": 'measurements/groupby_day_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale - day",
            "filename": 'measurements/ts_states_groupby_day_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
         {
            "title of boxplot": "SQLite States - day",
            "filename": 'measurements/states_groupby_day_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics - day",
            "filename": 'measurements/stat_groupby_day_sql_log.csv',
            "column": 2,
        },  
        {
            "title of boxplot": "Influx DB - week",
            "filename": 'measurements/groupby_week_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale - week",
            "filename": 'measurements/ts_states_groupby_week_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States- week",
            "filename": 'measurements/states_groupby_week_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics - week",
            "filename": 'measurements/stat_groupby_week_sql_log.csv',
            "column": 2,
        }, 
        {
            "title of boxplot": "Influx DB - month",
            "filename": 'measurements/groupby_month_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale - month",
            "filename": 'measurements/ts_states_groupby_month_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
         {
            "title of boxplot": "SQLite States - month",
            "filename": 'measurements/states_groupby_month_sql_log.csv',
            "column": 2,
        },         
        {
            "title of boxplot": "SQLite Statistics - month",
            "filename": 'measurements/stat_groupby_month_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Influx DB - year",
            "filename": 'measurements/groupby_year_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale - year",
            "filename": 'measurements/ts_states_groupby_year_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States - year",
            "filename": 'measurements/states_groupby_year_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics - year",
            "filename": 'measurements/stat_groupby_year_sql_log.csv',
            "column": 2,
        }
    ]
}

graph_AllGroupBy_Memory_hwm = {
    "chart_title": "Group by day/week/month/year - Memory HWM (MiB)",
    "svg_name": "graph_AllGroupBy_Memory_hwm",
    "boxplots": [
        {
            "title of boxplot": "Influx DB -  day",
            "filename": 'measurements/groupby_day_influx_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Timescale - day",
            "filename": 'measurements/ts_states_groupby_day_sql_log.csv',
            "column": 3,
            "factor": 0.001,
        },
        {
            "title of boxplot": "SQLite States - day",
            "filename": 'measurements/states_groupby_day_sql_log.csv',
            "column": 3,
        },
         {
            "title of boxplot": "SQLite Statistics - day",
            "filename": 'measurements/stat_groupby_day_sql_log.csv',
            "column": 3,
        },   
        {
            "title of boxplot": "Influx DB - week",
            "filename": 'measurements/groupby_week_influx_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Timescale - week",
            "filename": 'measurements/ts_states_groupby_week_sql_log.csv',
            "column": 3,
            "factor": 0.001,
        },
        {
            "title of boxplot": "SQLite States - week",
            "filename": 'measurements/states_groupby_week_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics - week",
            "filename": 'measurements/stat_groupby_week_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Influx DB - month",
            "filename": 'measurements/groupby_month_influx_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Timescale - month",
            "filename": 'measurements/ts_states_groupby_month_sql_log.csv',
            "column": 3,
            "factor": 0.001,
        },
        {
            "title of boxplot": "SQLite States - month",
            "filename": 'measurements/states_groupby_month_sql_log.csv',
            "column": 3,
        },
         {
            "title of boxplot": "SQLite Statistics - month",
            "filename": 'measurements/stat_groupby_month_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Influx DB  - year",
            "filename": 'measurements/groupby_year_influx_log.csv',
            "column": 3,
        },        
        {
            "title of boxplot": "Timescale - year",
            "filename": 'measurements/ts_states_groupby_year_sql_log.csv',
            "column": 3,
            "factor": 0.001,
        },
        {
            "title of boxplot": "SQLite States - year",
            "filename": 'measurements/states_groupby_year_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics - year",
            "filename": 'measurements/stat_groupby_year_sql_log.csv',
            "column": 3,
        }
    ]
}

# graph_AllGroupBy_io = {
#     "chart_title": "Group by day/week/month/year - Disk I/O (MiB)",
#     "svg_name": "graph_AllGroupBy_io",
#     "boxplots": [
#         {
#             "title of boxplot": "Influx DB reads - day",
#             "filename": 'measurements/groupby_day_influx_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite States reads - day",
#             "filename": 'measurements/states_groupby_day_sql_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite Statistics reads - day",
#             "filename": 'measurements/stat_groupby_day_sql_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "Influx DB writes - day",
#             "filename": 'measurements/groupby_day_influx_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite States writes - day",
#             "filename": 'measurements/states_groupby_day_sql_log.csv',
#             "column": 5,
#         },
#          {
#             "title of boxplot": "SQLite Statistics writes - day",
#             "filename": 'measurements/stat_groupby_day_sql_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "Influx DB reads - week",
#             "filename": 'measurements/groupby_week_influx_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite States reads - week",
#             "filename": 'measurements/states_groupby_week_sql_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite Statistics reads - week",
#             "filename": 'measurements/stat_groupby_week_sql_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "Influx DB writes - week",
#             "filename": 'measurements/groupby_week_influx_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite States writes - week",
#             "filename": 'measurements/states_groupby_week_sql_log.csv',
#             "column": 5,
#         },         
#         {
#             "title of boxplot": "SQLite Statistics writes - week",
#             "filename": 'measurements/stat_groupby_week_sql_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "Influx DB reads - month",
#             "filename": 'measurements/groupby_month_influx_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite States reads - month",
#             "filename": 'measurements/states_groupby_month_sql_log.csv',
#             "column": 4,
#         },
#           {
#             "title of boxplot": "SQLite Statistics reads - month",
#             "filename": 'measurements/stat_groupby_month_sql_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "Influx DB writes - month",
#             "filename": 'measurements/groupby_month_influx_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite States writes - month",
#             "filename": 'measurements/states_groupby_month_sql_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite Statistics writes - month",
#             "filename": 'measurements/stat_groupby_month_sql_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "Influx DB reads - year",
#             "filename": 'measurements/groupby_year_influx_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite States reads - year",
#             "filename": 'measurements/states_groupby_year_sql_log.csv',
#             "column": 4,
#         },
#          {
#             "title of boxplot": "SQLite Statistics reads - year",
#             "filename": 'measurements/stat_groupby_year_sql_log.csv',
#             "column": 4,
#         },     
#         {
#             "title of boxplot": "Influx DB writes - year",
#             "filename": 'measurements/groupby_year_influx_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite States writes - year",
#             "filename": 'measurements/states_groupby_year_sql_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite Statistics writes - year",
#             "filename": 'measurements/stat_groupby_year_sql_log.csv',
#             "column": 5,
#         }
#     ]
# }

graph_AllGroupBy_io = {
    "chart_title": "Group by day/week/month/year - Disk I/O (MiB)",
    "svg_name": "graph_AllGroupBy_io",
    "boxplots": [
        {
            "title of boxplot": "Influx DB reads - day",
            "filename": 'measurements/groupby_day_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads - day",
            "filename": 'measurements/states_groupby_day_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite Statistics reads - day",
            "filename": 'measurements/stat_groupby_day_sql_log.csv',
            "column": 4,
        },
       
        {
            "title of boxplot": "Influx DB reads - week",
            "filename": 'measurements/groupby_week_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads - week",
            "filename": 'measurements/states_groupby_week_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite Statistics reads - week",
            "filename": 'measurements/stat_groupby_week_sql_log.csv',
            "column": 4,
        },
       
        {
            "title of boxplot": "Influx DB reads - month",
            "filename": 'measurements/groupby_month_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads - month",
            "filename": 'measurements/states_groupby_month_sql_log.csv',
            "column": 4,
        },
          {
            "title of boxplot": "SQLite Statistics reads - month",
            "filename": 'measurements/stat_groupby_month_sql_log.csv',
            "column": 4,
        },
        
        {
            "title of boxplot": "Influx DB reads - year",
            "filename": 'measurements/groupby_year_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States reads - year",
            "filename": 'measurements/states_groupby_year_sql_log.csv',
            "column": 4,
        },
         {
            "title of boxplot": "SQLite Statistics reads - year",
            "filename": 'measurements/stat_groupby_year_sql_log.csv',
            "column": 4,
        }     
       
    ]
}

graph_AllGroupBy_realtime = {
    "chart_title": "Group by day/week/month/year - Actual Time (s)",
    "svg_name": "graph_AllGroupBy_realtime",
    "boxplots": [
        {
            "title of boxplot": "Influx DB - day",
            "filename": 'measurements/groupby_day_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale - day",
            "filename": 'measurements/ts_states_groupby_day_sql_log.csv',
            "column": 6,
        },
         {
            "title of boxplot": "SQLite States - day",
            "filename": 'measurements/states_groupby_day_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite Statistics - day",
            "filename": 'measurements/stat_groupby_day_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Influx DB - week",
            "filename": 'measurements/groupby_week_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale - week",
            "filename": 'measurements/ts_states_groupby_week_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite States- week",
            "filename": 'measurements/states_groupby_week_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite Statistics - week",
            "filename": 'measurements/stat_groupby_week_sql_log.csv',
            "column": 6,
        },   
        {
            "title of boxplot": "Influx DB - month",
            "filename": 'measurements/groupby_month_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale - month",
            "filename": 'measurements/ts_states_groupby_month_sql_log.csv',
            "column": 6,
        },
         {
            "title of boxplot": "SQLite States - month",
            "filename": 'measurements/states_groupby_month_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite Statistics - month",
            "filename": 'measurements/stat_groupby_month_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Influx DB - year",
            "filename": 'measurements/groupby_year_influx_log.csv',
            "column": 6,
        },   
        {
            "title of boxplot": "Timescale - year",
            "filename": 'measurements/ts_states_groupby_year_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite States - year",
            "filename": 'measurements/states_groupby_year_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite Statistics - year",
            "filename": 'measurements/stat_groupby_year_sql_log.csv',
            "column": 6,
        }
    ]
}

graph_AllGroupBy_realtimeNoStates = {
    "chart_title": "Group by day/week/month/year - Actual Time (s), no states table",
    "svg_name": "graph_AllGroupBy_realtimeNoStates",
    "boxplots": [
        {
            "title of boxplot": "Influx DB - day",
            "filename": 'measurements/groupby_day_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Influx DB - week",
            "filename": 'measurements/groupby_week_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Influx DB - month",
            "filename": 'measurements/groupby_month_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Influx DB - year",
            "filename": 'measurements/groupby_year_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale - day",
            "filename": 'measurements/ts_states_groupby_day_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale - week",
            "filename": 'measurements/ts_states_groupby_week_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale - month",
            "filename": 'measurements/ts_states_groupby_month_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale",
            "filename": 'measurements/ts_states_groupby_year_sql_log.csv',
            "column": 6,
        },
        
        {
            "title of boxplot": "SQLite Statistics - day",
            "filename": 'measurements/stat_groupby_day_sql_log.csv',
            "column": 6,
        },        
        {
            "title of boxplot": "SQLite Statistics - week",
            "filename": 'measurements/stat_groupby_week_sql_log.csv',
            "column": 6,
        },    
        
        {
            "title of boxplot": "SQLite Statistics - month",
            "filename": 'measurements/stat_groupby_month_sql_log.csv',
            "column": 6,
        },
    
        {
            "title of boxplot": "SQLite Statistics - year",
            "filename": 'measurements/stat_groupby_year_sql_log.csv',
            "column": 6,
        }
    ]
}

graph_l2_min_mon_sum_CPU = {
    "chart_title": "2 days / min/max / mon/sun / sum 3 phases - CPU Time (s)",
    "svg_name": "graph_l2_min_mon_sum_CPU",
    "boxplots": [
        {
            "title of boxplot": "Influx DB - 2 days",
            "filename": 'measurements/last2days_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale - 2 days",
            "filename": 'measurements/ts_states_last2days_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States - 2 days",
            "filename": 'measurements/states_last2days_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics - 2 days",
            "filename": 'measurements/stat_last2days_sql_log.csv',
            "column": 2,
        }, 
        {
            "title of boxplot": "Influx DB - min/max",
            "filename": 'measurements/min_max_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale - min/max",
            "filename": 'measurements/ts_states_min_max_phase1_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
         {
            "title of boxplot": "SQLite States- min/max",
            "filename": 'measurements/states_min_max_phase1_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics - min/max",
            "filename": 'measurements/stat_min_max_phase1_sql_log.csv',
            "column": 2,
        },  
        {
            "title of boxplot": "Influx DB - mon/sun",
            "filename": 'measurements/groupby_sun_mon_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale - mon/sun",
            "filename": 'measurements/ts_states_mon_sun_phase1_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
         {
            "title of boxplot": "SQLite States - mon/sun",
            "filename": 'measurements/states_mon_sun_phase1_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics - mon/sun",
            "filename": 'measurements/stat_mon_sun_phase1_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Influx DB - sum 3 phases",
            "filename": 'measurements/sum_phases_using_pivot_01_influx_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "Timescale - sum 3 phases",
            "filename": 'measurements/ts_states_sum_phase1_3_sql_log.csv',
            "column": 2,
            "factor": 0.0000001,
        },
        {
            "title of boxplot": "SQLite States - sum 3 phases",
            "filename": 'measurements/states_sum_phase1_3_sql_log.csv',
            "column": 2,
        },
        {
            "title of boxplot": "SQLite Statistics - sum 3 phases",
            "filename": 'measurements/stat_sum_phase1_3_sql_log.csv',
            "column": 2,
        }
    ]
}

graph_l2_min_mon_sum_memory = {
    "chart_title": "2 days / min/max / mon/sun / sum 3 phases - Memory HWM (MiB)",
    "svg_name": "graph_l2_min_mon_sum_memory",
    "boxplots": [
        {
            "title of boxplot": "Influx DB - 2 days",
            "filename": 'measurements/last2days_influx_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Timescale - 2 days",
            "filename": 'measurements/ts_states_last2days_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite States - 2 days",
            "filename": 'measurements/states_last2days_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics - 2 days",
            "filename": 'measurements/stat_last2days_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Influx DB - min/max",
            "filename": 'measurements/min_max_influx_log.csv',
            "column": 3,
        },
         {
            "title of boxplot": "Timescale - min/max",
            "filename": 'measurements/ts_states_min_max_phase1_sql_log.csv',
            "column": 3,
        },
         {
            "title of boxplot": "SQLite States- min/max",
            "filename": 'measurements/states_min_max_phase1_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics - min/max",
            "filename": 'measurements/stat_min_max_phase1_sql_log.csv',
            "column": 3,
        },    
        {
            "title of boxplot": "Influx DB - mon/sun",
            "filename": 'measurements/groupby_sun_mon_influx_log.csv',
            "column": 3,
        },
         {
            "title of boxplot": "Timescale - mon/sun",
            "filename": 'measurements/ts_states_mon_sun_phase1_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite States - mon/sun",
            "filename": 'measurements/states_mon_sun_phase1_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics - mon/sun",
            "filename": 'measurements/stat_mon_sun_phase1_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "Influx DB - sum 3 phases",
            "filename": 'measurements/sum_phases_using_pivot_01_influx_log.csv',
            "column": 3,
        },
       
       
        {
            "title of boxplot": "Timescale - sum 3 phases",
            "filename": 'measurements/ts_states_sum_phase1_3_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite States - sum 3 phases",
            "filename": 'measurements/states_sum_phase1_3_sql_log.csv',
            "column": 3,
        },
        {
            "title of boxplot": "SQLite Statistics - sum 3 phases",
            "filename": 'measurements/stat_sum_phase1_3_sql_log.csv',
            "column": 3,
        }
    ]
}

graph_l2_min_mon_sum_realtime = {
    "chart_title": "2 days / min/max / mon/sun / sum 3 phases - realtime (s)",
    "svg_name": "graph_l2_min_mon_sum_realtime",
    "boxplots": [
        {
            "title of boxplot": "Influx DB - 2 days",
            "filename": 'measurements/last2days_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale - 2 days",
            "filename": 'measurements/ts_states_last2days_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite States - 2 days",
            "filename": 'measurements/states_last2days_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite Statistics - 2 days",
            "filename": 'measurements/stat_last2days_sql_log.csv',
            "column": 6,
        }, 

        {
            "title of boxplot": "Influx DB - min/max",
            "filename": 'measurements/min_max_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale - min/max",
            "filename": 'measurements/ts_states_min_max_phase1_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite States- min/max",
            "filename": 'measurements/states_min_max_phase1_sql_log.csv',
            "column": 6,
        },
         {
            "title of boxplot": "SQLite Statistics - min/max",
            "filename": 'measurements/stat_min_max_phase1_sql_log.csv',
            "column": 6,
        },  
        {
            "title of boxplot": "Influx DB - mon/sun",
            "filename": 'measurements/groupby_sun_mon_influx_log.csv',
            "column": 6,
        },
         {
            "title of boxplot": "Timescale - mon/sun",
            "filename": 'measurements/ts_states_mon_sun_phase1_sql_log.csv',
            "column": 6,
        },{
            "title of boxplot": "SQLite States - mon/sun",
            "filename": 'measurements/states_mon_sun_phase1_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite Statistics - mon/sun",
            "filename": 'measurements/stat_mon_sun_phase1_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Influx DB - sum 3 phases",
            "filename": 'measurements/sum_phases_using_pivot_01_influx_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "Timescale - sum 3 phases",
            "filename": 'measurements/ts_states_sum_phase1_3_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite States - sum 3 phases",
            "filename": 'measurements/states_sum_phase1_3_sql_log.csv',
            "column": 6,
        },
        {
            "title of boxplot": "SQLite Statistics - sum 3 phases",
            "filename": 'measurements/stat_sum_phase1_3_sql_log.csv',
            "column": 6,
        }
    ]
}

# graph_l2_min_mon_sum_IO = {
#     "chart_title": "2 days / min/max / mon/sun / sum 3 phases - Disk I/O (MiB)",
#     "svg_name": "graph_l2_min_mon_sum_IO",
#     "boxplots": [
#         {
#             "title of boxplot": "SQLite Statistics - 2 days - reads",
#             "filename": 'measurements/stat_last2days_sql_log.csv',
#             "column": 4,
#         }, 
#         {
#             "title of boxplot": "Influx DB - 2 days - reads",
#             "filename": 'measurements/last2days_influx_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite States - 2 days - reads",
#             "filename": 'measurements/states_last2days_sql_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite Statistics - 2 days - writes",
#             "filename": 'measurements/stat_last2days_sql_log.csv',
#             "column": 5,
#         },  
#         {
#             "title of boxplot": "Influx DB - 2 days - writes",
#             "filename": 'measurements/last2days_influx_log.csv',
#             "column": 5,
#         },
#          {
#             "title of boxplot": "SQLite States - 2 days - writes",
#             "filename": 'measurements/states_last2days_sql_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite Statistics - min/max - reads",
#             "filename": 'measurements/stat_min_max_phase1_sql_log.csv',
#             "column": 4,
#         },   
#         {
#             "title of boxplot": "Influx DB - min/max - reads",
#             "filename": 'measurements/min_max_influx_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite States- min/max - reads",
#             "filename": 'measurements/states_min_max_phase1_sql_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite Statistics - min/max - writes",
#             "filename": 'measurements/stat_min_max_phase1_sql_log.csv',
#             "column": 5,
#         },  
#         {
#             "title of boxplot": "Influx DB - min/max - writes",
#             "filename": 'measurements/min_max_influx_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite States- min/max - writes",
#             "filename": 'measurements/states_min_max_phase1_sql_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite Statistics - mon/sun - reads",
#             "filename": 'measurements/stat_mon_sun_phase1_sql_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "Influx DB - mon/sun - reads",
#             "filename": 'measurements/groupby_sun_mon_influx_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite States - mon/sun - reads",
#             "filename": 'measurements/states_mon_sun_phase1_sql_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite Statistics - mon/sun writes",
#             "filename": 'measurements/stat_mon_sun_phase1_sql_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "Influx DB - mon/sun - writes",
#             "filename": 'measurements/groupby_sun_mon_influx_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite States - mon/sun - writes",
#             "filename": 'measurements/states_mon_sun_phase1_sql_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite Statistics - sum 3 phases - reads",
#             "filename": 'measurements/stat_sum_phase1_3_sql_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "Influx DB - sum 3 phases - reads",
#             "filename": 'measurements/sum_phases_using_pivot_01_influx_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite States - sum 3 phases - reads",
#             "filename": 'measurements/states_sum_phase1_3_sql_log.csv',
#             "column": 4,
#         },
#         {
#             "title of boxplot": "SQLite Statistics - sum 3 phases - writes",
#             "filename": 'measurements/stat_sum_phase1_3_sql_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "Influx DB - sum 3 phases - writes",
#             "filename": 'measurements/sum_phases_using_pivot_01_influx_log.csv',
#             "column": 5,
#         },
#         {
#             "title of boxplot": "SQLite States - sum 3 phases - writes",
#             "filename": 'measurements/states_sum_phase1_3_sql_log.csv',
#             "column": 5,
#         }
#     ]
# }

graph_l2_min_mon_sum_IO = {
    "chart_title": "2 days / min/max / mon/sun / sum 3 phases - Disk I/O (MiB)",
    "svg_name": "graph_l2_min_mon_sum_IO",
    "boxplots": [
        {
            "title of boxplot": "SQLite Statistics - 2 days - reads",
            "filename": 'measurements/stat_last2days_sql_log.csv',
            "column": 4,
        }, 
        {
            "title of boxplot": "Influx DB - 2 days - reads",
            "filename": 'measurements/last2days_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States - 2 days - reads",
            "filename": 'measurements/states_last2days_sql_log.csv',
            "column": 4,
        },
        
        {
            "title of boxplot": "SQLite Statistics - min/max - reads",
            "filename": 'measurements/stat_min_max_phase1_sql_log.csv',
            "column": 4,
        },   
        {
            "title of boxplot": "Influx DB - min/max - reads",
            "filename": 'measurements/min_max_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States- min/max - reads",
            "filename": 'measurements/states_min_max_phase1_sql_log.csv',
            "column": 4,
        },
        
        {
            "title of boxplot": "SQLite Statistics - mon/sun - reads",
            "filename": 'measurements/stat_mon_sun_phase1_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "Influx DB - mon/sun - reads",
            "filename": 'measurements/groupby_sun_mon_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States - mon/sun - reads",
            "filename": 'measurements/states_mon_sun_phase1_sql_log.csv',
            "column": 4,
        },
        
        {
            "title of boxplot": "SQLite Statistics - sum 3 phases - reads",
            "filename": 'measurements/stat_sum_phase1_3_sql_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "Influx DB - sum 3 phases - reads",
            "filename": 'measurements/sum_phases_using_pivot_01_influx_log.csv',
            "column": 4,
        },
        {
            "title of boxplot": "SQLite States - sum 3 phases - reads",
            "filename": 'measurements/states_sum_phase1_3_sql_log.csv',
            "column": 4,
        }
        
    ]
}