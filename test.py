from rle_program import *

print(to_hex_string([3, 15, 6, 4]) == "3f64")
print(count_runs(
    [4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8,
     7]))
print(encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]))
print(encode_rle(
    [4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8,
     7]))
print(get_decoded_length([3, 15, 6, 4]))
print(string_to_data("3f64"))
print(decode_rle([3,15,6,4]))
print(to_rle_string([15,15,6,4]))
