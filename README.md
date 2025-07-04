Enigma Password Manager

Enigma Password Manager is a secure and user-friendly application designed to help users manage their website credentials safely. Built with Python, MySQL, and SMTP for email-based OTP verification, it provides robust features for password management, including generation, storage, and modification of credentials. This project was developed by Yashwant Gokul P and Ritish Karthik S.

Features





Secure Login/Signup: Users can create accounts or log in using a master password with OTP verification sent via email.



Password Generation: Generate strong, random passwords (8-16 characters) with a mix of uppercase, lowercase, numbers, and symbols.



Credential Management:





Add, modify, or view website credentials (website, username, password, email, phone number).



Supports multiple accounts per website with unique usernames.



Account Deletion: Option to delete your account with a 5-minute recovery window.



Password Reset: Reset your master password securely using OTP verification.



Strong Password Validation: Ensures passwords meet security standards and are not common or weak.



Database Integration: Stores user data and credentials securely in a MySQL database.

Prerequisites

To run Enigma Password Manager, ensure you have the following installed:





Python 3.x



MySQL Server



Required Python libraries:

pip install mysql-connector-python tabulate



A Gmail account with an App Password for SMTP email functionality (enable 2-factor authentication and generate an app password in your Google Account settings).



A common_roots.txt file containing a list of common passwords to prevent weak password usage.

Installation





Clone the Repository:

git clone https://github.com/yourusername/enigma-pwd-manager.git
cd enigma-pwd-manager



Set Up MySQL Database:





Create a MySQL database (e.g., enigma_db).



Create the required tables using the following SQL commands:

CREATE TABLE signup7 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    masterpassword VARCHAR(255) NOT NULL
);

CREATE TABLE userinfo (
    id INT,
    website VARCHAR(255) NOT NULL,
    webpassword VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    usermail VARCHAR(255) NOT NULL,
    userph BIGINT NOT NULL,
    FOREIGN KEY (id) REFERENCES signup7(id)
);



Configure Database Connection:





Update the connect_db() function in the code with your MySQL credentials:

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="your_mysql_password",
        database="your_database_name"
    )



Configure Email Settings:





Update the mail() function with your Gmail address and App Password:

from_email = "your_gmail@gmail.com"
password = "your_app_password"



Add Common Passwords File:





Place the common_roots.txt file in the project directory with a list of common passwords (one per line) to prevent weak password usage.



Run the Application:

python enigma_pwd_manager.py

Usage





Run the Program:





Start the application by running the Python script.



The main menu will display the following options:

1. Login
2. Signup
3. Generate Password
4. How to Use
5. Exit



Signup:





Enter a valid email and name, then set a strong master password (8-16 characters with uppercase, lowercase, numbers, and symbols).



Verify your account using the OTP sent to your email.



Login:





Log in with your email and master password.



Use forgotpwd as the master password to reset it via OTP verification.



Manage Credentials:





After logging in, you can:





Add Details: Save website credentials.



Modify Details: Update existing credentials (username, email, password, or phone number).



Show Details: View all saved credentials in a tabulated format.



Delete Account: Permanently delete your account with a 5-minute recovery period.



Generate Password:





Create a strong, random password of specified length (8-16 characters).



How to Use:





Access the built-in guide for detailed instructions on using the application.

Security Features





OTP Verification: Ensures secure signup, login, and password reset with time-limited (5-minute) OTPs.



Strong Password Enforcement: Checks for password strength and prevents the use of common passwords.



Duplicate Entry Prevention: Avoids duplicate website credentials for the same username.



Account Recovery: Provides a 5-minute window to recover a deleted account.



Secure Storage: Credentials are stored in a MySQL database with proper foreign key constraints.

Limitations





Requires an active internet connection for sending OTP emails.



Password generation is limited to 8-16 characters.



The common_roots.txt file must be maintained to ensure weak password detection.



No local file I/O or network calls are supported beyond email functionality.

Contributing

Contributions are welcome! Please follow these steps:





Fork the repository.



Create a new branch (git checkout -b feature-branch).



Make your changes and commit (git commit -m "Add new feature").



Push to the branch (git push origin feature-branch).



Create a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Authors





Yashwant Gokul P and
Ritish Karthik S
.
