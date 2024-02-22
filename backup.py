import os
import shutil  # for backup
import datetime  # for time format
import time  # for sleep()
import socket  # for communication
import select  # for nonblocking

# Global Variable
interval = 60
last_backup = ""
src_dir = ""

def print_title():
    """
    Prints title and instruction of the program
    """
    print(
        f'''
    ________________________________________________________________

                        A U T O - B A C K - U P 

                        M I C R O - S E R V I C E

                
    ________________________________________________________________
    '''
    )
    print(
        f'''
    Instruction:
         
        > User enters the "file path" of the data to back up
        > User enters "time interval" desired for backup automation (default is 60s)
        > Microserivce will connect to the client program via Socket
        > Automatic back-up will begin 
        > Microservice will send back the absolute file path of the latest backup
          file path when the client program sends request msg 'Revert'

    '''
    )


def backup():
    """
    Copies the source file to destination with date/time
    """
    global last_backup
    # back up file path(create if does not exist)
    dest_dir = "./backup_file/"
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    # back up file name
    dest_file_name = f'backup_{datetime.datetime.now().strftime("%Y%b%d_%H%M%S")}.json'
    # create back up
    shutil.copy2(src_dir, dest_dir + dest_file_name)
    print(f'"{dest_file_name}" saved successfully.')
    last_backup = dest_file_name
    return


def get_src_dir() -> str:
    """
    Asks user for a valid file location
    """
    while True:
        dir = input("Enter the absolute path where the source file is located: \n")
        if os.path.isfile(dir):
            return dir
        else:
            print("File not found. Please try again.")


def get_interval() -> int:
    """
    Asks user for backup interval
    """
    while True:
        user_interval = input("Enter what interval you want the backup to occur(in seconds): \n")
        if user_interval == "":
            return interval
        elif user_interval.isdigit():
            return int(user_interval)
        else:
            print("Invalid time entered. Please try again.")


def main():
    global src_dir
    global interval

    print_title()
    time.sleep(2)

    # Get a valid file location & time interval from the user
    src_dir = get_src_dir()
    interval = get_interval()
    time.sleep(1)
    print(f"The program will automate back up every {interval} seconds.\n")   
    time.sleep(2)
    
    # Initialize Socket
    server = socket.socket()
    print ("Socket successfully created")
    port = 12345
    server.bind(('', port))
    print(f"Socket binded to {port}")
    server.listen(5)
    print("socket is listening... waiting for client program to start")
    try:
        # accept socket connection
        client, addr = server.accept()
        print(f'Got connection from {addr} \n')
        print("Starting automatic back-up ...")
        time.sleep(1)

        while True:
            #start backup automation
            backup()

            # check if the client requested backup data
            start_time = time.time()
            ready, _, _ = select.select([client], [], [], interval)
            if client in ready: 
                req = client.recv(1024).decode()
                print("         A REQUEST received from client")
                end_time = time.time()

                # check if the request is valid
                if req == "Revert" or req=="revert":    
                    abs_path = os.path.abspath(last_backup)                 # Convert last backup file to absolute path
                    client.send(abs_path.encode())                          # send client the requested data
                    print("         Latest back up sent to the client.")
                else:
                    client.send(f"Invalid request command '{req}' sent.".encode())
                    print("         ** ALERT **: Invalid request received")

                # calculate time pass since last backup
                time_passed = round(end_time - start_time)
                # sleep for the remainder of interval
                time.sleep(interval - time_passed)
            
    except ConnectionResetError:
        print("\n       ** ALERT **: Connection ended by the client, ending the program.\n")
        server.close()
    except ConnectionAbortedError:
        print("\n       ** ALERT **: Connection aborted by the client, ending the program.\n")
        server.close()
    except Exception as e:
        print("\n       ** ALERT **: Something went wrong",e)
    finally:
        server.close()

        
    



if __name__ == "__main__":
    main()
