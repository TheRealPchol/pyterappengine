import os
lines = []
def create_lines(lines_count):
    global lines
    lines = [''] * lines_count
def update():
    os.system('clear')
    for line in lines:
        print(line)
