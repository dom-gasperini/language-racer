// Dominic Gasperini
// Rust Prime Sieve

// namespace 
use std::env;
use std::process;
use std::convert::TryInto;


// main!
fn main() {
    // gather command line arguments
    let args: Vec<String> = env::args().collect();

    // set command line arguments
    let number: usize = args[1].parse().unwrap();
    let pass_count: usize = args[2].parse().unwrap();

    // create vector for primes and set all to true
    let mut primes = Vec::new();
    primes.resize(number, true);

    // now run the sieve
    for _ in 1..pass_count {
        // reset array
        primes.resize(number, true); 

        // run sieve
        prime_sieve(&mut primes);     
    }

    // check for valid primes
    if !prime_check(&primes) {
        process::exit(-1);
    }
}


fn prime_sieve(primes: &mut Vec<bool>) {
    // run the sieve
    primes[0] = false;
    primes[1] = false;

    let size = primes.len() as f64;

    let upper_limit = f64::sqrt(size) as usize + 1;
    for p in 3..(upper_limit) {
        if primes[p] {
            for i in ((p * p)..(primes.len() - 1)) {
                primes[i] = false;
            }
        }
    }
}


fn prime_check(primes: &Vec<bool>) -> bool {
    // check all numbers in the vector
    for i in 0..primes.len()-1 {
        if primes[i] {
            if !is_prime(i.try_into().unwrap()) {
                return false;
            }
        }
    }

    return true;
}


fn is_prime(number: i32) -> bool {
    if number == 2 {
        return true;
    }
    
    if number < 2 || number % 2 == 0 {
        return false;
    }

    let mut i = 3;
    let step = 2;
    while (i*i) <= number {
        if number % i == 0 {
            return false;
        }
        i += step;
    }

    return true;
}