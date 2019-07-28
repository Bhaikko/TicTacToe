import cx_Freeze

Executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="TicTacToe",
    options={"build_exe":{"packages":["pygame"]}},

    executables=Executables 

)