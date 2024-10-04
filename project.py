import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32

ENUM_CURRENT_SETTINGS = -1
CDS_UPDATEREGISTRY = 0x01
CDS_TEST = 0x02

class DEVMODE(ctypes.Structure):
    _fields_ = [
        ('dmDeviceName', ctypes.c_wchar * 32),
        ('dmSpecVersion', ctypes.c_ushort),
        ('dmDriverVersion', ctypes.c_ushort),
        ('dmSize', ctypes.c_ushort),
        ('dmDriverExtra', ctypes.c_ushort),
        ('dmFields', ctypes.c_ulong),
        ('dmPositionX', ctypes.c_long),
        ('dmPositionY', ctypes.c_long),
        ('dmDisplayOrientation', ctypes.c_ulong),
        ('dmDisplayFixedOutput', ctypes.c_ulong),
        ('dmColor', ctypes.c_short),
        ('dmDuplex', ctypes.c_short),
        ('dmYResolution', ctypes.c_short),
        ('dmTTOption', ctypes.c_short),
        ('dmCollate', ctypes.c_short),
        ('dmFormName', ctypes.c_wchar * 32),
        ('dmLogPixels', ctypes.c_ushort),
        ('dmBitsPerPel', ctypes.c_ulong),
        ('dmPelsWidth', ctypes.c_ulong),
        ('dmPelsHeight', ctypes.c_ulong),
        ('dmDisplayFlags', ctypes.c_ulong),
        ('dmDisplayFrequency', ctypes.c_ulong),
        ('dmICMMethod', ctypes.c_ulong),
        ('dmICMIntent', ctypes.c_ulong),
        ('dmMediaType', ctypes.c_ulong),
        ('dmDitherType', ctypes.c_ulong),
        ('dmReserved1', ctypes.c_ulong),
        ('dmReserved2', ctypes.c_ulong),
        ('dmPanningWidth', ctypes.c_ulong),
        ('dmPanningHeight', ctypes.c_ulong),
    ]

def get_display_settings():
    devmode = DEVMODE()
    devmode.dmSize = ctypes.sizeof(devmode)
    if not user32.EnumDisplaySettingsW(None, ENUM_CURRENT_SETTINGS, ctypes.byref(devmode)):
        raise Exception("Nie udało się pobrać ustawień wyświetlania.")
    return devmode

def get_supported_frequencies():
    supported_frequencies = set()
    devmode = DEVMODE()
    devmode.dmSize = ctypes.sizeof(devmode)
    i = 0
    while user32.EnumDisplaySettingsW(None, i, ctypes.byref(devmode)):
        supported_frequencies.add(devmode.dmDisplayFrequency)
        i += 1
    return supported_frequencies

def change_display_frequency(frequency):
    devmode = get_display_settings()
    rounded_frequency = int(round(frequency))
    supported_frequencies = get_supported_frequencies()
    
    if rounded_frequency not in supported_frequencies:
        print(f"Żądana częstotliwość ({rounded_frequency} Hz) nie jest obsługiwana.")
        print(f"Obsługiwane częstotliwości: {sorted(supported_frequencies)}")
        return False

    devmode.dmDisplayFrequency = rounded_frequency
    devmode.dmFields = 0x400000  # DM_DISPLAYFREQUENCY

    result = user32.ChangeDisplaySettingsW(ctypes.byref(devmode), CDS_TEST)
    if result != 0:
        print(f"Test zmiany częstotliwości nie powiódł się. Kod błędu: {result}")
        return False

    result = user32.ChangeDisplaySettingsW(ctypes.byref(devmode), CDS_UPDATEREGISTRY)
    if result == 0:
        new_frequency = get_display_settings().dmDisplayFrequency
        print(f"Zmieniono częstotliwość na {new_frequency} Hz.")
        return True
    else:
        print(f"Nie udało się zmienić częstotliwości odświeżania. Kod błędu: {result}")
        return False

if __name__ == "__main__":
    desired_frequency = 59
    change_display_frequency(desired_frequency)