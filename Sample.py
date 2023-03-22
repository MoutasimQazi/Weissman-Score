import zlib
import os

filename = "example.txt"

with open(filename, "rb") as f:
    data = f.read()

compressed_data = zlib.compress(data)

compression_ratio = len(compressed_data) / len(data)

print(f"Original file size: {os.path.getsize(filename)} bytes")
print(f"Compressed file size: {len(compressed_data)} bytes")
print(f"Compression ratio: {compression_ratio:.2f}")

# Line 04 Specify the file to be compressed
# Line 06 Read the contents of the file
# Line 09 Compress the data
# Line 11 Calculate the compression ratio
