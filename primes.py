"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
from math import sqrt

def primes(number_of_primes):
    _validate_argument(number_of_primes)
    primes = _generate_primes(number_of_primes)
    return primes

def _validate_argument(list_length):
    if list_length <= 0:
        raise ValueError(f"n={list_length} should be a positive number")

def _generate_primes(number_of_primes):
    primes = [2]
    for i in range(number_of_primes-1):
        prime = _get_next_prime(primes)
        primes.append(prime)
    return primes

def _get_next_prime(primes):
    number = primes[len(primes)-1] + 1
    while not _is_prime(number, primes):
        number += 1
    return number


def _is_prime(number, primes):
    for prime in primes:
        if prime > sqrt(number):
            return True
        elif number % prime == 0:
            return False
    return True