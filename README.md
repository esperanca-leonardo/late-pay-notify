# 🕒 Late Pay Notify

Late Pay Notify is a tool that automates the process of notifying customers about overdue payments by sending email reminders.

## 📑 Table of Contents
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Observations](#observations)

## 🚀 Key Features
1. **Notification Automation:** Automatically identifies overdue payments and sends email reminders to customers.

## 💡 How It Works
1. **Identification of Overdue Payments:** The system regularly checks the status of payments and identifies those that are overdue based on predefined criteria.
2. **Sending Email Reminders:** Once overdue payments are identified, the system automatically sends email reminders to customers, encouraging them to settle their payment status.

Late Pay Notify simplifies the process of managing overdue payments, providing an efficient and straightforward solution for notifying customers about their outstanding financial obligations.

## 🛠️ Installation
### 1. **Clone this project:**

 ```bash
git clone https://github.com/esperanca-leonardo/late-pay-notify.git
```

### 2. **Navigate to the project directory:**

```bash
cd late-pay-notify
```

### 3. **Create and activate a virtual environment:**

First, install the virtualenv library:

```bash
pip install virtualenv
```

Then, create a virtual environment named `venv`:

```bash
virtualenv venv
```

- #### 3.1. **Activate the virtual environment:**
    
    - ##### Linux or macOS:
    
        ```bash
        source venv/bin/activate
        ```
    
    - ##### Windows:
    
        ```bash
        venv\Scripts\activate
        ```

### 4. **Install dependencies:**

Make sure you have Python and pip installed on your system. Then, install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

### 5. **Setting up Gmail authentication:**

This project uses Gmail for sending emails. You will need to generate an app password for your Gmail account. Follow the instructions [here](https://support.google.com/accounts/answer/185833?hl=en) to generate an app password.

### 6. **Create a .env file:**

Create a file named `.env` in the project directory and add the following variables:

```plaintext
MAIL=your_email
PASSWORD=your_app_password
```

### 7. **Run the project:**

Execute the project using the following command:

```bash
python main.py
```

## 📝 Observations
As the project currently stands, it will not send emails to any real customers because all customer emails in the database are fake. Therefore, in order to test the application, it will send emails to the sender's email address.


