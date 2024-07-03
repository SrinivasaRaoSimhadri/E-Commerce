# E-Commerce Website

Welcome to my E-Commerce website project built using Django! This project combines modern web development techniques with robust backend functionality to create a seamless online shopping experience.

## Features

- **Dynamic Product Listings**: Utilizes the Fakestore API to fetch and display a wide range of products.
- **Add to Cart**: Allows users to add products to their cart, update quantities, and manage selections.
- **User Authentication**: Secure login and logout functionality with user registration, password encryption, and session management.
- **Address Management**: Enables users to save and manage their delivery addresses for a smooth checkout process.
- **Payment Integration**: Integrates Razorpay for secure and efficient payment processing.
- **Order Summary**: Provides a detailed summary of the user's purchase, including product details, prices, delivery address, and payment confirmation.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **API**: Fakestore API
- **Payment Gateway**: Razorpay

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SrinivasaRaoSimhadri/E-Commerce.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd E-Commerce
    ```

3. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Open your browser and navigate to** `http://127.0.0.1:8000/` to view the website.
2. **Register or log in** to access user-specific features.
3. **Browse products**, add them to your cart, and proceed to checkout.
4. **Enter your delivery address** and make a payment using Razorpay.
5. **View the order summary** after completing your purchase.

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements.

## License

This project is licensed under the MIT License.

---

Thank you for checking out my project! I hope you find it useful and informative.

