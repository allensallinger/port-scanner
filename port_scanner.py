import socket
import sys
from datetime import datetime

def main():
  print "port scanner..."
  server = raw_input("Please input the name of the server you want to scan: ")
  server_ip = socket.gethostbyname(server)

  port_to_test = input("Please enter a port to test: ")

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_response = sock.connect_ex((server_ip, port_to_test))

  if(server_response == 0):
    print "Port {} is open".format(port_to_test)

  sock.close()


if __name__ == "__main__":
	main()
