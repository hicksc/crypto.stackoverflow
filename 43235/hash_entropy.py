import hashlib
import random
import itertools

inputBytes = 8
inputSource = random.getrandbits(inputBytes*8)
h = hashlib.sha512(str(inputSource).encode('ascii'))

target = h.hexdigest()[:inputBytes]

print('Input entropy: ' + str(inputSource))
print('SHA512(input_entropy)[:{:}]: '.format(inputBytes) + target)

inputLUT = map(list, itertools.product("01", repeat=inputBytes*8))
#["".join(seq) for seq in itertools.product("01", repeat=inputBytes*8)]
inputLUT = [str(int(''.join(inputVal),2)).encode('ascii') for inputVal in inputLUT]
print('Input LUT generated.')

outputLUT = [hashlib.sha512(preimage).hexdigest()[:inputBytes] for preimage in inputLUT]
print('Output LUT generated.')

for k in range(1, inputBytes+1):

	countPreimages = 0
	for output in outputLUT:
		# Find how many preimages there are 
		if output[:k] == target[:k]:
			countPreimages += 1 

	print(str(target[:k]) + ': ' + str(countPreimages))

