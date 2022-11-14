# Dominic Gasperini
# Prime Sieve in R


primeSieve <- function(primes) {
    # set early primes
    primes[0] <- F
    primes[1] <- F

    # reduce run time by only caluclating up to the square root of the array
    smallLimit <- as.integer(sqrt(length(primes)) + 1)

    # run that sieve 
    for (i in 3:smallLimit) {
      if (primes[i]) {
        for (j in seq(from=(i * i), to=length(primes), by=i)) {
            primes[j] <- F
        }
      }
    }

    # return primes vector
    return(primes)
}


isPrime <- function(number) {
    if (number == 2) {
        return(T)
    }

    if (number < 2 | number %% 2 == 0) {
        return(F)
    }

    for (i in seq(from=3, to=sqrt(number), by=2)) {
        if (number %% i == 0) {
            return(F)
        }
    }

    # return true!
    T
}

primeCheck <- function(primes) {

    for (i in 1:length(primes)) {
        if (primes[i]) {
            if (!isPrime(i)) {
                return(F)
            }
        }
    }

    # return true
    T
}

main <- function() {
    # get command line arguments
    args <- commandArgs(trailingOnly = TRUE)
    number <- as.integer(args[1])
    passCount <- as.integer(args[2])

    # create logical vector
    primes <- logical(number)

    # run the sieve
    for (i in 0:passCount) {
        # reset array
        for (num in primes) {
            num <- T
        }

        # run sieve
        primes <- primeSieve(primes)
    }

    # confirm validitity
    if (!primeCheck(primes)) {
        print("invalid results")
        quit()
    }
}


# run it!
main()