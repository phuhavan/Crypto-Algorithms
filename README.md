# Crypto Algorithms Repository

Welcome to the **Crypto Algorithms Repository**! This project provides implementations of various cryptographic algorithms, including symmetric encryption, asymmetric encryption, hashing functions, key exchange protocols, and post-quantum cryptography algorithms. These implementations serve as a reference design for developers, researchers, and security professionals looking to understand and apply cryptographic techniques in their systems.

Cryptographic algorithms form the core **foundation of secure systems**, ensuring data confidentiality, integrity, and authentication in various applications such as secure communication, digital signatures, and data protection. This repository offers well-structured and modular implementations of these essential cryptographic primitives.

## Repository Structure

```
Crypto-Algorithms/
│── algorithms/
│   ├── symmetric/
│   ├── asymmetric/
│   ├── hashing/
│   ├── key_exchange/
│   ├── post_quantum/
│── examples/
│── tests/
│── docs/
│── requirements.txt
│── setup.py
│── .gitignore
│── LICENSE
│── README.md
```

## Implemented Algorithms

### Symmetric Encryption
- **AES (Advanced Encryption Standard)**
- **DES (Data Encryption Standard)**
- **RC4 (Rivest Cipher 4)**
- **Blowfish**

### Asymmetric Encryption
- **RSA (Rivest–Shamir–Adleman)**
- **ECC (Elliptic Curve Cryptography)**
- **DSA (Digital Signature Algorithm)**
- **ElGamal**

### Hashing Functions
- **SHA-256 (Secure Hash Algorithm 256-bit)**
- **MD5 (Message Digest Algorithm 5)**
- **Bcrypt**
- **Argon2**

### Key Exchange Protocols
- **Diffie-Hellman**
- **ECDH (Elliptic Curve Diffie-Hellman)**
- **SRP (Secure Remote Password)**

### Post-Quantum Cryptography
- **CRYSTALS-Kyber**
- **CRYSTALS-Dilithium**
- **NTRU (N-th Degree Truncated Polynomial Ring Units)**
- **Falcon**

## Usage
To use these algorithms, install the dependencies and run the scripts:

```bash
pip install -r requirements.txt
python examples/encrypt_decrypt_example.py
```

## Running Tests
To ensure correctness, run the test suite:

```bash
pytest tests/
```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

---

**Happy Coding & Secure Communications!**

