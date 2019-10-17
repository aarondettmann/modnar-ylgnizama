#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Minimalistic simulation of the 'secretary problem'

See: https://en.wikipedia.org/wiki/Secretary_problem
"""

# Author: Aaron Dettmann

import random
import math

# Ration of applicants to reject
TRIAL_RATIO = 1/math.e


def run_secretary_problem(n):
    """
    Simulate a single run of the secretary problem and return chosen applicant

    The pool of 'applicants' is represented by a randomly ordered list of
    integers. Values in the list are unique. The greater the value, the
    'better' the applicant. For instance, for n = 5, the applicants list may be

    [5, 2, 3, 4, 1]

    Args:
        :n: (int) Number of candidates

    Returns:
        :chosen: (int) 'Rank' of chosen candidate
    """

    # List of randomly ordered, unique integers ranging from 1 to n
    applicants = random.sample(range(1, n+1), n)

    n_trial = int(n*TRIAL_RATIO)
    trial_group = applicants[0:n_trial]
    remain_group = applicants[n_trial:]

    best_in_trial = max(trial_group)
    for applicant in remain_group:
        chosen = applicant
        if applicant > best_in_trial:
            break

    return chosen


def get_int_from_prompt(msg, default):
    """
    Return integer from prompt input

    Args:
        :msg: (str) Message to print
        :default: (int) Default value

    Returns:
        :value: (int) Integer from prompt
    """

    while True:
        value = input(msg)

        if not value:
            return default
        else:
            try:
                value = int(value)
                return value
            except ValueError:
                print("Invalid input, try again...")


if __name__ == '__main__':
    n = get_int_from_prompt("Number of applicants [10] > ", 10)
    N = get_int_from_prompt("Number of of trial runs [10] > ", 10)

    chosen = []
    for _ in range(N):
        chosen.append(run_secretary_problem(n))

    n_best = chosen.count(n)
    n_2nd = chosen.count(n-1)
    n_3rd = chosen.count(n-2)
    n_worst = chosen.count(1)

    print()
    print(f"--> Chosen: {chosen}")
    print(f"--> Best chosen: {n_best} ({n_best/len(chosen)*100}%)")
    print(f"--> 2nd best: {n_2nd} ({n_2nd/len(chosen)*100}%)")
    print(f"--> 3rd best: {n_3rd} ({n_3rd/len(chosen)*100}%)")
    print(f"--> Top 3: ({(n_best+n_2nd+n_3rd)/len(chosen)*100}%)")
    print(f"--> Worst chosen: {n_worst} ({n_worst/len(chosen)*100}%)")
