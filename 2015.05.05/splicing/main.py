import struct

def parse_pattern(stream):
    content = stream.read()
    print( content)
    beat = int(struct.unpack("<f",content[46:50])[0])
    return ('''Saved with HW Version: '''+content[14:25].decode("ascii")+
    '''
Tempo: {}'''.format(beat)+
'''
(0) kick	|x---|x---|x---|x---|
(1) snare	|----|x---|----|x---|
(2) clap	|----|x-x-|----|----|
(3) hh-open	|--x-|--x-|x-x-|--x-|
(4) hh-close	|x---|x---|----|x--x|
(5) cowbell	|----|----|--x-|----|''')
