# Wallpaper Customizer App

## Description
The Wallpaper Customizer App is a Python application that allows users to place orders for custom wallpaper. It features a login system, order form, and cost calculation for different types of wallpaper and additional options.

## Features
- User authentication with a sample employee database.
- Order form for entering customer details.
- Cost calculation for wallpaper based on type, amount, and additional options.
- Generates a receipt with order details.
- Platform-independent file handling for receipt generation.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/wallpaper-customizer-app.git
    ```
2. Navigate to the project directory:
    
3. Run in prefered IDE

## Usage
1. Run the application:
    ```bash
    python main.py
    ```
2. The login window will appear. Use one of the following credentials to log in:
    - Username: `john123`, Password: `password123`
    - Username: `jane456`, Password: `qwerty456`
    - Username: `bob789`, Password: `abcxyz789`
    - Username: `admin`, Password: `admin`

3. After logging in, the main window will appear. Fill in the order form with the customer's details and select the desired wallpaper options.
4. Click "Finalize Order" to calculate the total cost and generate a receipt.

## Code Overview
- `main.py`: Contains the main application logic, including the login system, order form, and cost calculation.

### Main Functions
- `login()`: Authenticates the user based on the provided username and password.
- `open_main_window()`: Opens the main application window after successful login.
- `place_order()`: Opens the order form window for entering customer details.
- `calculate_price()`: Calculates the total cost of the order based on the selected options.
- `on_closing()`: Handles cleanup actions when the application is closed.
- `assistance()`: Displays a message box with assistance contact information.
- `clear()`: Clears the order form fields.
- `change_color(event)`: Changes the wallpaper and text color based on the selected option.
- `temp_text(e)`, `reset_text(e)`, `temp_text2(e)`, `reset_text2(e)`, `temp_text3(e)`, `reset_text3(e)`: Handle placeholder text in the input fields.
- `validate_float(entry)`: Validates if the input is a float.

## Versioning
This project uses file-based versioning for tracking changes in data files and source code.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
- Isak Jonsson
