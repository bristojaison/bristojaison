#!usr/bin/env python3

from socket import *
import argparse
def honey(ip_addr):
    port=2121
    BANNER="220 ProFTPD 1.2.8 Server\nenter_username: "+"\n"+"username"
    try:
        get_socket_con=socket(AF_INET, SOCK_STREAM)
        get_socket_con.bind((ip_addr, port))
        get_socket_con.listen()
        while 1:
            client_con,client_addr=get_socket_con.accept()
            print("Visitor found [{}]".format(client_addr[0]))
            client_con.send(BANNER.encode('utf-8'))
            data= client_con.recv(1024)
            print(data)
            client_con.close()
    except:
        print("process terminated")
def main():
    parser=argparse.ArgumentParser()
    group=parser.add_mutually_exclusive_group()
    group.add_argument("-v","--verbose", action="store_true")
    group.add_argument("-q","--quiet", action="store_true")
    parser.add_argument("ip",help="ip addr of server")
    parser.add_argument("-o","--output",help="Output file",action="store_true")

    args=parser.parse_args()
    result=honey(args.ip)


    if args.verbose:
        print(str(args.ip)+"was been attacked:--> "+str(result))
    elif args.quiet:
        print(result)

    if args.output:
        f=open("ftphoney.txt", "a")
        f.write(data+'\n')
    print(result)
if __name__=="__main__":
    main()
