"""
Password Cracker - Jane the Ripper
Author: Leo Ke
Date: November 3, 2025

Description:
This program attempts to crack MD5 password hashes using a wordlist attack.
It reads a file containing MD5 hashes and attempts to match them against
passwords from a wordlist by hashing each word and comparing it to the
target hashes. Successfully cracked passwords are displayed, and any
hashes that could not be cracked are reported at the end.
"""

import hashlib

def crack_passwords(hash_file_path, wordlist_path):
    """
    Attempts to crack MD5 hashes using a wordlist attack.
    
    Args:
        hash_file_path: Path to file containing MD5 hashes (one per line)
        wordlist_path: Path to wordlist file containing potential passwords
    """
    # Create empty set to hold target hashes to crack
    hash_set = set()

    # Create empty set to track successfully cracked hashes
    cracked_hashes = set()

    # Read hash file and load all hashes into a set
    with open(f'{hash_file_path}', 'r') as f:

        for hashes in f:
            clean_hash = hashes.strip()  # Remove whitespace/newlines
            hash_set.add(clean_hash)
        
    # Try each word in the wordlist as a potential password
    with open(f'{wordlist_path}', 'r') as f:
        for words in f:
            clean_word = words.strip()  # Remove whitespace/newlines
            encoded_word = hashlib.md5(clean_word.encode())  # Encode to bytes
            hashed_word = encoded_word.hexdigest()  # Generate MD5 hash

            # Check if this hash matches any target hash
            if hashed_word in hash_set:
                print(f"Cracked: {hashed_word} --> {clean_word}")
                cracked_hashes.add(hashed_word)  # Track successful crack
    
    # Identify hashes that were not cracked
    uncracked_hashes = hash_set - cracked_hashes
    if uncracked_hashes:
        print("\n--- Hashes that could NOT be cracked ---")
        for hash_value in uncracked_hashes:
            print(f"Not Cracked: {hash_value}")

def main():
    """
    Main function to run the password cracker.
    Prompts user for file paths and initiates the cracking process.
    """
    # Get file paths from user
    hash_file_path = input("Enter path to hash file: ")
    wordlist_path = input("Enter path to wordlist file: ")
    
    # Run the password cracker
    crack_passwords(hash_file_path, wordlist_path)

# Run the program
main()