# Telemetry Packet Decoder — Medium

Implement `decode_packet` for: `AA 55 | type | sequence (big-endian uint16) |
length (uint8) | payload | checksum`. Length is 0–8. Checksum is the XOR of
every byte from `type` through the final payload byte; total size is `7 +
length`. Return 1 only for an exact-size, valid packet and leave output
unchanged on failure. Test valid, truncated, trailing-byte, bad-sync,
bad-length, bad-checksum, empty, and maximum-payload packets.
