# Samples of the uniform distribution will average out to a normal distribution 

import random
import plotly.express as px

def main() -> None:

    sample_size = 31
    sample_count = 1000

    # Central limit theorem, 1000 samples each with 31 random numbers between 0.0 and 0.1
    random.seed(42)
    x_values: list[float] = [
        (
            sum([random.uniform(0.0, 1.0) for _ in range(sample_size)]) / sample_size
        ) 
        for _ in range(sample_count)
    ]
    
    y_values: list[int] = [1 for _ in range(sample_count)]

    px.histogram(x = x_values, y = y_values, nbins = 20).show()

if __name__ == '__main__':
    main()
