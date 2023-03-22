import zlib
import os

filename = "example.txt"

with open(filename, "rb") as f:
    data = f.read()

compressed_data = zlib.compress(data)

compression_ratio = len(compressed_data) / len(data)

weissman_score = (1 - compression_ratio) * 100

decompressed_data = zlib.decompress(compressed_data)

if data == decompressed_data:
    print("Compression successful!")
else:
    print("Compression failed: decompressed data does not match original data.")

print(f"Original file size: {os.path.getsize(filename)} bytes")
print(f"Compressed file size: {len(compressed_data)} bytes")
print(f"Compression ratio: {compression_ratio:.2f}")
print(f"Weissman score: {weissman_score:.2f}%")

"""
Comments:
- The zlib library is used for compression and decompression.
- The specified file is "example.txt", but this can be changed to any file name.
- The contents of the file are read in binary mode using the "rb" mode.
- The compression ratio is calculated as the ratio of compressed size to original size.
- The Weissman score is calculated using the compression ratio.
- The compressed data is decompressed and compared with the original data to check for success.
- The original file size, compressed file size, compression ratio, and Weissman score are printed.
"""
