#!/usr/bin/python
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

import numberEncoding, sys

i=0
for line in sys.stdin:
	print "%s,C-%s" % (line[:-1],numberEncoding.encodeIntAsStr(i,radix=32).rjust(5,'-'))
	i+=1
