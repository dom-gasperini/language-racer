#!/usr/bin/perl

use warnings;

# Dominic Gasperini 
# Perl Prime Sieve


sub isPrime {
    # gather passed arguments
    my $number = $_[0];

    # knock out those small primes
    if ($number == 2) {
        return 1;
    }

    if ($number < 2 || $number % 2 == 0) {
        return 0;
    }

    for (my $i = 3; ($i * $i) <= $number; $i += 2) {
        if ($number % $i == 0) {
            return 0;
        }
    }

    return 1;
}


sub primeCheck {
    # gather passed arguments
    my $primes = $_[0];
    my $size = $_[1];

    # iterate through primes array
    for my $i (0..$size-1) {
        if ($primes->[$i] == 1) {
            if (isPrime($i) == 0) {
                return 0;
            }
        }
    }
    return 1;
}


sub primeSieve {
    # gather passed arguments
    my $primes = $_[0];
    my $size = $_[1];

    # set first two numbers to 0
    $primes->[0] = 0;
    $primes->[1] = 0;

    # loop through the prime array marking non-primes as 0
    my $smallerLimit = int(sqrt($size)) + 1;

    for my $i (2..$smallerLimit) {
        if ($primes->[$i] == 1) {
            for (my $j = ($i * $i); $j < $size; $j+=$i) {
                $primes->[$j] = 0;
            }
        }
    }
}


# main script!
# get command line arguments
my ($number, $passCount) = @ARGV;

# create primes array
my @primes = ();

# fill array with 1 (true)
my @upper = (1..$number);
for (@upper){
    push(@primes, 1);
}

# run the sieve!
for (1..$passCount) {
    # set all to true
    foreach my $num (@primes) {
        $num = 1;
    }

    # run do some sieveing
    primeSieve(\@primes, scalar @primes);
}

# test validiity of primes
if (!primeCheck(\@primes, scalar @primes)) {
    print "failed!\n";
    exit(-1);
}

exit(0);