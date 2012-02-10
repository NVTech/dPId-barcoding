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

with open('dPIdTagTemplateProlog.ps') as tagTemplateProlog:
	print tagTemplateProlog.read()

with open('dPIdTagTemplate.ps') as tagTemplate:
	print tagTemplate.read()

print r"""/pageParameters <<
  /pageXSize 210 mm
  /pageYSize 297 mm

  /pageLeftMargin 5 mm
  /pageRightMargin 5 mm
  /pageTopMargin 5 mm
  /pageBottomMargin 5 mm % Start drawing at the bottom

  /interspacingX 0 mm
  /interspacingY 0 mm
>> def

/tagParameters <<
  /externalSizeX 15 mm
  /externalSizeY 30 mm

  /barcodeSize 10 mm

  /topBorderSize 2.5 mm
  /bottomBorderSize 3 mm

  /borderLineWidth 1

  /circleFillFactor 0
  /circleSize 5.5 mm
  /circleOffset 4.75 mm      % From bottom of tag

  /tagTextFont /ocrb10 findfont 13 scalefont

>> def

/realTags ["""

for line in csv.reader(sys.stdin):
	if len(line) > 1:
		print "  <</tagBarcode (%s) /tagText (%s)>>" % (line[0],line[1])
	else:
		print "  <</tagBarcode (%s) /tagText ()>>" % line[0]

print """] def

/tags realTags def    % Duplicate every item, then package it in the array

pageParameters tagParameters tagFullSize {tagParameters exch drawTag} tags drawItems"""
