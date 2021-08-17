from dice_stats import dice_rolls
import numpy as np

def bar_chart_data(numbers, minimum=None, maximum=None, num_bins=None, density=False):
    minimum = minimum if minimum is not None else min(numbers)
    maximum = maximum if maximum is not None else max(numbers)
    num_bins = num_bins if num_bins is not None else int(maximum - minimum) + 1

    values, labels = np.histogram(numbers, range=(minimum, maximum), bins=num_bins, density=density)
    return (values.tolist(), [int(np.ceil(x)) for x in labels][:-1])