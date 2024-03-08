# RLE Image Encoding and Decoding
Image encoding console application written in python

> RLE: Repeat Length Encoder

> This project implements routines to encode and decode data for images using run-length encoding (RLE). RLE is a form of lossless compression used in many industry applications, including imaging. It is intended to take advantage of datasets where elements (such as bytes or characters) are repeated several times in a row in certain types of data (such as pixel art in games).

## Features

- Encoding and decoding of raw image data using RLE
- Conversion between data and strings (hexadecimal and human-readable RLE format)
- Display of image information and encoded/decoded data

## Requirements

- Python 3.x
- ConsoleGfx library (provided)

## Usage

The project provides a standalone mode with a menu interface when run as the main program. The menu allows users to:

1. Load an image file
2. Load the test image
3. Read RLE string in hexadecimal notation with delimiters
4. Read RLE hexadecimal string without delimiters
5. Read flat (raw) data hexadecimal string
6. Display the current image
7. Display the RLE string (human-readable format with delimiters)
8. Display the RLE hexadecimal data (without delimiters)
9. Display the flat (raw) hexadecimal data (without delimiters)

## Class Methods

The project includes the following class methods:

1. `to_hex_string(data)`: Translates data (RLE or raw) to a hexadecimal string without delimiters.
2. `count_runs(flat_data)`: Returns the number of runs of data in an image data set.
3. `encode_rle(flat_data)`: Returns the encoding (in RLE) of the raw data passed in.
4. `get_decoded_length(rle_data)`: Returns the decompressed size of RLE data.
5. `decode_rle(rle_data)`: Returns the decoded data set from RLE encoded data.
6. `string_to_data(data_string)`: Translates a hexadecimal string into byte data (can be raw or RLE).
7. `to_rle_string(rle_data)`: Translates RLE data into a human-readable representation with delimiters.
8. `string_to_rle(rle_string)`: Translates a human-readable RLE string (with delimiters) into RLE byte data.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
