# Dominic Gasperini
# Module 3 - Open-Ended Project
# The Amazing Race!


# --- imports --- #
from ast import arg
from concurrent.futures import thread
import random
from language_sieves import * 
import threading
from telnetlib import Telnet
import matplotlib.pyplot as plt


# --- functions --- #
def get_user_input() -> int:
    while(True):
        # init a valid flag
        valid = True

        # get user input
        number = input("enter an integer: ")

        # don't crash on string to into conversion or floats
        try:
            number = int(number)

        except ValueError:
            print("invalid input, please enter an integer")
            continue
        
        # now ensure the number is within an approved range
        if number < 0:
            print("invalid input, enter an integer greater than 0")
            valid = False

        if number > 1000000000:
            print("invalid input, that's a little too big, try something smaller")
            valid = False

        if valid:
            return number


# --- main! --- #
def main():
    # welcome
    print("welcome to the amazing race!\n")
    print("you're about to witness a race between different programming languages")
    print("here's how it's going to work:")
    print("1. each language will find prime numbers up to a number specified by you!")
    print("2. they will perform this operation a number of time also specified by you!")
    print("3. each prime finder will loop until it has reached the designated pass count")
    print("4. the results of all languages will be plotted and the winner crowned!")
    print("---------------------------------------------------------------------------------")

    # get user input
    print("\nnow for the number for each finder to find primes up to (ex: 1000000)")
    number = get_user_input()
    print("and the number of times each finder should repeat its operations")
    pass_count = get_user_input()
    print("---------------------------------------------------------------------------------")


    # create threads
    cpp_thread = threading.Thread(target=run_cpp, name="cpp-thread", args=[number, pass_count])
    python_thread = threading.Thread(target=run_python, name="python-thread", args=[number, pass_count])
    rust_thread = threading.Thread(target=run_rust, name="rust-thread", args=[number, pass_count])
    go_thread = threading.Thread(target=run_go, name="go-thread", args=[number, pass_count])  
    swift_thread = threading.Thread(target=run_swift, name="swift-thread", args=[number, pass_count])
    perl_thread = threading.Thread(target=run_perl, name="perl-thread", args=[number, pass_count])
    java_thread = threading.Thread(target=run_java, name="java-thread", args=[number, pass_count])
    r_thread = threading.Thread(target=run_r, name="r-thread", args=[number, pass_count])
    julia_thread = threading.Thread(target=run_julia, name="julia-thread", args=[number, pass_count])

    # start threads
    cpp_thread.start()
    python_thread.start()
    rust_thread.start()
    go_thread.start()
    swift_thread.start()
    perl_thread.start()
    java_thread.start()
    r_thread.start()
    julia_thread.start()

    # wait for all to finish
    cpp_thread.join()
    python_thread.join()
    rust_thread.join()
    go_thread.join()
    swift_thread.join()
    perl_thread.join()
    java_thread.join()
    r_thread.join()
    julia_thread.join()

    # print results
    print("\n\nresults:\n")
    print(f"c++:\nduration: {cpp['duration']} seconds | file name: {cpp['filename']}")
    print(f"\npython:\nduration: {python['duration']} seconds | file name: {python['filename']}")
    print(f"\nrust:\nduration: {rust['duration']} seconds | file name: {rust['filename']}")
    print(f"\ngo:\nduration: {go['duration']} seconds | file name: {go['filename']}")
    print(f"\nswift:\nduration: {swift['duration']} seconds | file name: {swift['filename']}")
    print(f"\nperl:\nduration: {perl['duration']} seconds | file name: {perl['filename']}")
    print(f"\njava:\nduration: {java['duration']} seconds | file name: {java['filename']}")
    print(f"\nr:\nduration: {r['duration']} seconds | file name: {r['filename']}")
    print(f"\njulia:\nduration: {julia['duration']} seconds | file name: {julia['filename']}")

    # graph results
    results = {
        "C++" : cpp['duration'],
        "Python" : python['duration'],
        "Rust" : rust['duration'],
        "Go" : go['duration'],
        "Swift" : swift['duration'],
        "Perl" : perl['duration'],
        "Java" : java['duration'],
        "R" : r['duration'],
        "Julia" : julia['duration'],
    }

    names = list(results.keys())
    data = list(results.values())

    color_list = ['purple', 'red', 'green', 'blue', 'pink', 'olive', 'yellow', 'brown', 'orange', 'grey', 'palegreen', 'navy']
    random.shuffle(color_list)
    plt.bar(names, data, color=color_list, width=0.5)

    plt.gcf().canvas.manager.set_window_title("The Amazing (Programming) Race!")
    plt.title("Results of the Race!")
    plt.xlabel("Language")
    plt.ylabel("Runtime Duration (in seconds)")

    # Save & show the plot
    plt.savefig("Amazing_Race_Results.png")
    plt.show()

    # exit message 
    print("---------------------------------------------------------------------------------")
    print("Thanks for taking part in the amazing race!")



# --- run it! :) --- #
if __name__ == "__main__":
    main()