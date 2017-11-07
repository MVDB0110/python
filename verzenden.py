import socket

def stuur_bericht(bericht):
    s = socket.socket()
    s.bind(('', 12345))
    s.listen(5)

    while True:
        c, addr = s.accept()
        print('Ik heb verbinding met: ', addr)
        c.send(bericht)
        c.close()
        break