import socket

#input target
target = input("Enter target IP/domain: ")

#get port range
def get_port_range(): 
    while True:
        try:
            start_port = int(input("Enter the start port range: ")) 
            end_port = int(input("Enter the end port range "))

            #validate the port range
            if start_port <1 or end_port > 65535 or start_port > end_port:
                print("Invalid Port range. try again")
                print("- start port is >=1")
                print("- end point is <= 65535")
                print("- start port <= End Port")
            else:
                return start_port, end_port
        except ValueError:
            print("Invalid input. Please enter a number")

start_port, end_port = get_port_range()

# scan ports
print(f"Scanning taget {target} from port {start_port} to {end_port}")
for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # time out for the connection attempt

        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()
    except KeyboardInterrupt:
        print("\nExiting program.")
        break
    except socket.error:
        print(f"could not connect to {target}")
        break