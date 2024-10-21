# main.py
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort

def run_algorithm(algorithm, array):
    for step in algorithm(array):
        pass  # Run the sorting algorithm without visualization

if __name__ == "__main__":
    import argparse

    # Set up command-line argument parsing for choosing an algorithm
    parser = argparse.ArgumentParser(description="Run a sorting algorithm")
    parser.add_argument("algorithm", choices=["bubble", "quick", "merge", "selection", "insertion"], help="Algorithm to run")

    array = [64, 34, 25, 12, 22, 11, 90]  # Example array

    # Map algorithm names to the actual functions
    algorithms = {
        "bubble": bubble_sort,
        "quick": quick_sort,
        "merge": merge_sort,
        "selection": selection_sort,
        "insertion": insertion_sort
    }

    # Select the correct sorting function
    selected_algorithm = algorithms[parser.parse_args().algorithm]

    # Run the selected algorithm
    run_algorithm(selected_algorithm, array)

    print("Sorted array:", array)
