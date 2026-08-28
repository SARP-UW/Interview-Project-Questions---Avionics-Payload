#include <stddef.h>
#include <stdint.h>
#define MAX_PAYLOAD 8u
typedef struct { uint8_t type; uint16_t sequence; uint8_t length; uint8_t payload[MAX_PAYLOAD]; } Packet;
int decode_packet(const uint8_t *bytes, size_t size, Packet *packet) {
    /* TODO: validate exact size, parse big-endian fields, and verify checksum. */
    (void)bytes; (void)size; (void)packet; return 0;
}
int main(void) { return 0; }
