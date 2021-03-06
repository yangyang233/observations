from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import shutil
import sys
import tempfile

from observations.r.cbpp import cbpp


def test_cbpp():
  """Test module cbpp.py by downloading
   cbpp.csv and testing shape of
   extracted data has 56 rows and 4 columns
  """
  test_path = tempfile.mkdtemp()
  x_train, metadata = cbpp(test_path)
  try:
    assert x_train.shape == (56, 4)
  except:
    shutil.rmtree(test_path)
    raise()
