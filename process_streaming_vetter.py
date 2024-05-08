#Imports - Nic Vetter

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
# No logging needed because I am writing the streamed data to the output file
def stream_row(input_file_name, output_file_name, address_tuple):
    with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
        reader = csv.reader(input_file)
        #Creating a csv reader. I am also going to account for the header and skip it
        header = next(reader)
        #separating the attributes by comma's and adding new lines
        output_file.write(','.join(header) + '\n')
        
        # Using my Contructor to make a socket obj
        # assigning variable name "sock_object"
        sock_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        for row in reader:
            message = prepare_message_from_row(row)
            sock_object.sendto(message, address_tuple)
            output_file.write(','.join(row) + '\n')
            time.sleep(random.uniform(1, 3))  
# Calling the stream row function
if __name__ == "__main__":
    try:
        print("Data Currently Streaming.")
        stream_row(INPUT_FILE_NAME, OUTPUT_FILE_NAME, ADDRESS_TUPLE)
        print("Stream Complete!")
    except Exception as e:
        print(f"An error occurred: {e}")
