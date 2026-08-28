#include <stddef.h>
#include <stdint.h>

int validate_packet(const uint8_t *packet, size_t packet_size) {
    /* TODO: parse the length safely, bounds-check, then verify XOR checksum. */
    (void)packet; (void)packet_size;
    return 0;
}

int main(void) { return 0; }
