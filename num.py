import keyboard


#decimal to binary
def dectobin(num):
  binary = ""
  while int(num) > 0:
    binary = str((num % 2)) + binary
    num //= 2
  return binary


#dec to hexadec

def dectohexa(num):
  hexadecimal = ""
  hex_chars = "0123456789ABCDEFabcdef"
  while int(num) > 0:
    remainder = int(num) % 16
    hexadecimal = hex_chars[remainder] + hexadecimal
    num //= 16
  return hexadecimal


#dec to octal


def dectooctal(num):
  octal = ""
  while num > 0:
    octal = str(int(num) % 8) + octal
    num //= 8
  return octal


#binary to decimal
def bintodec(binary):
  decimal = 0
  power = 0
  for digit in reversed(binary):
    decimal += int(digit) * (2**power)
    power += 1
  return decimal


#octal to decimal
def octaltodec(octal):
  decimalnum = 0
  power = len(octal) - 1
  for i in octal:
    decimalnum += int(i) * (8**power)
    power -= 1
  return decimalnum


#hexadecimal to decimal
def hexatodec(hexa):
  decimal = 0
  hex_chars = "0123456789ABCDEFabcdef"
  power = 0
  for digit in reversed(hexa):
    decimal += hex_chars.index(digit) * (16**power)
    power += 1
  return decimal


#hexadecimal to octal


def hexatooctal(hexa):
  decimal = hexatodec(hexa)
  octal = dectooctal(decimal)
  return octal


# hexadecimal to binary
def hexatobin(hexa):
  decimal = hexatodec(hexa)
  binary = dectobin(decimal)
  return binary


# octal to binary
def octaltobinary(octal):
  decimal = octaltodec(octal)
  binary = dectobin(decimal)
  return binary


# octal to hexadecimal
def octaltohexa(octal):
  decimal = octaltodec(octal)
  hexa = dectohexa(decimal)
  return hexa


#main loop
key_exit = False
dhob = ['d', 'h', 'o', 'b']
base = 10
a = input("Please enter d for dec, b for binary, o for octal, and h for hexa: ")
if a == "d":
    base = 10
elif a == "h":
    base = 16
elif a == "o":
    base = 8
elif a == "b":
    base = 2



current = []
while not key_exit:
    e = keyboard.read_event()
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == "esc":
            exit()
        else:
            current.append(e.name)
            
        input_string = "".join(current)
        decimal_value = None
        binary_value = None
        octal_value = None
        hex_value = None

        
        if base == 16:
            decimal_value = hexatodec(input_string)
            binary_value = hexatobin(input_string)
            octal_value = hexatooctal(input_string)
            hex_value = input_string
        elif base == 8:
            decimal_value = octaltodec(input_string)
            binary_value = octaltobinary(input_string)
            hex_value = octaltohexa(input_string)
            octal_value = input_string
        elif base == 2: 
            decimal_value = bintodec(input_string)
            octal_value = dectooctal(decimal_value)
            hex_value = dectohexa(decimal_value)
            binary_value = input_string
        else:
            decimal_value = (input_string)
            binary_value = dectobin(decimal_value)
            octal_value = dectooctal(decimal_value)
            hex_value = dectohexa(decimal_value)
            
        print("\rDecimal:", decimal_value, end = " ")
        print("\nHexadecimal:", hex_value, end = " ")
        print("\nOctal:", octal_value, end = " ")
        print("\nBinary:", binary_value, end = " ")
