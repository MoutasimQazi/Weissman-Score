# Weissman-Score
In This Repositary I am Writing My Self Satisfaction Project #1

This Is Compression Score Mesuring Code Inspired By Silicon Valley A Famous TV series
The Weissman score is a fictional metric from Silicon Valley that represents the efficiency of a compression algorithm. While it is not a real-life metric, we can create a program to measure the efficiency of a compression algorithm and use it as a proxy for the Weissman score.

There are many compression algorithms available, each with its own strengths and weaknesses. Some popular algorithms include:

DEFLATE (used by gzip)
LZ77 and LZ78 (used by zip)
LZW (used by GIF images)
Brotli
Zstandard
Snappy

To create a program that measures the efficiency of a compression algorithm, we can compare the size of the compressed file to the size of the original file. The closer the compressed file size is to the original file size, the more efficient the compression algorithm.

In Sample.py Python code that uses the zlib library to compress a file and calculate the compression ratio The code reads the contents of a file named 'example.txt', compresses the data using the zlib library, and calculates the compression ratio. The output of this code will show the original file size, the compressed file size, and the compression ratio.

You can try running this code with your own files and see how the compression ratio varies with different compression algorithms.


To ensure that the compressed data contains all of the data from the original file, we can use a technique called decompression. Decompression is the process of reversing the compression process to recreate the original data.

In Python, we can use the zlib library to decompress the compressed data.  main.py an updated version of the previous code that also includes decompression with printing of weisseman score.
Using the formula used in the Silicon Valley TV show, which is:

Weissman score = (1 - Compressed size / Original size) * 100%

Using this formula, we can calculate the Weissman score for a file that is 1 MB in size and is compressed to 0.1 MB:

Weissman score = (1 - 0.1 MB / 1 MB) * 100%
Weissman score = 90%

So the Weissman score for this scenario would be 90%. This means that the compression algorithm was able to compress the file by 90% of its original size, which is a fairly high compression ratio.

And main.py works As This code first calculates the compression ratio and then uses it to calculate the Weissman score. It then decompresses the compressed data and checks if the decompressed data matches the original data. Finally, it prints the original file size, compressed file size, compression ratio, and Weissman score.

You can try running this code with your own files and see how the Weissman score varies with different compression algorithms.
