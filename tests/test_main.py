import unittest

"""
This script will discover and run all tests in the current directory. It will be used
to make automation more convenient.
"""

if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.discover('.', pattern='test_*.py', top_level_dir="..")
    test_runner = unittest.runner.TextTestRunner(verbosity=1)
    test_runner.run(tests)