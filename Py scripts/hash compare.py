# Input the two hashes
hash1 = input("Enter the first SHA256 hash: ").strip()
hash2 = input("Enter the second SHA256 hash: ").strip()

# Compare and display the result
if hash1 == hash2:
    print("The hashes match!")
else:
    print("The hashes do not match.")
    print(f"Difference:\nHash 1: {hash1}\nHash 2: {hash2}")
input("\nPress Enter to exit...")