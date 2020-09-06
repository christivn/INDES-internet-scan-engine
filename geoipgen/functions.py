def ips(start, end):
    import socket, struct
    end_host=end
    start = struct.unpack('>I', socket.inet_aton(start))[0]
    end = struct.unpack('>I', socket.inet_aton(end))[0]
    arr=[socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end)]
    arr.append(end_host)
    return arr