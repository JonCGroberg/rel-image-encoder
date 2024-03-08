from console_gfx import ConsoleGfx


def to_hex_string(data: list[int]) -> str:
    hex_digits = "0123456789abcdef"  # the index of each char can be used to convert from decimal to hex
    result = ""

    for digit in data:
        result += hex_digits[int(digit)]  # 15 should result in the 15th char (F) in the list
    return result


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


def get_decoded_length(rle_data: list[int]) -> int:  # sums every other element starting at 0,2,4,6...
    total = 0
    for i in range(0, len(rle_data), 2):
        total += rle_data[i]
    return total


def decode_rle(rle_data: list[int]) -> list[int]:
    arr = []
    for i in range(0, len(rle_data), 2):  # goes over every 2 elements
        count = rle_data[i]
        elem = rle_data[i + 1]

        for j in range(count):
            arr.append(elem)
    return arr


def string_to_data(data_string: str) -> list[int]:
    hex_digits = "0123456789abcdef"  # the index of each char can be used to convert from decimal to hex
    arr = []

    for digit in data_string:
        arr.append(hex_digits.index(digit))

    return arr


# run length is in decimal, run value is in hexadecimal with ':' as delimiter
def to_rle_string(rle_data: list[int]) -> str:
    string = ""

    for i in range(0, len(rle_data), 2):
        delimiter = "" if i == len(rle_data)-2 else ":"  # if it's the last two elements make delimiter is blank
        run_bin_str = str(rle_data[i])
        value_hex_str = to_hex_string([(rle_data[i + 1])])  # converts to hex string by placing it in an empty array
        string += run_bin_str + value_hex_str + delimiter

    return string


if __name__ == '__main__':
    # Welcome Message
    # Display spectrum image message
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    image_data = None

    while True:
        # Show RLE MENU
        print("\nRLE Menu")
        print("--------")
        print(
            "0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hext String\n5. Read Data Hex "
            "String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data"
            "\n9. Display Hex Flat Data\n")

        # PROMPT USER for option
        selected_option = int(input("Select a Menu Option: "))

        if selected_option == 0:
            exit()
        elif selected_option == 1:
            file_name = input("Enter name of file to load: ")
            image_data = ConsoleGfx.load_file(file_name)
            print("Loaded file: " + file_name + "\n")
        elif selected_option == 2:
            image_data = ConsoleGfx.test_image
        elif selected_option == 6:
            ConsoleGfx.display_image(image_data)
