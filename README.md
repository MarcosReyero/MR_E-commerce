# E-Commerce Project

## Overview

E-Commerce Project is a full-featured online store application built using Django, Python, and modern web technologies. This project demonstrates a complete e-commerce solution, including user authentication, product management, and a responsive user interface.

## Features

- **User Authentication**: Register, login, and manage user accounts with custom authentication and authorization.
- **Product Management**: Add, edit, and view products with support for categories and images.
- **Shopping Cart**: Add products to a cart, view cart contents, and proceed to checkout.
- **Responsive Design**: Mobile-friendly layout using Bootstrap and custom CSS.
- **Image Handling**: Support for image uploads and dynamic display using Pillow.
- **Custom Admin Panel**: Manage products and categories through a custom-built admin interface.

## Technologies

- **Backend**: Django 5.0.7, Python 3.12.4
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite3
- **Image Processing**: Pillow
- **API**: Django REST Framework (DRF)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/e-commerce.git
   cd e-commerce
Create a Virtual Environment


python -m venv .venv
Activate the Virtual Environment

On Windows:
.venv\Scripts\activate

On macOS/Linux:
source .venv/bin/activate

Install Dependencies

pip install -r requirements.txt

Apply Migrations

python manage.py migrate
Run the Development Server
python manage.py runserver
The application should now be running at http://127.0.0.1:8000.

Usage
Access the Admin Panel: Navigate to /admin/ and log in with admin credentials to manage products and categories.
Add Products: Use the /add-product/ page to add new products to the store.
View Products: Browse products through the main home page or category pages.
Configuration
Static Files: Ensure that static files are correctly served in development mode. See STATIC_URL and STATICFILES_DIRS in settings.py.
Media Files: Ensure that media files are correctly served. See MEDIA_URL and MEDIA_ROOT in settings.py.
Contributing
Contributions are welcome! Please submit a pull request with detailed information about your changes. Make sure to follow the project's code style and include relevant tests.


Contact
For questions or feedback, please reach out to marcos.reyero31@gmail.com.
