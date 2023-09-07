from utils import *

testing_class = utils()

test_values = ["127", 12.7, 127]
# test function #1, reversed
for test in test_values:
    print(testing_class.reversed(test))

# test function #2, formatter
for test in test_values:
    print(testing_class.formatter(test))