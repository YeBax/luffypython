# -*- coding: utf-8 -*-
from .main import FTPserver


class ManagementTool:
    '''
    负责对用户输入的指令进行解析并调用相应模块处理
    '''

    def __init__(self, sys_argv):
        self.sys_argv = sys_argv
        self.verify_argv()

    def verify_argv(self):
        # 验证指令是否合法
        if len(self.sys_argv) < 2:
            self.help_msg()
        cmd = self.sys_argv[1]
        if not hasattr(self, cmd):
            print('invalid argument!')
            self.help_msg()


    def help_msg(self):
        msg = '''
        start       start FTP server
        stop        stop FTP server
        restart     restart FTP server
        createuser  username create a ftp user
        '''
        exit(msg)

    def execute(self):
        # 解析执行指令
        cmd = self.sys_argv[1]
        func = getattr(self, cmd)
        func()

    def start(self):
        # start ftp server
        server = FTPserver(self)
        server.run_forever()



    def stop(self):
        pass

    def createuser(self):
        pass




