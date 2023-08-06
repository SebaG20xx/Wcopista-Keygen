import ctypes

def get_serial_number(str_drive):
    MAX_PATH = 260
    volume_name_buffer = ctypes.create_unicode_buffer(MAX_PATH)
    file_system_name_buffer = ctypes.create_unicode_buffer(MAX_PATH)
    serial_number = ctypes.c_long()
    max_component_length = ctypes.c_ulong()
    file_system_flags = ctypes.c_ulong()

    res = ctypes.windll.kernel32.GetVolumeInformationW(
        ctypes.c_wchar_p(str_drive),
        volume_name_buffer,
        MAX_PATH,
        ctypes.byref(serial_number),
        ctypes.byref(max_component_length),
        ctypes.byref(file_system_flags),
        file_system_name_buffer,
        MAX_PATH
    )

    return serial_number.value if res != 0 else 0

def calculate_activation_code(serial_number):
    sCad = ""
    nombre = str(serial_number).strip()

    for char in nombre:
        sCad += format(ord(char), "03")

    # Devolver el código de activación
    return sCad

def test_activation_code_calculation():
    str_drive = "C:\\"
    serial_number = get_serial_number(str_drive) 
    activation_code = calculate_activation_code(serial_number)

    print("Código de activación:", activation_code)

if __name__ == "__main__":
    test_activation_code_calculation()
