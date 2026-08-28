#include <stddef.h>

typedef struct { const char *name; unsigned period, runtime, deadline; } Task;
typedef void (*TaskCallback)(const char *name, unsigned tick);

void schedule(const Task *tasks, size_t count, unsigned ticks,
              TaskCallback on_run, TaskCallback on_miss) {
    /* TODO: implement the 20 ms tick simulation described in the README. */
    (void)tasks; (void)count; (void)ticks; (void)on_run; (void)on_miss;
}
int main(void) { return 0; }
