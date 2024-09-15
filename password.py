import itertools
import string
import hashlib

def brute_force_attack(target_hash, max_length=4):
    # Define the possible characters (e.g., lowercase, uppercase, digits)
    characters = string.ascii_letters + string.digits
    print(f"Starting brute-force attack...")

    # Try all combinations from length 1 to max_length
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            guess_hash = hashlib.sha256(guess.encode()).hexdigest()  # Hash the guess
            print(f"Trying password: {guess} -> Hash: {guess_hash}")
            if guess_hash == target_hash:
                print(f"Password found: {guess}")
                return guess
    print("Password not found")
    return None

# Example usage:
# Assume we are ethically testing a system where the password is "abc123", and we know the hash.
# We use SHA-256 for hashing.
real_password = "abc"
hashed_password = hashlib.sha256(real_password.encode()).hexdigest()  # Hashed password

# Now, we perform the brute-force attack to find the password
found_password = brute_force_attack(hashed_password, max_length=4)

#can you update it to hack any wifi and passwords pls the program run only in py
#but i have to run it in like that so it can type password in notepad or in msword or
#any thing 
