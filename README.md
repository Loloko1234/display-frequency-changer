# Display Frequency Changer

This Python script allows users to change the display refresh rate (frequency) on Windows systems using the Windows API through ctypes.

## Features

- Retrieve current display settings
- Get a list of supported display frequencies
- Change the display frequency to a specified value

## Requirements

- Windows operating system
- Python 3.x

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/display-frequency-changer.git
   ```

2. Navigate to the project directory:
   ```
   cd display-frequency-changer
   ```

3. Run the script:
   ```
   python project.py
   ```

   By default, the script attempts to change the display frequency to 59 Hz. You can modify the `desired_frequency` variable in the `__main__` block to change this value.

## Functions

- `get_display_settings()`: Retrieves current display settings
- `get_supported_frequencies()`: Returns a set of supported display frequencies
- `change_display_frequency(frequency)`: Attempts to change the display frequency to the specified value

## Warning

Changing display settings can potentially cause system instability or display issues. Use this script at your own risk and ensure you have a way to revert changes if needed.

## License

This project is open source.

## Contributing

Contributions, issues, and feature requests are welcome.

## Author

Maciej Kowalczyk
