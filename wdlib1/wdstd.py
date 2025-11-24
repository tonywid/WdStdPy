def get_inputstring(prompt, default=''):
    if prompt != '':
        print('<?>', prompt)
    inputtext = input()
    if len(inputtext) == 0:
        return default
    else:
        return inputtext


# input expects a valid filepath
# when an invalid filepath is entered
# the dialog offers a retry
# when retry is selected the input is repeated
def get_valid_filename (prompt, default=''):
    import os
    filefound = False
    while not filefound:
        inputtext = get_inputstring(prompt, default)
        if len(inputtext) > 0:
            if os.path.isfile(inputtext):
                return inputtext
        print ('<!> filename not valid or file does not exist')
        retrytext = input('<?> r=retry (anything else is quit)\n')
        if retrytext != 'r':
            break;
    return None


# input expects a valid folderpath
# when an invalid folderpath is entered
# the dialog offers a retry
# when retry is selected the input is repeated
def get_valid_foldername (prompt, default=''):
    import os
    filefound = False
    while not filefound:
        inputtext = get_inputstring(prompt, default)
        if len(inputtext) > 0:
            if os.path.isdir(inputtext):
                return inputtext
        print ('<!> filename not valid or file does not exist')
        retrytext = input('<?> r=retry (anything else is quit)\n')
        if retrytext != 'r':
            break;
    return None


# das ist nur experimentel
def check_is_file (filepath):
    import os

# os.path.isfile(path)
# os.path.isdir(path)
# os.path.exists(path)

    # Check if the file exists
    if os.path.isfile(filepath):
        print("The file exists.")
        return True
    else:
        print("The file does not exist.")
        return False


def is_float_de(string):
    # -1.234,56 is converted into -1_234.56)
    # leading zeros are not considered
    float_value = string.replace('.', '_').replace(',','.')
    try:
        float(float_value)
        return True
    except ValueError:
        return False


def get_float_de(string):
    # 1.234,56 is converted into 1_234.56)
    float_value = float(string.replace('.', '_').replace(',','.'))
    return float(float_value)


def is_int(string):
    # leading zeros are considered as part of a string
    if string != "0" and string[0] == '0':
        return False
    try:
        int(string)
        return True
    except ValueError:
        return False


def get_int(string):
    return int(string)
