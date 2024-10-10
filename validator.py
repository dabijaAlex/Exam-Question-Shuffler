# Copyright 2024 Dabija Alexandru

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and 
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies 
# or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from PySide6.QtGui import QValidator

class FloatValidator(QValidator):
    def validate(self, input_str, pos):
        if input_str == "":
            return QValidator.Intermediate, input_str, pos

        try:
            value = float(input_str)
        except ValueError:
            return QValidator.Invalid, input_str, pos

        # Check if the number ends in .0 or .5
        if value * 10 % 5 == 0:
            return QValidator.Acceptable, input_str, pos
        else:
            return QValidator.Invalid, input_str, pos

    def fixup(self, input_str):
        try:
            value = float(input_str)
            # Round to nearest .0 or .5
            rounded_value = round(value * 2) / 2
            return str(rounded_value)
        except ValueError:
            return input_str