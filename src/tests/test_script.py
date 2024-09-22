"""
Test
 """

import importlib.util
import sys
import os.path


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    assert module is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_stats_pdf():
    # Load lib.py
    lib = load_module("lib", "src/main_workspace/lib.py")
    # Load stats.py
    stats_pdf = load_module("stats_pdf", "src/main_workspace/stats_pdf.py")

    stats = lib.calculate("src/main_workspace/data/hw1_q3_test_data.csv")
    stats_pdf.print_to_pdf(stats, "src/main_workspace/outputs/")
    assert os.path.isfile("src/main_workspace/outputs/scatter_plot.png")
    assert os.path.isfile("src/main_workspace/outputs/example_stats.pdf")


# if __name__ == "__main__":
#     test_stats_pdf()
