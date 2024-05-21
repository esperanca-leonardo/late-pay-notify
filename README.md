# 📨 Late Pay Notify

Late Pay Notify is a tool that automates the process of notifying customers about overdue payments by sending email reminders.

## 📑 Table of Contents
- [Key Features](#-key-features)
- [How It Works](#-how-it-works)
- [Tools and Technologies Used](#-tools-and-technologies-used)
- [Installation Instructions](#-installation-instructions)
  - [Clone this project](#1-clone-this-project)
  - [Navigate to the project directory](#2-navigate-to-the-project-directory)
  - [Create and activate a virtual environment](#3-create-and-activate-a-virtual-environment)
    - [First, install the virtualenv library](#31-first-install-the-virtualenv-library)
    - [Then, create a virtual environment named venv](#32-then-create-a-virtual-environment-named-venv)
      - [Linux or macOS](#linux-or-macos)
      - [Windows](#windows) 
    - [Activate the virtual environment](#33-activate-the-virtual-environment)
      - [Linux or macOS](#linux-or-macos-1)
      - [Windows](#windows-1)
  - [Install dependencies](#4-install-dependencies)
  - [Setting up Gmail authentication](#5-setting-up-gmail-authentication)
  - [Create a .env file](#6-create-a-env-file)
  - [Run the project](#7-run-the-project)
- [Observations](#-observations)

## 🚀 Key Features
- **Data Management:** The script efficiently handles data from an Excel file to identify clients with overdue payments and prepares personalized email notifications.
- **Automated Communication:** It automatically composes and sends email messages to notify clients of overdue payments, streamlining communication processes.
- **Workflow Automation:** By automating the process of identifying overdue payments and sending notifications, the script saves time and ensures timely communication with clients.

## 💡 How It Works
1. **Data Loading:** The script loads data from an Excel file named `data.xlsx` using the pandas library.
2. **Data Processing:** It processes the loaded data, converting the `Previsão Pagamento` column to datetime format and filtering payments that are overdue.
3. **Email Composition:** For each client with overdue payments, an email message is composed using their purchase details (ID, Name, Value, Due Date) and a predefined message template.
4. **Email Sending:** The script sends the composed email to the respective clients using the SMTP protocol and a Gmail account configured with provided credentials.
5. **Email Notification:** After sending each email, a confirmation message is printed to the console.

## 🔧 Tools and Technologies Used
- [**python:**](https://www.python.org/) A versatile and widely-used programming language known for its simplicity and readability. It's used to develop the automation.
- [**pandas:**](https://pandas.pydata.org/) Employed for efficient data manipulation, enabling the automation to handle product data from an Excel file within the Python environment.
- [**excel:**](https://support.microsoft.com/en-us/excel) Product data is stored in an Excel file format, widely-used and accessible for tabular data storage.
- [**smtplib:**](https://docs.python.org/3/library/smtplib.html) A module for sending emails via SMTP.
- [**email.message:**](https://docs.python.org/3/library/email.examples.html) A module for creating and manipulating email messages.
- [**os:**](https://docs.python.org/3/library/os.html) A module for interacting with the operating system.
- [**datetime:**](https://docs.python.org/3/library/datetime.html) A module for working with dates and times.
- [**dotenv:**](https://pypi.org/project/python-dotenv/#getting-started) A library for loading environment variables from .env files.


## 📝 Installation Instructions
### 1. Clone this project

 ```bash
git clone https://github.com/esperanca-leonardo/late-pay-notify.git
```

### 2. Navigate to the project directory

```bash
cd late-pay-notify
```

### 3. Create and activate a virtual environment

- #### 3.1. First, install the virtualenv library
    ```bash
    pip install virtualenv
    ```

- #### 3.2. Then, create a virtual environment named `venv`

  - ##### Linux or macOS
      ```bash
      virtualenv venv
      ```
  
  - ##### Windows
      ```bash
      python -m virtualenv venv
      ```

- #### 3.3. Activate the virtual environment
    
    - ##### Linux or macOS
        ```bash
        source venv/bin/activate
        ```
    
    - ##### Windows
        ```bash
        .\venv\Scripts\activate.bat
        ```

### 4. Install dependencies

Make sure you have Python and pip installed on your system. Then, install the project dependencies using pip

```bash
pip install -r requirements.txt
```

### 5. Setting up Gmail authentication

This project uses Gmail for sending emails. You will need to generate an app password for your Gmail account. Follow the instructions [here](https://support.google.com/accounts/answer/185833?hl=en) to generate an app password.

### 6. Create a .env file

Create a file named `.env` in the project directory and add the following variables

```plaintext
MAIL=your_email
PASSWORD=your_app_password
```

### 7. Run the project

Execute the project using the following command

```bash
python main.py
```

## 📌 Observations
As the project currently stands, it will not send emails to any real customers because all customer emails in the database are fake. Therefore, in order to test the application, it will send emails to the sender's email address.


