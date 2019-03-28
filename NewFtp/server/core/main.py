# -*- coding: utf-8 -*-
import socket
from conf import settings


class FTPserver:
    '''
    处理与客户端所有的交互的socket server
    '''

    def __init__(self, mangement_instance):
        self.management_instance = mangement_instance
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((settings.HOST, settings.PORT))
        self.sock.listen(settings.MAX_SOCKET_LISTEN)

    def run_forever(self):
        # 启动socket server
        print("starting NewFtp server on %s:%s".center(50, '-') %
              (settings.HOST, settings.PORT))
        self.request, self.addr = self.sock.accept()
        print("got a new connection from %s" % self.addr)
        self.handle()

    def handle(self):
        # 处理与用户的所有指令交互
        data = self.request.recv(1024)
        if not data:
            self.request.close()


