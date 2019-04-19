FNV_32_PRIME = 0x01000193
FNV1_32_INIT = 0x811c9dc5

def fnv1a_32(data):
	hval = FNV1_32_INIT
	for byte in data:
		hval = hval ^ byte
		hval = (hval * FNV_32_PRIME) % 2**32
	return hval
