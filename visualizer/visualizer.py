# visualizer/visualizer.py
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .utils import generate_random_array
from algorithms.bubble_sort import bubble_sort
from algorithms.quick_sort import quick_sort
from algorithms.merge_sort import merge_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort

def visualize_sorting_algorithm(algorithm_func, array, speed):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(array)), array, align="edge")

    ax.set_xlim(0, len(array))
    ax.set_ylim(0, max(array) * 1.1)

    def update_fig(array, rects):
        for rect, val in zip(rects, array):
            rect.set_height(val)

    # Adjust animation speed by changing the interval
    anim = animation.FuncAnimation(
        fig, func=update_fig, fargs=(bar_rects,),
        frames=algorithm_func(array), interval=speed, repeat=False
    )

    plt.show()

if __name__ == "__main__":
    import argparse

    # Set up command-line argument parsing for choosing an algorithm and animation speed
    parser = argparse.ArgumentParser(description="Visualize a sorting algorithm")
    parser.add_argument("algorithm", choices=["bubble", "quick", "merge", "selection", "insertion"], help="Algorithm to visualize")
    parser.add_argument("--size", type=int, default=50, help="Size of the array to sort")
    parser.add_argument("--speed", type=int, default=50, help="Animation speed in milliseconds (lower is faster)")

    args = parser.parse_args()

    # Generate a random array of the given size
    array = generate_random_array(args.size)

    # Map algorithm names to the actual functions
    algorithms = {
        "bubble": bubble_sort,
        "quick": quick_sort,
        "merge": merge_sort,
        "selection": selection_sort,
        "insertion": insertion_sort
    }

    # Select the correct sorting function
    selected_algorithm = algorithms[args.algorithm]

    # Visualize the selected algorithm with the specified speed
    visualize_sorting_algorithm(selected_algorithm, array, args.speed)
