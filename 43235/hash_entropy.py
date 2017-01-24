import hashlib
import random
import itertools
import math

inputNibbles = 6
inputSource = random.getrandbits(inputNibbles*4)
h = hashlib.sha512(str(inputSource).encode('ascii'))

target = h.hexdigest()[:inputNibbles]

print('Input entropy: ' + str(inputSource))
print('SHA512(input_entropy)[:{:}]: '.format(inputNibbles) + target)

inputLUT = map(list, itertools.product("01", repeat=inputNibbles*4))
inputLUT = [str(int(''.join(inputVal),2)).encode('ascii') for inputVal in inputLUT]
print('Input LUT generated.')

outputLUT = [hashlib.sha512(preimage).hexdigest()[:inputNibbles] for preimage in inputLUT]
print('Output LUT generated.')

for k in range(1, (inputNibbles)+1):

	countPreimages = 0
	for output in outputLUT:
		# Find how many preimages there are 
		if output[:k] == target[:k]:
			countPreimages += 1 

	print(str(target[:k]) + ': ' + str(countPreimages) + ' ~ 2^' +str(math.log(countPreimages)/math.log(2)))

