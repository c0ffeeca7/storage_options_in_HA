// https://docs.influxdata.com/flux/v0.x/spec/types/#duration-types

from(bucket: "energy-data-test-05")
  |> range(start: 2020-11-14T00:00:00Z, stop: 2021-11-14T12:00:00Z)
  |> filter(fn: (r) => r["_measurement"] == "Wh")
  |> filter(fn: (r) => r["_field"] == "value")
  |> filter(fn: (r) => r["domain"] == "sensor")
  |> filter(fn: (r) => r["entity_id"] == "phase1")
  |> aggregateWindow(every: 1mo, fn: sum, createEmpty: false)
  |> yield(name: "sum")
