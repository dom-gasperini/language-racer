# imports 
import time
import os
import platform
import subprocess
from subprocess import PIPE, Popen
import time


# --- global variables --- #
cpp = {
    "filename" : "cppPrimeSieve.cpp",
    "duration": 0,
}

python = {
    "filename" : "snake_sieve.py",
    "duration": 0,
}

rust = {
    "filename" : "rusty_sieve.rs",
    "duration" : 0,
}

go = {
    "filename" : "stopSieve.go",
    "duration" : 0,
}

swift = {
    "filename" : "quickSieve.swift",
    "duration" : 0,
}

perl = {
    "filename" : "oysterSieve.pl",
    "duration" : 0,
}

java = {
    "filename" : "coffeeSieve.java",
    "duration" : 0,
}

r = {
    "filename" : "pirates_say.r",
    "duration" : 0,
}

julia = {
    "filename" : "julia.jl",
    "duration" : 0,
}


# C++ 
def run_cpp(number: int, pass_count: int):
    # start clock
    start = time.time()

    # compile c++ file
    try:
        subprocess.check_output("g++ -O2 " + cpp["filename"], stdin=None, stderr=subprocess.STDOUT, shell=True)

    except subprocess.CalledProcessError as e:
        # compiler errors detected, print out error message and exit
        print(e.output)
        raise SystemExit

    # run c++ file
    if platform.system() == 'Windows':
        p = Popen('a.exe ' + str(number) + str(pass_count), shell=True, stdout=PIPE, stdin=PIPE)
        os.remove("a.exe")

    # for mac os and linux
    else:
        to_run = "./a.out " + str(number) + " " + str(pass_count)
        process = Popen([to_run], shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()
        os.remove("a.out")
    
    # stop clockcount
    end = time.time()

    # save results
    cpp["duration"] = end - start


# Python
def run_python(number: int, pass_count: int):
    # start clock
    start = time.time()

    # run python file
    if platform.system() == 'Windows':
        to_run = "python " + python["filename"] + " " + str(number) + " " + str(pass_count)
        process = Popen(to_run, shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()

    # for mac os and linux
    else:
        to_run = "python3 " + python["filename"] + " " + str(number) + " " + str(pass_count)
        process = Popen([to_run], shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()
    
    # stop clockcount
    end = time.time()

    # save results
    python["duration"] = end - start


# Rust
def run_rust(number: int, pass_count: int):
    # start clock
    start = time.time()

    # compile rust file
    try:
        subprocess.check_output("rustc -C debuginfo=0 -C opt-level=3 " + rust["filename"], stdin=None, stderr=subprocess.STDOUT, shell=True)

    except subprocess.CalledProcessError as e:
        # compiler errors detected, print out error message and exit
        print(e.output)
        raise SystemExit

    # run rust file
    if platform.system() == 'Windows':
        to_run = "rusty_sieve.exe " + str(number) + " " + str(pass_count)
        process = Popen(to_run, shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()
        os.remove("rusty_sieve.exe")

    # for mac os and linux
    else:
        to_run = "./rusty_sieve " + str(number) + " " + str(pass_count)
        process = Popen([to_run], shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()
        os.remove("rusty_sieve")
    
    # stop clockcount
    end = time.time()

    # save results
    rust["duration"] = end - start


# Go
def run_go(number: int, pass_count: int):
    # start clock
    start = time.time()

    # run go file
    if platform.system() == 'Windows':
        to_run = "go run " + go["filename"] + " " + str(number) + " " + str(pass_count)
        process = Popen(to_run, shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()

    # for mac os and linux
    else:
        to_run = "go run " + go["filename"] + " " + str(number) + " " + str(pass_count)
        process = Popen([to_run], shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()
    
    # stop clockcount
    end = time.time()

    # save results
    go["duration"] = end - start


# Swift
def run_swift(number: int, pass_count: int):
    # start clock
    start = time.time()

    # compile rust file
    try:
        subprocess.check_output("swiftc -o main " + swift["filename"], stdin=None, stderr=subprocess.STDOUT, shell=True)

    except subprocess.CalledProcessError as e:
        # compiler errors detected, print out error message and exit
        print(e.output)
        raise SystemExit

    # run go file
    if platform.system() == 'Windows':
        to_run = "main.exe " + str(number) + " " + str(pass_count)
        process = Popen(to_run, shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()

    # for mac os and linux
    else:
        to_run = "./main " + str(number) + " " + str(pass_count)
        process = Popen([to_run], shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()
    
    # stop clockcount
    end = time.time()

    # save results
    swift["duration"] = end - start


# Perl
def run_perl(number: int, pass_count: int):
    # start clock
    start = time.time()

    # run go file
    if platform.system() == 'Windows':
        to_run = "perl " + perl["filename"] + " " + str(number) + " " + str(pass_count)
        process = Popen(to_run, shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()

    # for mac os and linux
    else:
        to_run = "perl " + perl["filename"] + " " + str(number) + " " + str(pass_count)
        process = Popen([to_run], shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()
    
    # stop clockcount
    end = time.time()

    # save results
    perl["duration"] = end - start


# Java
def run_java(number: int, pass_count: int):
    # start clock
    start = time.time()

    # complie java file
    try:
        subprocess.check_output("javac " + java["filename"], stdin=None, stderr=subprocess.STDOUT, shell=True)

    except subprocess.CalledProcessError as e:
        # compiler errors detected, print out error message and exit
        print(e.output)
        raise SystemExit

    # run go file
    if platform.system() == 'Windows':
        to_run = "java coffeeSieve " + str(number) + " " + str(pass_count)
        process = Popen(to_run, shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()
        os.remove("coffeeSieve.class")

    # for mac os and linux
    else:
        to_run = "java coffeeSieve " + str(number) + " " + str(pass_count)
        process = Popen([to_run], shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()
        os.remove("coffeeSieve.class")
    
    # stop clockcount
    end = time.time()

    # save results
    java["duration"] = end - start


# R
def run_r(number: int, pass_count: int):
    # start clock
    start = time.time()

    # run go file
    if platform.system() == 'Windows':
        to_run = "Rscript " + r["filename"] + " " + str(number) + " " + str(pass_count)
        process = Popen(to_run, shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()

    # for mac os and linux
    else:
        to_run = "Rscript " + r["filename"] + " " + str(number) + " " + str(pass_count)
        process = Popen([to_run], shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()
    
    # stop clockcount
    end = time.time()

    # save results
    r["duration"] = end - start


# Julia
def run_julia(number: int, pass_count: int):
    # start clock
    start = time.time()

    # run go file
    if platform.system() == 'Windows':
        to_run = "julia " + julia["filename"] + " " + str(number) + " " + str(pass_count)
        process = Popen(to_run, shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()

    # for mac os and linux
    else:
        to_run = "julia " + julia["filename"] + " " + str(number) + " " + str(pass_count)
        process = Popen([to_run], shell=True, stdout=PIPE, stdin=PIPE)
        process.wait()
    
    # stop clockcount
    end = time.time()

    # save results
    julia["duration"] = end - start
