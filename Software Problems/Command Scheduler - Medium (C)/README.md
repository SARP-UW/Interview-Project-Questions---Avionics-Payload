# Command Scheduler — Medium

Simulate a cooperative scheduler for a 20 ms loop. Tick `t` runs tasks where
`t % period == 0`; runtime consumes that tick's budget. Run due tasks by
increasing deadline, then original array order. If a task does not fit, leave
it pending and report a miss if it cannot finish by `release + deadline`.
Each task runs at most once per tick. Reject period 0, runtime > 20, or
deadline < runtime. Use no dynamic allocation and record runs/misses through
the callbacks in `starter.c`. Test execution order and a missed task using the
Start with tasks such as `radio (period 2, runtime 8, deadline 2)`, `imu
(period 1, runtime 7, deadline 1)`, and `logger (period 4, runtime 10,
deadline 2)` over 8 ticks; test execution order and at least one missed task.
