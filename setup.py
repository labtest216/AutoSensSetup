#!/user/bin

import os




#packges = ['sudo pip install ']

class install_script:

    password = '123qweasd'

    programs = ['sudo apt install git', 'sudo apt install minicom',
                'sudo apt install python-pip', 'sudo apt install python-pip3',
                'sudo apt install gedit', 'sudo apt install gparted'
                'sudo apt install gedit', 'sudo apt install git']

    py_packeges = ['sudo apt install python python-tk', 'sudo apt install python python3-tk',
                   'sudo pip install schedule', 'sudo pip3 install schedule']

    def auto_install(self, programs, password):
        for program in programs:
            debug = os.system('echo %s|sudo -S %s' % (password, program))
            print(str(program))
            print(str(debug))
            print('\n')

    def install_usefull_programs(self):
        self.auto_install(self.programs, self.password)

    def install_python_packeges(self):
        self.auto_install(self.py_packeges, self.password)


a=install_script().install_python_packeges()

