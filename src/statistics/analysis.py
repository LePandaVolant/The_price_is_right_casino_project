def calculate_average(data):
    return sum(data) / len(data) if data else 0

def calculate_percentiles(data, percentiles):
    from numpy import percentile
    return {p: percentile(data, p) for p in percentiles}

def analyze_results(results):
    average = calculate_average(results)
    percentiles = calculate_percentiles(results, [0.1, 1, 5, 20, 25, 50, 75, 90, 95, 99])
    return average, percentiles

def print_analysis(average, percentiles):
    print(f"Average: {average}")
    for p, value in percentiles.items():
        print(f"{p}th Percentile: {value}")