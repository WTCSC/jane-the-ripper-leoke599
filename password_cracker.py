import hashlib

def crack_passwords(hash_file_path, wordlist_path):
    hash_set = set()

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
                print(f"Cracked: {hashed_word} -> {clean_word}")
            else:
                print(f"Failed: {hashed_word}")
            


def main():
    hash_file_path = input("Enter path to hash file: ")
    wordlist_path = input("Enter path to wordlist file: ")
    crack_passwords(hash_file_path, wordlist_path)
    print("running main")

main()