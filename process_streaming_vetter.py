#Imports

import csv
import socket
import time
import random

# Constants
HOST = "localhost"
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)
INPUT_FILE_NAME = "BigmacPrice.csv"
OUTPUT_FILE_NAME = "out9.txt"

# Function to prepare message from row
def prepare_message_from_row(row):
    return f"{','.join(row)}\n".encode()

# Function to stream data
def stream_data(input_file_name, output_file_name, address_tuple):
    with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
        reader = csv.reader(input_file)
        header = next(reader)
        output_file.write(','.join(header) + '\n')

        sock_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        for row in reader:
            message = prepare_message_from_row(row)
            sock_object.sendto(message, address_tuple)
            output_file.write(','.join(row) + '\n')
            time.sleep(random.uniform(1, 3))  

if __name__ == "__main__":
    try:
        print("Starting data streaming.")
        stream_data(INPUT_FILE_NAME, OUTPUT_FILE_NAME, ADDRESS_TUPLE)
        print("Streaming complete!")
    except Exception as e:
        print(f"An error occurred: {e}")
