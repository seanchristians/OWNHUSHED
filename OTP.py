import time, hmac, hashlib, base64

class default:
	T0 = 0
	TX = 30
	N = 6
	digest = hashlib.sha1

def base32decode(K):
	K = K.replace(' ','')
	if len(K) % 8 != 0:
		K += '='*(8 - (len(K)%8))
	return base64.b32decode(K, casefold=True)

def int_to_bytearray(i):
	b = bytearray(8)
	for n in range(7,-1,-1):
		b[n] = i & 0xff
		i >>= 8
	return b

def counter(T0=default.T0, TX=default.TX):
	T = int(time.time())
	return int((T-T0)/TX)

def HOTP(K, C, *, N=default.N, hash=default.digest):
	K = base32decode(K)
	C = int_to_bytearray(C)
	mac = hmac.new(K, C, hash)
	mac = bytearray(mac.digest())
	i = mac[-1] & 0xf
	trunc = (
		(mac[i] & 0x7f) << 24 |
		mac[i + 1] << 16 |
		mac[i + 2] << 8 |
		mac[i + 3]
	)
	code = str(trunc % (10**N))
	code += '0'*(6-len(code))
	return code

def TOTP(K, *, N=default.N, hash=default.digest):
	C = counter()
	return HOTP(K, C, N=N)