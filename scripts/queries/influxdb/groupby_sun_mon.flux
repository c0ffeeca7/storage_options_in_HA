// shows sum per day of phase1, for sundays and mondays.
// https://docs.influxdata.com/flux/v0.x/stdlib/date/weekday/

//influx query
import "date"
from(bucket: "energy-data-test-05")
  |> range(start: 2020-11-14T00:00:00Z, stop: 2021-11-14T12:00:00Z)   
  |> filter(fn: (r) => r["_measurement"] == "Wh")
  |> filter(fn: (r) => r["_field"] == "value")
  |> filter(fn: (r) => r["domain"] == "sensor")
  |> filter(fn: (r) => r["entity_id"] == "phase1")  
  |> aggregateWindow(every: 1d, fn: sum, createEmpty: false)  
  |> filter(fn: (r) => ((date.weekDay(t: r["_time"]) == 0) or (date.weekDay(t: r["_time"]) == 1)))
  |> map(fn: (r) => ({r with weekday:  date.weekDay(t: r._time)}) )
  |> yield(name: "sum")
