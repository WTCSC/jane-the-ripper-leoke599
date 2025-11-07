# Jane the Ripper - Password Cracker

A Python-based MD5 password cracker that uses dictionary/wordlist attacks to crack hashed passwords.

## 📋 Description

This tool attempts to crack MD5 password hashes by comparing them against a wordlist of potential passwords. It reads a file containing MD5 hashes and systematically hashes each word from a wordlist to find matches. Successfully cracked passwords are displayed along with their original hashes.

## ✨ Features

- **MD5 Hash Cracking**: Cracks MD5-hashed passwords
- **Wordlist Attack**: Uses dictionary-based attack methodology
- **Efficient Matching**: Uses set-based lookups for fast hash comparison
- **Progress Reporting**: Displays cracked passwords in real-time
- **Uncracked Hash Reporting**: Shows which hashes could not be cracked

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Built-in `hashlib` library (included with Python)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/WTCSC/jane-the-ripper-leoke599.git
cd jane-the-ripper-leoke599
```

2. Ensure you have Python 3 installed:
```bash
python --version
```

## 💻 Usage

### Basic Usage

Run the script and provide the required file paths when prompted:

```bash
python password_cracker.py
```

The program will ask for:
1. Path to the hash file (e.g., `hashes.txt`)
2. Path to the wordlist file (e.g., `wordlist.txt`)

### Example

```
Enter path to hash file: hashes.txt
Enter path to wordlist file: wordlist.txt

Cracked: e99a18c428cb38d5f260853678922e03 --> abc123
Cracked: 40be4e59b9a2a2b5dffb918c0e86b3d7 --> password
Cracked: aa47f8215c6f30a0dcdb2a36a9f4168e --> 123456

--- Hashes that could NOT be cracked ---
Not Cracked: a53f3929621dba1306f8a61588f52f55
Not Cracked: c33367701511b4f6020ec61ded352059
```

## 📁 File Structure

```
jane-the-ripper-leoke599/
├── password_cracker.py    # Main password cracker script
├── hashes.txt            # Sample file containing MD5 hashes
├── wordlist.txt          # Sample wordlist for dictionary attack
└── README.md             # This file
```

## 🔧 How It Works

1. **Load Hashes**: Reads all MD5 hashes from the target file into a set
2. **Process Wordlist**: Iterates through each word in the wordlist
3. **Hash Generation**: Converts each word to its MD5 hash
4. **Comparison**: Checks if the generated hash matches any target hash
5. **Report Results**: Displays cracked passwords and remaining uncracked hashes

### Algorithm Complexity

- **Time Complexity**: O(n × m) where n = wordlist size, m = hash file size
- **Space Complexity**: O(h) where h = number of hashes

## ⚠️ Important Notes

### Educational Purpose

This tool is designed for **educational purposes only** to demonstrate:
- How password cracking works
- Why weak passwords are vulnerable
- The importance of using strong, unique passwords
- How dictionary attacks operate

### Legal & Ethical Considerations

- ⚠️ **Only use this tool on systems you own or have explicit permission to test**
- Unauthorized password cracking is illegal in most jurisdictions
- This tool should only be used for learning, security research, or authorized penetration testing

### Security Limitations

- **MD5 is Weak**: MD5 is cryptographically broken and should not be used for password storage
- **Dictionary Attacks**: Only effective against weak passwords in the wordlist
- **No Salting**: This tool does not handle salted hashes
- **Limited Scope**: Does not perform brute force, rainbow table, or other advanced attacks

## 🎓 Educational Value

This project demonstrates:
- File I/O operations in Python
- Working with hash functions (`hashlib`)
- Set operations for efficient lookups
- Basic cybersecurity concepts
- The vulnerability of unsalted MD5 hashes

## 🔒 Best Practices for Password Security

After understanding how this tool works, remember to:
- Use strong, unique passwords for each account
- Enable two-factor authentication (2FA)
- Use a password manager
- Never reuse passwords across services
- Use modern hashing algorithms (bcrypt, Argon2, scrypt) with salting

## 📝 Author

**Leo Ke**  
Date: November 3, 2025

## 📄 License

This project is for educational purposes. Please use responsibly and ethically.

## 🤝 Contributing

This is an educational project. If you'd like to suggest improvements or report issues, feel free to open an issue or submit a pull request.

---

**Remember**: With great power comes great responsibility. Use this knowledge to build more secure systems, not to break them. 🛡️