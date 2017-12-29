#!/usr/bin/env python
"""
http://www.pnas.org/content/88/10/4433.full.pdf
"""

import numpy as np
from event_emitter import EventEmitter

class Synapse(EventEmitter):
  def __init__(self, input_neuron, output_neuron, weight=None):
    super()
    self.input_neuron = input_neuron
    self.output_neuron = output_neuron
    self.weight = weight if weight is not None else np.random.random()

class Neuron(EventEmitter): pass

class Context(object):
  input_neurons = None
  output_neurons = None
  synapses = None

  _incoming_synapses = None
  _outgoing_synapses = None

  event_callbacks = None

  def __init__(self):
    self.input_neurons = []
    self.output_neurons = []
    self.synapses = []
    self._incoming_synapses = {}
    self._outgoing_synapses = {}
    self.event_callbacks = {}

  def connect(self, sending_neuron, target_neuron, weight=None):
    s = Synapse(sending_neuron, target_neuron, weight)
    self.synapses.append(s)

    self._incoming_synapses.setdefault(target_neuron, [])
    self._incoming_synapses[target_neuron].append(s)

    self._outgoing_synapses.setdefault(sending_neuron, [])
    self._outgoing_synapses[sending_neuron].append(s)





ctx = Context()
for i in xrange(4):
  n = Neuron()
  ctx.input_neurons.append(n)

layers = [ctx.input_neurons]
for layer_i in xrange(2):
  current_layer = []
  for i in xrange(4):
    n = Neuron()
    current_layer.append(n)
    for ni in layers[-1]: ctx.connect(ni,n)

  layers.append(current_layer)

ctx.output_neurons = []
for i in xrange(4):
  n = Neuron()
  ctx.output_neurons.append(n)
  for ni in layers[-1]: ctx.connect(ni,n)
layers.append(ctx.output_neurons)


# initialize event queue
input_pattern = [1,0,1,0]

# input neurons send spikes
# synapses receive events, multiply weight, send event to receiving neuron
# reset of counters on time step
# receiving neurons receive events, increase counter by value
# on time step (after increase events): apply activation function and send output spike probabilistically

# time step:
#   with probability activation_function(counter): send spike to connected synapses
#   reset counter (must be done before spikes come in!
# spike comes in on synapse:
#   increase counter of connected neuron by weight

"""
T: start, delay

    T1  T2
I - S - N
I - S - N
I - S - N
I - S - N
"""
