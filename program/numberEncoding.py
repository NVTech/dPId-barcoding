# Original Author Michael van der Kolff         
# Copyright (c) 2010-2012 dPId Pty. Ltd.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import string

encodingStuff = string.digits.replace('0','') + string.ascii_uppercase.replace('I','').replace('O','').replace('Z','')

def reverseOrderIter(sequence):
	"""reverse an iterator implementing __len__"""
	i = len(sequence) - 1
	while i >=0:
		yield sequence[i]
		i -= 1

def encodeIntAsStr(numberToEncode,radix=10, mapToEncodeBy=None, zeroFillChars=1):
	"""This function encodes an integer to a string using a string supplied as the map to encode by.  If the radix is less than the length of the map to encode by, the map is truncated"""
	sign = ''
	result = ''
	if mapToEncodeBy is None:
		mapToEncodeBy=encodingStuff
	if not (2 <= radix <= len(mapToEncodeBy)):
		raise ValueError, "radix must be between 2 and the length of the map to encode by, which is %d" % len(mapToEncodeBy)
	if numberToEncode < 0:
		sign = '-'
		numberToEncode = -numberToEncode
	while True:
		numberToEncode, digitToPull = divmod(numberToEncode, radix)
		result = mapToEncodeBy[digitToPull] + result
		if (numberToEncode == 0):
			return sign + result.rjust(zeroFillChars,mapToEncodeBy[0])

def decodeStrToInt(strToDecode,radix=10,mapToDecodeBy=None):
	"""This function decodes a string into an integer using a string supplied as the map to decode by.  If the radix is less than the length of the map to decode by, the map is truncated"""
	if mapToDecodeBy is None:
		mapToDecodeBy=encodingStuff
	if not (2 <= radix <= len(mapToDecodeBy)):
		raise ValueError, "radix must be between 2 and the length of the map to encode by, which is %d" % len(mapToEncodeBy)
	reverseMap = dict(zip(mapToDecodeBy,range(0,radix))) # Create a map from each of the characters to each of the numbers they represent
	result = 0
	signBit = (strToDecode[0] == '-')
	if signBit:
		strToDecode = strToDecode[1:]
	try:
		effectiveMultiplier = 1
		for currChar in reverseOrderIter(strToDecode):
			result += reverseMap[currChar] * effectiveMultiplier
			effectiveMultiplier *= radix
		if signBit:
			return -result
		else:
			return result
	except KeyError, e:
		raise ValueError, "character in input string outside of expected values: %s" % e.args[0]
