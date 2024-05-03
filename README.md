# Late Pay Notify

Brief description or summary of your project.
Table of Contents

- [Installation](#Installation)

## Installation
1. **Clone this project:**

```bash
git clone https://github.com/esperanca-leonardo/late-pay-notify.git
```

2. **Navigate to the project directory:**

```bash
cd late-pay-notify
```

3. **Create and activate a virtual environment:**

    First, install the virtualenv library:

    ```bash
    pip install virtualenv
    ```

    Then, create a virtual environment named `venv`:

    ```bash
    virtualenv venv
    ```

    3.1. **Activate the virtual environment:**
    
    - Linux or macOS:
    
        ```bash
        source venv/bin/activate
        ```
    
    - Windows:
    
        ```bash
        venv\Scripts\activate
        ```

5. **Install dependencies:**

Make sure you have Python and pip installed on your system. Then, install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

5. **Setting up Gmail authentication:**

    This project uses Gmail for sending emails. You will need to generate an app password for your Gmail account. Follow the instructions [here](https://support.google.com/accounts/answer/185833?hl=en) to generate an app password.

6. **Create a .env file:**

Create a file named `.env` in the project directory and add the following variables:

```plaintext
MAIL=your_email
PASSWORD=your_app_password
```

7. **Run the project:**

Execute the project using the following command:

```bash
python main.py
```