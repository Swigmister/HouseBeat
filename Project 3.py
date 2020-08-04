#		Comments Section
#       python code
#		script_name: Earsketch Project
#
#		author: Parth Desai
#		description: House Beat
#

from earsketch import *

#SetUp Section
init()
setTempo(128)

#Music Section
#Instruments for Section 1
beat2 = ELECTRO_DRUM_MAIN_BEAT_005
bass1 = ELECTRO_ANALOGUE_BASS_011
bass3 = ELECTRO_ANALOGUE_BASS_001
vocal1 = HIPHOP_VOCALHIT_002
piano1 = HOUSE_ACOUSTIC_PIANO_004
transition = YG_FUNK_CYMBALS_3
edm1 = YG_EDM_PAD_3


#Instruments for Section 2
bass2 = RD_UK_HOUSE__FMBASS_1
beat1 = RD_EDM_DRUMBEATPART_3
drum1 = RD_ELECTRO_DRUM_PART_13
synth1 = YG_EDM_SYNTH_LEAD_2
epiano1 = YG_ELECTRO_ELECTRIC_PIANO_1
lead1 = YG_ELECTRO_LEAD_1


#Execution of Media Section 1
fitMedia(vocal1, 4, 5, 9)
fitMedia(bass3, 1, 1, 9)
fitMedia(beat2, 2, 1, 9)
fitMedia(piano1, 5, 5, 9)
fitMedia(bass3, 3, 9, 13)
fitMedia(beat2, 6, 9, 13)
fitMedia(bass1, 7, 13, 17)
fitMedia(edm1, 8, 13, 17)
fitMedia(beat2, 9, 13, 17)


#Effects Section1
setEffect(1, VOLUME, GAIN, -60, 1, 0, 5)
setEffect(2, VOLUME, GAIN, -60, 1, 0, 5)
setEffect(1, VOLUME, GAIN, -60, 1, 0, 5)
setEffect(3, PAN, LEFT_RIGHT, -100, 9, 100, 13)
setEffect(6, PAN, LEFT_RIGHT, -100, 9, 100, 13)
setEffect(7, PITCHSHIFT, PITCHSHIFT_SHIFT, 4.0, 5, 4.0, 9)
setEffect(4, DELAY, DELAY_TIME, 500.0, 5, 500.0, 9)
setEffect(10, DELAY, DELAY_TIME, 500.0, 17, 300.0, 19)
setEffect(5, VOLUME, GAIN, 5, 5, 5, 9)
setEffect(7, VOLUME, GAIN, 0, 13, -60, 17)
setEffect(8, VOLUME, GAIN, 0, 13, -60, 17)
setEffect(9, VOLUME, GAIN, 0, 13, -60, 17)


#Transition
fitMedia(transition, 10, 17, 19)


#Execution of Media Section2
#For-loop to create beat
for measure in range(19, 39):
  fitMedia(beat1, 11, measure, measure + 1)
  fitMedia(drum1, 12, measure, measure + 1)

#Distortion effect for-loop
for track in range(11, 13):
  for measure in range(19, 23):
    setEffect(track, DISTORTION, DISTO_GAIN, 25.0, measure, 0, measure + 1)
  track += 1

fitMedia(bass2, 13, 23, 27)
fitMedia(synth1, 14, 27, 39)
fitMedia(epiano1, 15, 31, 39)
fitMedia(lead1, 16, 35, 39)
setEffect(11, VOLUME, GAIN, 0, 23, -60, 39)
setEffect(12, VOLUME, GAIN, 0, 23, -60, 39)
setEffect(14, VOLUME, GAIN, 0, 35, -60, 39)
setEffect(15, VOLUME, GAIN, 0, 35, -60, 39)
setEffect(16, VOLUME, GAIN, 0, 35, -60, 39)


#Finish
finish()
