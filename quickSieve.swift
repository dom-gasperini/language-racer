// Dominic Gasperini
// Swift Prime Sieve

// imports
import Swift
import Foundation


func primeSieve(primes: [Bool]) -> [Bool] {
    // set low primes
    var primes = primes
    primes[0] = false
    primes[1] = false

    // reduce the amount of number we need to check
    let length = Double(primes.count)
    let reducedLimit = Int(sqrt(length) + 1)

    for i in 3...reducedLimit {
        if (primes[i]) {
            for j in stride(from: (i * i), to: primes.count-1, by: i) {
                primes[j] = false
            }
        }
    }
    
    return primes
}

func primeCheck(primes: [Bool]) -> Bool {
    for i in 0...primes.count-1 {
        if (primes[i]) {
            if (!isPrime(number: i)) {
                return false
            } 
        }
    }

    return true
}

func isPrime(number: Int) -> Bool {
    // exit early for 2 
    if (number == 2) {
        return true
    }

    // exit early for small composites
    if (number < 2 || number % 2 == 0) {
        return false
    }

    // the number is large so now it's a manual check
    for i in stride(from: 3, to: number, by: 2) {
        if (number % i == 0) {
            return false
        }
    }

    return true
}

func main() {
    // get command line arguments
    let number = Int(CommandLine.arguments[1])!
    let passCount = Int(CommandLine.arguments[2])!

    // create array for the primes
    var primes: [Bool] = []
    
    // add trues
    for _ in 0...number {
        primes.append(true)
    }

    // run sieve for pass count
    for _ in 0...passCount {
        // set all to true
        for num in 0...primes.count-1 {
            primes[num] = true
        }

        // run the sieve!
        primes = primeSieve(primes: primes)
    }

    if !primeCheck(primes: primes) {
        exit(-1)
    }

    exit(0)
}


// run it!
main()