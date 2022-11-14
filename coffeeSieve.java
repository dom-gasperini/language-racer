/**
 * Dominic Gasperini
 * Java Prime Sieve
 */

// imports
import java.util.ArrayList;
import java.lang.Math;;

/**
 * coffeeSieve Class! 
 */
public class coffeeSieve {
    public static void main(String[] args) {
        // gather command line arguments
        int size = Integer.parseInt(args[0]);
        int passCount = Integer.parseInt(args[1]);


        // create arraylist to represent the primes
        ArrayList<Boolean> primes = new ArrayList<Boolean>();

        // fill with true
        for (int i = 0; i < size - 1; ++i) {
            primes.add(i, true);
        }

        // run the sieve!
        for (int i = 0; i < passCount; ++i) {
            // reset all to true
            for (int j = 0; j < primes.size() - 1; ++j) {
                primes.set(j, true);
            }

            // run the sieve
            primes = primeSieve(primes);
        }

        // check if those primes are valid!
        if (!primeCheck(primes)) {
            System.exit(-1);
        }
    }


    /**
     * this function runs a prime sieve!
     * @param primes the arraylist of booleans
     * @return the same arraylist, but now all the composite numbers are marked as false
     */
    public static ArrayList<Boolean> primeSieve(ArrayList<Boolean> primes) {
        primes.set(0, false);
        primes.set(1, false);

        // loop through the prime array marking non-primes as false
        int smallerLimit = (int) Math.sqrt(primes.size()) + 1;
        for (int p = 3; p < smallerLimit; ++p) {
            if (primes.get(p)) {
                for (int i = (p * p); i < primes.size() - 1; i += p) {
                    primes.set(i, false);
                }
            }
        }

        return primes;
    }

    
    /**
     * this function tests the arraylist for invalid primes
     * @param primes an arraylist of booleans 
     * @return a boolean as to wether all of the primes in the list are actually primes
     */
    public static boolean primeCheck(ArrayList<Boolean> primes) {
        // iterate through the vector testing if each number is prime or not
        for (int i = 0; i < (primes.size() - 1); ++i) {
            if (primes.get(i)) {
                if (!isPrime(i)) {
                    return false;
                } 
            }
        }
        
        return true;
    }

    /**
     * this function determines if a number is prime or not
     * @param number the number to be tested
     * @return a boolen as to whether the number was prime or not
     */
    public static boolean isPrime(int number) {
        // stop on the first prime!
        if (number == 2) {
            return true;
        }

        // test less than 2 and if divisable by 2
        if (number < 2 || number % 2 == 0) {
            return false;
        }

        // for any number larger than 2
        for (int i = 3; (i * i) <= number; i += 2) {
            if (number % i == 0) {
                return false;
            }
        }

        return true;
    }
}