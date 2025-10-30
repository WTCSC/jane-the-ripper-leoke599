import hashlib

def crack_passwords(hash_file_path, wordlist_path):
    hash_set = set()
    cracked_hashes = set()

    with open(f'{hash_file_path}', 'r') as f:

        for hashes in f:
            clean_hash = hashes.strip()
            hash_set.add(clean_hash)
        

    with open(f'{wordlist_path}', 'r') as f:
        for words in f:
            clean_word = words.strip()
            encoded_word = hashlib.md5(clean_word.encode())
            hashed_word = encoded_word.hexdigest()
            if hashed_word in hash_set:
                print(f"Cracked: {hashed_word} --> {clean_word}")
                cracked_hashes.add(hashed_word)
    
    uncracked_hashes = hash_set - cracked_hashes
    if uncracked_hashes:
        print("\n--- Hashes that could NOT be cracked ---")
        for hash_value in uncracked_hashes:
            print(f"Not Cracked: {hash_value}")

def main():
    hash_file_path = input("Enter path to hash file: ")
    wordlist_path = input("Enter path to wordlist file: ")
    crack_passwords(hash_file_path, wordlist_path)

main()