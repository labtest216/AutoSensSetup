#!/user/bin

import os




#packges = ['sudo pip install ']

class install_script:

    password = ' '
    
    crypto = ['sudo apt install ocl-icd-opencl-dev','sudo apt install curl',
              'sudo apt install build-essential cmake git libgit2-dev clang libncurses5-dev libncursesw5-dev zlib1g-dev pkg-config libssl-dev llvm']
    programs = ['sudo apt install git', 'sudo apt install minicom',
                'sudo apt install python-pip', 'sudo apt install python-pip3',
                'sudo apt install gedit', 'sudo apt install gparted'
                'sudo apt install gedit', 'sudo apt install git'
		'sudo apt install speedtest-cli']

    py_packeges = ['sudo apt install python python-tk', 'sudo apt install python python3-tk',
                   'pip install schedule', 'pip3 install schedule']

    def auto_install(self, programs, password):
        for program in programs:
            print('Out put for '+str(program) + ':')
            debug = os.system('echo %s|sudo -S %s' % (password, program))
            print('return='+str(debug))
            print('\n\n\n')


    def install_usefull_programs(self):
        self.auto_install(self.programs, self.password)

    def install_python_packeges(self):
        self.auto_install(self.py_packeges, self.password)


a=install_script().install_python_packeges()

