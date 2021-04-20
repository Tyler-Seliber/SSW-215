import unittest
from part1_dodecahedron import roll_dodecahedron

# Simulate 10000 dodecahedron rolls
simulated_values = []
for i in range(0,10000):
    simulated_values.append(roll_dodecahedron())

# Statistical constants
a = 1
b = 12
n = (b-a) + 1

# Descriptive statistics
# Mean
true_mean = (a + b) / 2
sample_mean = sum(simulated_values)/len(simulated_values)

# Standard deviation
sample_std = 0 
for i in range(0,len(simulated_values)):
    sample_std += (simulated_values[i] - sample_mean) ** 2
sample_std = (sample_std / (len(simulated_values) - 1)) ** (1/2)

# Variance
true_var = ((n ** 2) - 1) / 12
sample_var = sample_std ** 2

class TestDistribution(unittest.TestCase):

    def test_mean(self):
        """ Test if mean value is sufficiently close to expected """
        self.assertAlmostEqual(true_mean, sample_mean, delta = 0.2, msg = 'True and Sample means are significantly different.')

    def test_variance(self):
        """ Test is variance value is sufficiently close to expected """
        self.assertAlmostEqual(true_var, sample_var, delta = 0.2, msg = 'True and Sample variances are significantly different.')

if __name__ == '__main__':
    unittest.main()