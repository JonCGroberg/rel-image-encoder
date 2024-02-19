from console_gfx import ConsoleGfx

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
            print("Loaded file: " + file_name+"\n")
        elif selected_option == 2:
            image_data = ConsoleGfx.test_image
        elif selected_option == 6:
            ConsoleGfx.display_image(image_data)
