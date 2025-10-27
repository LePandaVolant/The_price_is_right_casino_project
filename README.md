# Gambling Simulation

This project is a gambling simulation that allows users to guess a number using different strategies. The simulation implements various algorithms and statistical analyses to evaluate the effectiveness of each strategy.

## Project Structure

```
gambling-simulation
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── algorithms
│   │   ├── __init__.py
│   │   └── binary_search.py
│   ├── statistics
│   │   ├── __init__.py
│   │   └── analysis.py
│   ├── strategies
│   │   ├── __init__.py
│   │   ├── strategy1.py
│   │   ├── strategy2.py
│   │   └── strategy3.py
│   ├── game
│   │   ├── __init__.py
│   │   └── interactive_game.py
│   └── utils
│       ├── __init__.py
│       └── calculations.py
├── tests
│   ├── __init__.py
│   ├── test_algorithms.py
│   ├── test_strategies.py
│   └── test_game.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the gambling simulation, execute the `main.py` file:

```
python src/main.py
```

## Strategies

The simulation includes the following strategies:

1. **Strategy 1**: Multiplies the bet based on the number of attempts taken to guess the number.
2. **Strategy 2**: Similar to Strategy 1 but with different multipliers.
3. **Strategy 3**: Offers higher multipliers for fewer attempts.

## Testing

Unit tests are provided for each module. To run the tests, use:

```
pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.