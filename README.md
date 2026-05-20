# pyterappeng (Python Terminal Application Engine)

pyterappeng is an ultra-lightweight engine for creating text and terminal applications in Python. It allows you to initialize text buffers and update the screen content.

## Features

* Simple start
* Dynamic buffer
* Built-in update cycle

## Installation

Copy the pyterappeng.py file into the root directory of your project.

## Usage

The engine works on a buffering principle: you initialize lines, fill them with content, and render them.

```python
import pyterappeng

pyterappeng.create_lines(2)

pyterappeng.lines[0] = "Hello, Terminal!"
pyterappeng.lines[1] = "This is line number two."

pyterappeng.update()
```

## API Documentation

### create_lines(lines_count: int)
Creates an internal buffer for storing the lines of your application. lines_count is the total number of lines to display.

### lines: list
A global list of application lines. Modify the elements directly using indexes from 0 to lines_count - 1.

### update()
Prints all lines from the lines list to the console.

## Roadmap

* Add automatic console clearing before each update call
* Implement keypress handling for user input
* Add support for text coloring via ANSI codes

## License

This project is licensed under the GNU General Public License (GPL).
