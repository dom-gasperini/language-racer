/**
 * @file primeSieve.cpp
 * @author your name (you@domain.com)
 * @brief 
 */


// --- includes --- //
#include <iostream>
#include <vector>
#include <math.h>


// --- namespace --- //
using namespace std;


// --- function declarations --- //
vector<bool> primeSieve(vector<bool> primes);
bool primeCheck(vector<bool> primes);
bool isPrime(int number);


// main!
int main(int argc, char const *argv[])
{
    // inits
    vector<bool> primes;
    int passCount;
    int size;

    // Get command line input
    if (argc > 1) {
        size = stoi(argv[1]);
        passCount = stoi(argv[2]);
    }
    else {
        return -1;
    }

    // fill the vector with all true primes as placeholders
    for (int i = 0; i < size; ++i) {
        primes.push_back(true);
    }

    // run the sieve
    for (int i = 0; i < passCount; ++i) {
        // reset primes array to all true
        for (int j = 0; j < primes.size() - 1; ++j) {
            primes[j] = true;
        }

        // run sieve
        primes = primeSieve(primes);
    }

    // verify primes 
    if (!primeCheck(primes)) {
        return -1;
    }
    
    // return successfully! :)
    return 0;
}


/**
 * @brief prime sieve
 * 
 * @param count the max value to search to
 * @param primes 
 */
vector<bool> primeSieve(vector<bool> primes) {
    primes[0] = false;
    primes[1] = false;

    // loop through the prime array marking non-primes as false
    int smallerLimit = (int) sqrt(primes.size()) + 1;
    for (int i = 3; i < smallerLimit; ++i) {
        if (primes[i]) {
            for (int j = (i * i); j < primes.size() - 1; j+=i) {
                primes[j] = false;
            }
        }
    }

    return primes;
}


/**
 * @brief 
 * 
 * @param primes 
 * @return true 
 * @return false 
 */
bool primeCheck(vector<bool> primes) {
    bool valid = true;

    for (int i = 0; i < (primes.size() - 1); ++i) {
        if (primes.at(i)) {
            if (!isPrime(i)) {
                valid = false;
            } 
        }
    }

    return valid;
}


/**
 * @brief 
 * 
 * @return true 
 * @return false 
 */
bool isPrime(int number) {
    // catch early primes and eliminate all numbers divisable by 2
    if (number == 2) {
        return true;
    }

    if (number < 2 || number % 2 == 0) {
        return false;
    }

    // if the number is larger 
    for (int i = 3; (i * i) <= number; i += 2) {
        if (number % i == 0) {
            return false;
        }
    }
    
    // otherwise the number is prime!
    return true;
}