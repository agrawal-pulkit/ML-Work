#!/usr/bin/env python3

#-------------------------------------------------------------------------
# Copyright (c) @pulkit.  
# Author: Pulkit Agrawal
# Date: 04 of Aug 2018
#--------------------------------------------------------------------------

"""
Time complexity:
    O(n+k) for counting search.
    here k = 100
    total time complexity is O(n)
    Note:
        here i am using counting sort because of k is small as given in problem statement.
        otherwise for large number counting sort is not preferrable.

Run Command:
    Python program2.py 
    (OR)
    Python program2.py --list list.txt

"""

import random
import argparse

_default_random_list = 'R'


def countSort(unsorted_list):
    """
    Implemented counting search. 

    Args:
        unsorted_list: input unsorted array.
    
    Returns:
        return sorted list.
    """
    Aux = [0]*101
    for i in unsorted_list:
        if i in range(1, 101):
            Aux[i] += 1
    sorted_list =sum([[idx]*val for idx, val in enumerate(Aux)], [])
    print("sorted list: ", sorted_list)


def get_unsorted_list(input_file):
    """
    Getting input unsorted digits and covert to list for pass in counting sort.

    Args:
        input_file: input file path for creating millions of digit list.
    
    Returns:
        return list of unsorted digit.
    """
    if input_file == _default_random_list:
        print("randomfile")
        return [random.randint(1,100) for i in range(10**7)]
    else:
        print("inputfile")
        with open(input_file, 'r', encoding='utf-8') as f:
            A = []
            for line in f:
                A += [int(x) for x in line.split(",")] 
            return A


def main(input_file):
    """
    Main method to start counting sort.

    """
    countSort(get_unsorted_list(input_file))


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Fetch input')
    parser.add_argument("--list", dest="input_file_path", nargs=1, default=_default_random_list, help="Name of textfile for input list.  Default is randomlist")
    args = parser.parse_args()
    print("args: ", args.input_file_path[0])
    main(args.input_file_path[0])