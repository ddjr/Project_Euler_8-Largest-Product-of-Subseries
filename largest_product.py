from sys import argv
script, filename = argv
import time


def open_file(filename):
    txt = open(filename)
    print "Openning file named: %r " % filename
    return txt.read()


def find_largest_product_in_series(series,subseries_size):
    largest_subseries = 0
    product_of_largest_subseries = 0
    for current_index in range(0,len(series)-subseries_size+1):
        current_subseries = series[current_index:current_index+subseries_size]
        product_of_current_subseries = find_product_of_series(current_subseries)
        if product_of_current_subseries > product_of_largest_subseries:
            product_of_largest_subseries = product_of_current_subseries
            largest_subseries = current_subseries
    return product_of_largest_subseries, largest_subseries


def find_product_of_series(series):
    product_of_series = 1
    for number in series:
        product_of_series *= int(number)
    return product_of_series



if __name__ == "__main__":
    # there is a hanging line at the end of the input file.
    # adding ###.spilt('n')[0] gets rid of it
    series = open_file(filename).split('\n')[0]
    subseries_size = 13
    print "(Largest Product, Subseries)",find_largest_product_in_series(series,subseries_size)
