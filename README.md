# Dobble generator

A simple Python script that generates general Dobble games of order $q = p^m$, with $p$ prime and $m > 1$ integer.

## Requirements
* Python 3.x
* Library `galois` to perform finite field arithmetic.
```bash
pip install galois
```

## How to Use

### Option 1: Quick Copy & Paste (Recommended)
1. Open [dobble.py](dobble.py) in this repository.
2. Click the **"Copy raw contents"** icon in the top-right corner of the code box.
3. Paste the code into a local file named `dobble.py` on your computer.
4. Run it via terminal:
   ```bash
   python dobble.py 3 2
   ```

### Option 2: Clone the Repository
```bash
git clone https://github.com/massimozanetti/dobble-generator.git
cd YOUR_REPOSITORY_NAME
python dobble.py 3 2
```

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
