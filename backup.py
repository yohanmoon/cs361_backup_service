import os
import shutil  # for backup
import datetime  # for time format
import socket  # for communication
import select  # for nonblocking

# Global Variable
interval = 60
last_backup = None
src_dir = r"C:\Users\hamme\Desktop\Software Engineering 1\Idea Board Project\Backups\ideaboard_backup.json"
dest_dir = "./backup_file/"

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


def backup():
    """
    Copies the source file to destination with date/time
    """
    global last_backup
    # back up file path(create if does not exist)   
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    # back up file name
    dest_file_name = f'backup_{datetime.datetime.now().strftime("%Y%b%d_%H%M%S")}.json'
    # create back up
    shutil.copy2(src_dir, dest_dir + dest_file_name)
    print(f'"{dest_file_name}" saved successfully.')
    last_backup = dest_file_name
    return


def get_src_dir():
    """
    verify for a valid file location
    """
    while True: 
        if os.path.isfile(src_dir):
            return
        else:
            print("File not found. Please try again.")


def main():
    print_title()
   
    # Initialize Socket
    server = socket.socket()
    print ("Socket successfully created")
    port = 12345
    server.bind(('', port))
    print(f"Socket binded to {port}")
    server.listen(5)
    print("socket is listening... waiting for client program to start")

    # accept socket connection
    client, addr = server.accept()
    print(f'Got connection from {addr} \n')
    # validate file location
    get_src_dir()

    while True:
        try:
            ready, _, _ = select.select([client], [], [], interval)

            if client in ready: 
                req = client.recv(1024).decode()
                print("A REQUEST received from client")
          
                # check the content of the request
                if req == "Backup" or req=="backup":
                    backup()
                    client.send("Backup completed".encode())
                elif req == "Revert" or req=="revert":
                    if last_backup:    
                        abs_path = os.path.abspath(last_backup)                 # Convert last backup file to absolute path
                        client.send(abs_path.encode())                          # send client the requested data
                        print("Latest back up sent to the client.")
                    else:
                        client.send("No backup found.".encode())
                elif req == "Exit" or req=="exit":
                    print("Client requested to end connection")
                    break
                else:
                    client.send(f"Invalid request command '{req}' sent.".encode())
                    print("Invalid request received")

        except ConnectionResetError:
            print("\n       ** ALERT **: Connection ended by the client, ending the program.\n")
        except ConnectionAbortedError:
            print("\n       ** ALERT **: Connection aborted by the client, ending the program.\n")
        except Exception as e:
            print("\n       ** ALERT **: Something went wrong",e)
        finally:
            server.close()

if __name__ == "__main__":
    main()
