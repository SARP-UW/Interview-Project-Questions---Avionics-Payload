# Packet Checksum — Easy

Implement `validate_packet` in `starter.c`. Packets contain a two-byte big-
endian payload length, a payload (of variable length), and a one-byte checksum equal to the XOR of
all payload bytes. Reject truncated packets, impossible lengths, and bad
checksums without reading past the buffer. Add at least four tests.

### Hints
* How could you figure out the bounds on the payload length?
* Be careful with big-endian and little-endian (look up what these mean, what does your machine use?)
* Think about how you can manipulate the pointer to get access to the data you need.
