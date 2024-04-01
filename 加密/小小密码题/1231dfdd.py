import zlib

def decompress_zlib(input_file, output_file):
    with open(input_file, 'rb') as compressed_file, open(output_file, 'wb') as decompressed_file:
        compressed_data = compressed_file.read()
        decompressed_data = zlib.decompress(compressed_data)
        decompressed_file.write(decompressed_data)

input_file = "29.zlib"
output_file = "decompressed.txt"
decompress_zlib(input_file, output_file)