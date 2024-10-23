# Copyright 2018 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

r"""
A :term:`sampler` accepts a problem in :term:`quadratic model` (e.g., BQM, CQM) or
:term:`nonlinear model` format and returns variable assignments.
Samplers generally try to find minimizing values but can also sample from
distributions defined by the problem.

These samplers use a quantum computer, either directly or as part of a
:term:`hybrid` algorithm. 

Sampler are are non-blocking. For quadratic models, returned
:class:`~dimod.SampleSet`\ s are constructed from a
:class:`~concurrent.futures.Future`-like object that is resolved on the first
read of any of its properties; for example, by printing the results. Your code
can query its status with the :meth:`~dimod.SampleSet.done` method or ensure
resolution with the :meth:`~dimod.SampleSet.resolve` method.
"""

from dwave.system.samplers.clique import *
from dwave.system.samplers.dwave_sampler import *
from dwave.system.samplers.leap_hybrid_sampler import *
