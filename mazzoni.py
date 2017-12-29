#!/usr/bin/env python
"""
http://www.pnas.org/content/88/10/4433.full.pdf
"""

import numpy as np
from event_emitter import EventEmitter
import networkx as nx
import itertools

DG = nx.DiGraph()
node_ids = itertools.count()
input_neurons = []

for i in range(4):
    input_neurons.append(node_ids.next())

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
