# Sensor Window Statistics — Easy

Complete `summarize_samples`. Given signed integer sensor readings, copy only
values in `[0, 1000]` into the output array and calculate count, minimum,
maximum, and arithmetic mean. Return `0` for empty or all-invalid input. Do
not sort or dynamically allocate memory; preserve input order.

For example, `{42, -3, 1001, 17, 0, 999}` produces `{42, 17, 0, 999}`,
minimum `0`, maximum `999`, and mean `264.5`.

Add tests for empty input, all-invalid input, one valid value, and both
boundaries. The intended solution is one pass through the input.

Compile with `cc -std=c11 -Wall -Wextra -Wpedantic starter.c -o starter`.
