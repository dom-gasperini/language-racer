// Dominic Gasperini
// Go Prime Sieve

// packages
package main

// imports
import (
	"os"
	"strconv"
)

// prime sieve
func primeSieve(primes []bool) []bool {
	// get size of array
	size := len(primes) - 1

	// prime sieve
	primes[0] = false
	primes[1] = false
	for multiplier := 2; multiplier*multiplier <= size; multiplier++ {
		if primes[multiplier] == true {
			for i := multiplier * 2; i <= size; i += multiplier {
				primes[i] = false
			}
		}
	}

	return primes
}

// prime check
func primeCheck(primes []bool) bool {
	for i := 0; i < len(primes)-1; i++ {
		if primes[i] {
			result := isPrime(i)
			if !(result) {
				return false
			}
		}
	}

	return true
}

// is prime
func isPrime(num int) bool {
	// stop on early primes
	if num == 2 {
		return true
	}

	if num < 2 || num%2 == 0 {
		return false
	}

	i := 3
	for (i * i) <= num {
		if num%i == 0 {
			return false
		}
		i += 2
	}

	return true
}

// main
func main() {
	// get command line arguments
	numberArg := os.Args[1]
	passCountArg := os.Args[2]

	// convert to int type
	number, err := strconv.Atoi(numberArg)
	if err != nil {
		panic(err)
	}

	// convert to int type
	passCount, err := strconv.Atoi(passCountArg)
	if err != nil {
		panic(err)
	}

	// create prime storage - initialized with all false (0) values
	primeStorage := make([]bool, number)

	// have all values of the array be set to true
	for i := range primeStorage {
		primeStorage[i] = true
	}

	// run loop
	for i := 0; i < passCount; i++ {
		// reset array
		for i := range primeStorage {
			primeStorage[i] = true
		}

		// run sieve
		primeStorage = primeSieve(primeStorage)
	}

	// check for incorrect primes
	if !primeCheck(primeStorage) {
		os.Exit(1)
	}
}
