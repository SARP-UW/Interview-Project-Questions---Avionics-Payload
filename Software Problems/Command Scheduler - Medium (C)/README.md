# Command Scheduler — Medium

Simulate a cooperative scheduler where each scheduler tick represents a 20 ms execution window. At the start of tick `t`, release a new instance of each task whose `t % period == 0`. The tick at which an instance is released is its `release_tick`. Task `period` and `deadline` values are measured in scheduler ticks, while `runtime` is measured in milliseconds.

Each tick has a total execution budget of 20 ms. When a task instance runs, subtract its `runtime` from the remaining budget for that tick. For example, tasks with runtimes of 7 ms and 8 ms can both execute in the same tick, consuming 15 ms and leaving 5 ms of budget.

Each released task instance has an absolute deadline of `release_tick + deadline`. Among all released or pending task instances, run them in order of increasing absolute deadline, breaking ties by their original task array order. A task instance may run only if its entire runtime fits within the remaining budget for the current tick; tasks may not be partially executed across ticks. Each task may run at most once per tick. If an instance does not fit, leave it pending for a later tick. A pending instance is considered missed if it has not completed by its absolute deadline tick.

Reject invalid tasks where `period == 0`, `deadline == 0`, or `runtime > 20`. Use no dynamic allocation. Record task executions and deadline misses using the callbacks provided in `starter.c`.

Test the scheduler over 8 ticks using tasks such as `radio (period 2, runtime 8 ms, deadline 2 ticks)`, `imu (period 1, runtime 7 ms, deadline 1 tick)`, and `logger (period 4, runtime 10 ms, deadline 2 ticks)`. Your tests should verify execution order and include at least one deadline miss.
