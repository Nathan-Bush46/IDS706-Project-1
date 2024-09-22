"""
Test goes here

"""

import importlib.util
import sys
import pandas as pd

# from src.main_workspace.lib import calculate


def is_calc_valid(stat):
    """check is stat is of type list[(str,pd.Series.dype: float64)]"""
    if not isinstance(stat, list):
        return False
    for item in stat:
        if not (isinstance(item, tuple) and len(item) == 2):
            return False
        if not isinstance(item[0], str):
            return False
        if not isinstance(item[1], pd.Series):
            return False
        if item[1].dtype != "float64":
            return False
    return True


def test_lib():
    # load lib dynamically
    spec = importlib.util.spec_from_file_location("lib", "src/main_workspace/lib.py")
    assert spec is not None
    libary = importlib.util.module_from_spec(spec)
    assert libary is not None
    sys.modules["lib"] = libary
    spec.loader.exec_module(libary)
    # test lib
    stat = libary.calculate("src/main_workspace/data/hw1_q3_test_data.csv")
    assert stat is not None
    assert is_calc_valid(stat)


# if __name__ == "__main__":
#     test_lib()
