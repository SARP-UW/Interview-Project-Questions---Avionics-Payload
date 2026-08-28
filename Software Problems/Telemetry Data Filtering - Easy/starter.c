#include <stddef.h>
typedef struct { size_t count; int minimum; int maximum; double mean; } Summary;

int summarize_samples(const int *input, size_t count, int *output,
                      size_t capacity, Summary *summary) {
    /* TODO: implement the one-pass filter and summary. */
    (void)input; (void)count; (void)output; (void)capacity; (void)summary;
    return 0;
}

int main(void) { return 0; }
