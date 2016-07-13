from __future__ import print_function
from __future__ import absolute_import

import sys
import time

from .. import chord

if sys.version_info[0] > 2:
    xrange = range

def protocol_rejection_validation(iters, start_port, encryption, k=4, name='test'):
    for i in xrange(iters):
        print("----------------------Test start----------------------")
        f = chord.chord_socket('localhost', start_port + i*2, k=4, prot=chord.protocol('test', encryption), debug_level=5)
        g = chord.chord_socket('localhost', start_port + i*2 + 1, k=k, prot=chord.protocol(name, encryption), debug_level=5)
        print("----------------------Test event----------------------")
        g.connect('localhost', start_port + i*2)
        time.sleep(1)
        print("----------------------Test ended----------------------")
        assert len(f.routing_table) == len(f.awaiting_ids) == len(g.routing_table) == len(g.awaiting_ids) == 0
        print(f.status)
        print(g.status)
        del f, g

def test_protocol_rejection_Plaintext(iters=3):
    protocol_rejection_validation(iters, 6000, 'Plaintext', name='test2')

def test_protocol_rejection_SSL(iters=3):
    protocol_rejection_validation(iters, 6100, 'SSL', name='test2')

def test_size_rejection_Plaintext(iters=3):
    protocol_rejection_validation(iters, 6200, 'Plaintext', k=5)

def test_size_rejection_SSL(iters=3):
    protocol_rejection_validation(iters, 6300, 'SSL', k=3)