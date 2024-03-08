from console_gfx import ConsoleGfx
HEX_DIGITS = "0123456789abcdef"

# to_hex_string([3, 15, 6, 4]) yields string "3f64"
def to_hex_string(data: list[int]) -> str:
    return "".join(HEX_DIGITS[val] for val in data)


# count_runs([15, 15, 15, 4, 4, 4, 4, 4, 4]) yields integer 2.
def count_runs(flat_data: list[int]) -> int:
    count = 0
    running_count = 0  # this gets reset everytime a run ends
    current = None

    for element in flat_data:  # for each element, check if it is a new number
        if running_count >= 15:  # runs have a limit of 15
            count += 1
            running_count = 0
        if element != current:
            count += 1
            running_count = 0
            current = element
        else:  # else they are equal
            running_count += 1

    return count


# encode_rle([15, 15, 15, 4, 4, 4, 4, 4, 4]) yields list [3, 15, 6, 4]
def encode_rle(flat_data: list[int]) -> list[int]:
    running_count = 0
    current = flat_data[0]  # starts as the first element
    arr = []

    def append():
        arr.append(running_count)
        arr.append(current)

    for i in range(len(flat_data)):  # uses a range because we need the check if it's the last index
        element = flat_data[i]  # grab the current elem

        if running_count >= 15:
            append()
            running_count = 0
        if element != current:  # if a new run starts or last element is hit add to arr
            append()
            running_count = 1  # reset the count
            current = element
        else:
            running_count += 1

        if i == len(flat_data) - 1:
            append()

    return arr


# get_decoded_length([3, 15, 6, 4]) yields integer 9
def get_decoded_length(rle_data: list[int]) -> int:  # sums every other element starting at 0,2,4,6...
    total = 0
    for i in range(0, len(rle_data), 2):
        total += rle_data[i]
    return total


# decode_rle([3, 15, 6, 4]) yields list [15, 15, 15, 4, 4, 4, 4, 4, 4]
def decode_rle(rle_data: list[int]) -> list[int]:
    arr = []
    for i in range(0, len(rle_data), 2):  # goes over every 2 elements
        count = rle_data[i]
        elem = rle_data[i + 1]

        for j in range(count):
            arr.append(elem)
    return arr


# string_to_data ("3f64") yields list [3, 15, 6, 4].
def string_to_data(data_string: str) -> list[int]:
    arr = []

    for digit in data_string:
        arr.append(HEX_DIGITS.index(digit))

    return arr


# to_rle_string([15, 15, 6, 4]) yields string "15f:64"
# run length is in decimal, run value is in hexadecimal with ':' as delimiter
def to_rle_string(rle_data: list[int]) -> str:
    string = ""

    for i in range(0, len(rle_data), 2):
        delimiter = "" if i == len(rle_data) - 2 else ":"  # if it's the last two elements make delimiter is blank
        length: str = str(rle_data[i])
        value: str = to_hex_string([(rle_data[i + 1])])  # converts to hex string by placing it in an empty array
        string += length + value + delimiter

    return string


# string_to_rle("15f:64") yields list [15, 15, 6, 4]
# Translates a string in human-readable RLE format (with delimiters, binary_hex:binary_hex:...) into RLE byte data.
def string_to_rle(data_string: str) -> list[int]:
    data_string_pairs = data_string.split(":")
    array = []

    for pair in data_string_pairs:
        decimal_end_index = 2 if len(pair) == 3 else 1
        hex_index = len(pair) - 1

        length: str = pair[0:decimal_end_index]  # first 1 or 2 elements and also the run length
        value: str = pair[hex_index]  # last element and also run value

        array.append(int(length))
        array.append(int(string_to_data(value)[0]))

    return array


if __name__ == '__main__':
    # Welcome Message
    # Display spectrum image message
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image: ")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    image_data = None

    while True:
        # Show RLE MENU
        print("RLE Menu")
        print("--------")
        print(
            "0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex String\n5. Read Data Hex "
            "String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data"
            "\n9. Display Hex Flat Data\n")

        # PROMPT USER for option
        selected_option = int(input("Select a Menu Option: "))

        if selected_option == 0:
            break
        elif selected_option == 1:
            file_name = input("Enter name of file to load: ")
            image_data = ConsoleGfx.load_file(file_name)
        elif selected_option == 2:
            image_data = ConsoleGfx.test_image
            print("Test image data loaded.")
        elif selected_option == 3:
            user_input = input("Enter an RLE string to be decoded: ")
            image_data = decode_rle(string_to_rle(user_input))
        elif selected_option == 4:
            user_input = input("Enter the hex string holding RLE data: ")
            image_data = decode_rle(string_to_data(user_input))
        elif selected_option == 5:
            user_input = input("Enter the hex string holding flat data: ")
            image_data = string_to_data(user_input)
        elif selected_option == 6:
            print("Displaying image... ")
            ConsoleGfx.display_image(image_data)
        elif selected_option == 7:
            print("RLE representation: " + to_rle_string(encode_rle(image_data)))
        elif selected_option == 8:
            print("RLE hex values: " + to_hex_string(encode_rle(image_data)))
        elif selected_option == 9:
            print("Flat hex values: " + "".join(
                map(lambda x: str(x), image_data)))  # turns each element into a str and adds them
