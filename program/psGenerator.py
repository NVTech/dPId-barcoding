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

import sys, csv

with open('ps/dPIdTagTemplateProlog.ps') as tagTemplateProlog:
	print tagTemplateProlog.read()

with open('ps/dPIdTagTemplate.ps') as tagTemplate:
	print tagTemplate.read()

print r"""/pageParameters <<
  /pageXSize 210 mm
  /pageYSize 297 mm

  /pageLeftMargin 7.5 mm
  /pageRightMargin 7.0 mm
  /pageTopMargin 9.5 mm
  /pageBottomMargin 26 mm % Start drawing at the bottom

  /interspacingX 3 mm
  /interspacingY 3 mm
>> def

/tagParameters <<
  /externalSizeX 30 mm
  /externalSizeY 30 mm

  /barcodeSize 15 mm

  /topBorderSize 4 mm
  /bottomBorderSize 3 mm

  /borderLineWidth 0

  /circleFillFactor 0
  /circleSize 0 mm
  /circleOffset 3 mm      % From bottom of tag

  /tagTextFont /ocrb10 findfont 13 scalefont

>> def

/realTags ["""

for line in csv.reader(sys.stdin):
	print "  <</tagBarcode (%s) /tagText (%s)>>" % (line[0],line[1])

print """] def

/tags [ realTags {dup} forall ] def    % Duplicate every item, then package it in the array

pageParameters tagParameters tagFullSize {tagParameters exch drawTag} tags drawItems"""
