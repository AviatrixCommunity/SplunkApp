#!/usr/bin/env python
import csv
import sys
import socket

#Based on etc/system/bin/external_lookup.py

# Given a service name, find the port
def serv_to_port(dst_servname):
    # Not needed, not implemented
    return ''

# Given a port, find the service name
def port_to_serv(dst_port):
    try:
        dst_servname = socket.getservbyport(int(dst_port))
        if dst_servname=='domain':
            dst_servname='dns'
        return dst_servname.upper()
    except:
        return str(dst_port)

def main():
    if len(sys.argv) != 3:
        print "Usage: python getServName.py [port field] [service name field]"
        sys.exit(1)

    dst_port = sys.argv[1]
    dst_servname = sys.argv[2]

    infile = sys.stdin
    outfile = sys.stdout

    r = csv.DictReader(infile)
    header = r.fieldnames

    w = csv.DictWriter(outfile, fieldnames=r.fieldnames)
    w.writeheader()

    for result in r:
        if result[dst_port] and result[dst_servname]:
            # both fields were provided, just pass it along
            w.writerow(result)

        elif result[dst_port]:
            # port was provided, get service name
            result[dst_servname] = port_to_serv(result[dst_port])
            if result[dst_servname]:
                w.writerow(result)
            
        elif result[dst_servname]:
            # service name was provided, get port number
            result[dst_port] = serv_to_port(result[dst_servname])
            if result[dst_port]:
                w.writerow(result)

main()
