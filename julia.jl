# Dominic Gasperini
# Prime Sieve in Julia

function primeSieve(primes) 
    primes[1] = false
    primes[2] = false

    reducedLimit = Int(sqrt(length(primes) - 1)) + 1

    for i in 3:reducedLimit 
        if primes[i]
            for j in (i * i):i:length(primes) - 1 
                primes[j] = false
            end
        end
    end

    return primes
end


function primeCheck(primes) 
    for i in 1:length(primes) - 1
        if primes[i]
            if !isPrime(i)
                return false
            end
        end
    end

    return true
end


function isPrime(number)
    if number == 2
        return true
    end

    if number < 2 || number % 2 == 0
        return false
    end
    
    for i in 1:2:number
        if number % i == 0
            return false
        end
    end

    return true
end


function main()
    # get command line arguments
    number = parse(Int, ARGS[1])
    pass_count = parse(Int, ARGS[2])

    # initialize prime storage
    primes = []
    for _ in 0:number
        push!(primes, true)
    end

    # run the sieve
    for _ in 0:pass_count
        # reset prime storage
        for num in primes
            num = true
        end

        # run sieve
        primes = primeSieve(primes)
    end 

    # validate primes
    if !primeCheck(primes)
        exit(-1)
    end

    exit(0)
end


# run it!
main()