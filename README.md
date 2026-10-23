# Dobble games generator

A simple Python script that generates general Dobble games of order $q = p^m$, with $p$ prime and $m \geq 1$ integer.

Here I have explained the mathematical formulation of Dobble games: [dobble.pdf](dobble.pdf) 

## Requirements
* Python 3.x
* Library `galois` to perform finite field arithmetic:
  ```bash
  pip install galois
  ```

## How to Use

1. Copy the [dobble.py](dobble.py) script into a local file named `dobble.py` on your computer.
2. See helper for the arguments:
   ```bash
   python dobble.py -h
   usage: dobble.py [-h] p m

   Generator of Dobble games of prime power order q=p^m
   
   positional arguments:
     p           prime base
     m           power exponent
   
   options:
     -h, --help  show this help message and exit

   ```
3. Generate a Dobble game of order $q=3^2$:
   ```bash
   python dobble.py 3 2
   ```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
