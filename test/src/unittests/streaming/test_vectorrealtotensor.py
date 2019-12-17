#!/usr/bin/env python

# Copyright (C) 2006-2016  Music Technology Group - Universitat Pompeu Fabra
#
# This file is part of Essentia
#
# Essentia is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation (FSF), either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the Affero GNU General Public License
# version 3 along with this program. If not, see http://www.gnu.org/licenses/


from essentia_test import *
from essentia.streaming import *


class TestVectorRealToTensor(TestCase):
    def testInvalidParam(self):
        # VectorRealToTensor only supports single chanel data
        self.assertConfigureFails(VectorRealToTensor(), {'shape': [1, 2, 1, 1]})

        # dimensions have to be different from 0.
        self.assertConfigureFails(VectorRealToTensor(), {'shape': [0, 1, 1, 1]})
        self.assertConfigureFails(VectorRealToTensor(), {'shape': [1, 0, 1, 1]})
        self.assertConfigureFails(VectorRealToTensor(), {'shape': [1, 1, 0, 1]})
        self.assertConfigureFails(VectorRealToTensor(), {'shape': [1, 1, 0, 0]})

suite = allTests(TestVectorRealToTensor)

if __name__ == '__main__':
    TextTestRunner(verbosity=2).run(suite)
