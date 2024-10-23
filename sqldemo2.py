import random
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta  # Import for time handling
import tabulate
import re
def is_valid_email(email):
    # Regular expression for validating an Email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="demo5"
    )


connection = connect_db()
if connection.is_connected():
    print("Connected")

cursor = connection.cursor()


def fetch_user_data():
    # Query to fetch id, email, masterpassword, and name from signup7
    query = "SELECT id, email, name, masterpassword FROM signup7"
    cursor.execute(query)
    result = cursor.fetchall()

    user_ids = []  # List to store user IDs#uid, website, webuname, upassword, webmail, webph
    user_emails = []  # List to store emails
    master_passwords = []  # List to store master passwords
    user_names = []  # List to store names

    for row in result:
        user_ids.append(row[0])  # ID
        user_emails.append(row[1])  # Email
        master_passwords.append(row[3])  # Master Password
        user_names.append(row[2])  # Name

    return user_ids, user_emails, master_passwords, user_names

def mail(to_email, subject, body):
    from_email = "enigmapwdmanager@gmail.com"
    password = "yaxv gdzk hyhj mrxp"
    # Set up the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Set up the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()


def pgen(pwlen):
    s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s2 = s1.lower()
    l1 = list(s1)
    l2 = list(s2)
    l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    l4 = ["!", "@", "#", "$", "%", "^", "&", "*"]
    pw = ""
    if pwlen >= 8 and pwlen <= 16:
        #
        for i in range(0, pwlen):
            lists = [l1, l2, l3, l4]
            chosen_list = random.choice(lists)
            n = len(chosen_list)
            p = random.randrange(0, n)
            q = chosen_list[p]
            k = str(q)
            pw = pw + k
        return pw

    else:
        if pwlen < 8:
            print("Minimum 8 characters can be only generated!")
        elif pwlen > 16:
            print("The Maximum Characters can be 16 only!")


def signup(to_mail, subject, body):
    # phno is the phone number (including the country code)
    otpgen = random.randint(1000, 9999)  # Generate a random OTP
    login = False
    msg = body + str(otpgen)  # Message to send
    mail(to_mail, subject, msg)  # Send the OTP message via WhatsApp
    print(f"OTP sent to {to_mail}")

    otp_time = datetime.now()  # Record the time when the OTP is generated

    # Allow the user up to 5 attempts to enter the correct OTP
    for logtype in range(5):
        # Check if the OTP has expired (5 minutes from otp_time)
        if datetime.now() > otp_time + timedelta(minutes=5):
            print("OTP has expired!")
            exit()

        uotp = int(input("Enter your OTP: "))  # Prompt user for OTP

        if uotp == otpgen:
            print("OTP Verified!")
            login = True
            break
        else:
            print(f"Incorrect OTP. {4 - logtype} attempts remaining.")

        if not login and logtype == 4:  # Use 'not login' for readability
            print("Out of Chances!")

    return login


def strongpwd(pwd):
    cap = False
    small = False
    sym = False
    num = False
    all = False
    for i in pwd:
        if i.islower() == True:
            small = True
        if i.isupper() == True:
            cap = True
        if i.isdigit() == True:
            num = True
        if i.isalnum() != True:
            sym = True
        if cap == True and small == True and num == True and sym == True:
            all = True
    return all


userid, umail, mskey, usrnamel = fetch_user_data()

f = open(r"C:\Users\yashw\Documents\common_roots.txt", "r")
comp = f.read()
while True:
    print("===========================================================")
    print("Enigma Pwd Manager")
    print("===========================================================")
    print("India's One of the safest Password Manager")
    print("===========================================================")
    print("                 ~BY Yashwant Gokul P and Ritish Karthik S")
    print("===========================================================")
    print("1. Login")
    print("2. Signup")
    print("3. Generate Password")
    print("4. How to Use")
    print("5. Exit")
    ch = int(input("Enter Your Choice: "))

    if ch == 2:
        to_mail = input("Your mail Address: ").strip().upper()
        while True:
            if is_valid_email(to_mail) == False:
                print("Invalid email format.")
                to_mail = input("Your mail Address: ").strip().upper()
                # Proceed with further processing, like database insertion
            else:
                break
        if to_mail not in umail:
            usr_name = input("Enter Your Name: ").strip().upper()
            subject = (f"{usr_name} Thanks For Creating account in Enigma pwd Manager")
            body = "Your OTP for Signing Up is "
            is_logged_in = signup(to_mail, subject, body)  # Call signup once and store the result
            if is_logged_in:  # Use the stored result to check if login was successful
                usrnamel.append(usr_name.strip())
                umail.append(to_mail)
                while True:
                    pas = input(
                        "Your MasterKey Password(should have a minimum of 8 characters and maximum of 16 characters): ").strip()
                    c = 0
                    while True:
                        if len(pas) > 7 and len(pas) < 17:
                            break
                        if c == 5:
                            print("Retype you Details and login")
                            exit()
                        else:
                            print("Incorrect entry!")
                            c += 1
                            pas = input(
                                "Your MasterKey Password(should have a minimum of 8 characters and maximum of 16 characters): ").strip()
                    stp = strongpwd(pas)  # password Strength
                    if pas.strip() != "forgotpwd":
                        if pas not in comp:
                            if stp == True:
                                pasc = input("Retype Your MasterKey Password: ").strip()
                                if pas.strip() == pasc.strip():
                                    qwery = "INSERT INTO signup7(email, name, masterpassword) VALUES (%s, %s, %s)"
                                    cursor.execute(qwery, (to_mail, usr_name, pas))
                                    connection.commit()
                                    print("Account Created Successfully")
                                    mskey.append(pas.strip())
                                    break
                                else:
                                    print("Verify Your Password Properly")
                            else:
                                print("Type a Strong Password mixed of Numbers, Symbols,capital and small letters")
                        else:
                            print("your password is weak and vulnerable so type a new one")
                    else:
                        print("forgot pwd cannot be the password")
        else:
            print("Account exists already")

    elif ch == 1:
        changed = False
        if changed == True:
            break
        uinmail = input("Email: ").strip().upper()
        while True:
            if is_valid_email(uinmail) == False:
                print("Invalid email format.")
                uinmail = input("Email: ").strip().upper()
            else:
                break
        userid, umail, mskey, usrnamel = fetch_user_data()
        for i in range(5):
            if changed == True:
                break
            count = i
            print("Type 'forgotpwd'in masterkey")
            passw = input("MasterKey: ").strip()
            if uinmail.strip() in umail:
                ind = umail.index(uinmail.strip())
                if mskey[ind] == passw.strip():
                    print("Logged in Successfully")
                    name = usrnamel[ind]
                    body = "A Device has Logged In "
                    subject = f"Was it You {name}?"
                    is_logged_in = signup(uinmail, subject, body)
                    if is_logged_in:
                        while True:
                            print("===========================================================")
                            print("Enigma Pwd Manager")
                            print("===========================================================")
                            print("India's One of the safest Password Manager")
                            print("===========================================================")
                            print("                 ~BY Yashwant Gokul P and Ritish Karthik S")
                            print("===========================================================")
                            print("1. Add Details")
                            print("2. Modify Details")
                            print("3. Show Details")
                            print("4. Delete Your Profile")
                            print("5. Exit")
                            ch1 = int(input("Enter your choice: "))
                            if ch1 == 1:
                                qwery = "select website,username from userinfo where id= %s"
                                cursor.execute(qwery, (userid[ind],))
                                k = cursor.fetchall()
                                lweb = []
                                lun = []
                                for l in k:
                                    lweb.append(l[0])
                                    lun.append(l[1])
                                uid = userid[ind]
                                website = input("Your Website Name: ").strip().upper()
                                print("We require usernames to be mandatory in order to differentiate between multiple accounts for the same website. ")
                                print("""The username doesn't need to be the original one if the website doesn't provide one;
                                you can create a different username of your choice to differentiate between accounts. 
                                However,if the website does provide an original username, use that one.""")
                                webuname = input("Your Username Associated with the website is: ")
                                while True:
                                    if webuname.strip() == "":
                                        print("Invalid input")
                                        print("We require usernames to be mandatory in order to differentiate between multiple accounts for the same website. ")
                                        print("""The username doesn't need to be the original one if the website doesn't provide one;
                                        you can create a different username of your choice to differentiate between accounts. 
                                        However,if the website does provide an original username, use that one.""")
                                        webuname = input("Your Username Associated with the website is: ")
                                    else:
                                        break
                                if website in lweb:
                                    webindex = lweb.index(website)
                                    if lun[webindex] == webuname:
                                        print("You CANNOT have Duplicate entries")
                                        break
                                upassword = input("Your Password: ")
                                webmail = input("Your Email Associated with the website is: ").strip().upper()
                                while True:
                                    if is_valid_email(webmail) == False:
                                        print("Invalid email format.")
                                        webmail = input("Your Email Associated with the website is: ").strip().upper()
                                        # Proceed with further processing, like database insertion
                                    else:
                                        break
                                webph = int(input("Your Phoneno Associated with the website is: "))
                                qwery = "INSERT INTO userinfo(id, website, webpassword, username, usermail, userph) VALUES (%s, %s, %s, %s, %s, %s)"
                                cursor.execute(qwery, (uid, website, upassword, webuname, webmail, webph))
                                connection.commit()
                            elif ch1 == 2:
                                qwery = "select website,username from userinfo where id= %s"
                                cursor.execute(qwery, (userid[ind],))
                                k = cursor.fetchall()
                                lweb = []
                                lun = []
                                for l in k:
                                    lweb.append(l[0])
                                    lun.append(l[1])
                                print(lweb, lun)
                                qwery = "SELECT website, username, webpassword, usermail, userph FROM userinfo WHERE id = %s"
                                cursor.execute(qwery, (userid[ind],))
                                op = cursor.fetchall()
                                print(f"{usrnamel[ind]}'s Websites and Credentials")
                                header = ("Website", "Username", "Password", "Email", "Phone Number")
                                print(tabulate.tabulate(op, headers=header, tablefmt="pretty"))
                                print(
                                    "What do you want to modify:\n 1.Web username\n2.Email\n3.Website Password\n4.Web Phoneno\n5.Exit")
                                ch4 = int(input("Enter your choice: "))
                                option = ""
                                if ch4 == 1:
                                    option = "a"
                                elif ch4 == 2:
                                    option = "b"
                                elif ch4 == 3:
                                    option = "c"
                                elif ch4 == 4:
                                    option = "d"
                                if option != "":
                                    webmod = input("Type the website you want modify: ").strip().upper()
                                    if lweb.count(webmod) > 1 and webmod in lweb:
                                        usmod = input("Your username as multiple wesite exist, enter a new one: ").strip()
                                        webindex = lun.index(usmod)
                                        if lun[webindex] == usmod:
                                            if option == "a":
                                                qwery1 = "update userinfo set username=%s where website=%s and username=%s and id=%s"
                                                change = input("Change the web username into: ").strip()
                                                while True:
                                                    if change.strip() == "":
                                                        print("Invalid input")
                                                        print(
                                                            "We require usernames to be mandatory in order to differentiate between multiple accounts for the same website. ")
                                                        print("""The username doesn't need to be the original one if the website doesn't provide one;
                                                        you can create a different username of your choice to differentiate between accounts. 
                                                        However,if the website does provide an original username, use that one.""")
                                                        change = input("Change the web username into: ").strip()
                                                    else:
                                                        break

                                                if webmod in lweb:
                                                    webindex = lweb.index(webmod)
                                                    if lun[webindex] == change:
                                                        print("You CANNOT have Duplicate entries")
                                                        changed=True
                                                        break
                                                cursor.execute(qwery1, (change, webmod, usmod, userid[ind]))
                                                connection.commit()
                                            elif option == "b":
                                                qwery2 = "update userinfo set usermail=%s where website=%s and username=%s and id=%s"
                                                change = input("Change the web email into: ").strip().upper()
                                                while True:
                                                    if is_valid_email(change) == False:
                                                        print("Invalid email format.")
                                                        change = input("Change the web email into: ").strip().upper()
                                                        # Proceed with further processing, like database insertion
                                                    else:
                                                        break
                                                cursor.execute(qwery2, (change, webmod, usmod, userid[ind]))
                                                connection.commit()
                                            elif option == "c":
                                                qwery3 = "update userinfo set webpassword=%s where website=%s and username=%s and id=%s"
                                                change = input("Change the web password into: ")
                                                cursor.execute(qwery3, (change, webmod, usmod, userid[ind]))
                                                connection.commit()
                                            elif option == "d":
                                                qwery4 = "update userinfo set userph=%s where website=%s and username=%s and id=%s"
                                                change = int(input("Change the web ph.no into: "))
                                                cursor.execute(qwery4, (change, webmod, usmod, userid[ind]))
                                                connection.commit()
                                        else:
                                            print("print invalid username")
                                    else:
                                        if webmod not in lweb:
                                            print("Website not found")
                                        else:

                                            if option == "a":
                                                qwery1 = "update userinfo set username=%s where website=%s and id=%s"
                                                change = input("Change the web username into: ").strip()
                                                if change.strip() == "":
                                                    print("Invalid input")
                                                    print("We require usernames to be mandatory in order to differentiate between multiple accounts for the same website. ")
                                                    print("""The username doesn't need to be the original one if the website doesn't provide one;
                                                    you can create a different username of your choice to differentiate between accounts. 
                                                    However,if the website does provide an original username, use that one.""")
                                                change = input("Change the web username into: ").strip()
                                                cursor.execute(qwery1, (change, webmod, userid[ind]))
                                                connection.commit()
                                            elif option == "b":
                                                qwery2 = "update userinfo set usermail=%s where website=%s and id=%s"
                                                change = input("Change the web email into: ").strip().upper()
                                                while True:
                                                    if is_valid_email(change) == False:
                                                        print("Invalid email format.")
                                                        change = input("Change the web email into: ").strip().upper()
                                                    else:
                                                        break
                                                cursor.execute(qwery2, (change, webmod, userid[ind]))
                                                connection.commit()
                                            elif option == "c":
                                                qwery3 = "update userinfo set webpassword=%s where website=%s and id=%s"
                                                change = input("Change the web password into: ")
                                                cursor.execute(qwery3, (change, webmod, userid[ind]))
                                                connection.commit()
                                            elif option == "d":
                                                qwery4 = "update userinfo set userph=%s where website=%s and id=%s"
                                                change = int(input("Change the web ph.no into: "))
                                                cursor.execute(qwery4, (change, webmod, userid[ind]))
                                                connection.commit()
                            elif ch1 == 3:
                                qwery = "select website, webpassword, username, usermail, userph from userinfo where id= %s"
                                cursor.execute(qwery, (userid[ind],))
                                k = cursor.fetchall()
                                print(f"{usrnamel[ind]}'s Websites and Credentials")
                                header = ("Website", "Username", "Password", "Email", "Phone Number")
                                print(tabulate.tabulate(k, headers=header, tablefmt="pretty"))
                            elif ch1 == 4:
                                print("Caution You May Loose your data")
                                ques = input("Are you sure about Deleting your account(y/n)").lower().strip()
                                qwerylog = "DELETE FROM signup7 where id=%s"
                                qwerydet = "DELETE FROM userinfo where id=%s"
                                if ques == "y":
                                    subject = f"{usrnamel[ind]} We are Sorry To See You Going :("
                                    body = ("If you dont like any of our feature or You want any other feature mail us"
                                            "We are expecting your return"
                                            "Your OTP for Deleting Your Account is:  ")
                                    signup(uinmail, subject, body)
                                    del_time = datetime.now()
                                    print(" You will be able to recover Account within the next five Minutes")
                                    confirm=input("Do you want to recover your account(y/n): ")
                                    while True:
                                        if confirm.lower()=="y":
                                            print("Your account has been Recovered")
                                            subject = f"{usrnamel[ind]} We are happy that you changed your mind"
                                            body = (
                                                "If you dont like any of our feature or You want any other feature mail us"
                                                "We will do our best not to give you another chance to rethink this decision.")
                                            mail(uinmail, subject, body)
                                            break
                                        else:
                                            print("You would be able to see thi")
                                            confirm = input("Do you want to recover your account(y/n): ")
                                        if datetime.now() > del_time + timedelta(minutes=5):
                                            print("Your Account has been Deleted")
                                            cursor.execute(qwerylog, (userid[ind],))
                                            connection.commit()
                                            cursor.execute(qwerydet, (userid[ind],))
                                        print("If you dont like any of our feature or You want any other feature mail us"
                                              "We are expecting your return ")
                                        exit()
                                else:
                                    break
                            elif ch1 == 5:
                                print("Exiting......")
                                changed = True
                                break
                            else:
                                print("Invalid Option")
                elif passw == "forgotpwd":
                    if umail[ind] == uinmail:
                        subject = f"{usrnamel[ind]} do you want to change password"
                        body = "Your OTP is, "
                        is_logged_in = signup(uinmail, subject, body)  # Call signup once and store the result
                        if is_logged_in:  # Use the stored result to check if login was successful
                            while True:
                                c = 0
                                while True:
                                    newpas = input("Your New MasterKey Password: ")
                                    if len(newpas) > 7 and len(newpas) < 17:
                                        break
                                    if c == 5:
                                        print("Retype you Details and login")
                                        exit()
                                    else:
                                        print("Incorrect entry!")
                                        c += 1
                                        newpas = input(
                                            "Your New MasterKey Password(should have a minimum of 8 characters and maximum of 16 characters): ").strip()
                                stpf = strongpwd(newpas)  # password Strength
                                if newpas != "forgotpwd":
                                    if newpas not in comp:
                                        if stpf == True:
                                            newpasc = input(
                                                "Your New MasterKey Password(should have a minimum of 8 characters and maximum of 16 characters): ").strip()
                                            if newpas == newpasc:
                                                ind = umail.index(uinmail)
                                                # SQL query to update the master password
                                                qwery = "UPDATE signup7 SET masterpassword = %s WHERE email = %s"
                                                cursor.execute(qwery, (newpas, uinmail))
                                                connection.commit()
                                                print("Your Password Has changed Successfully")
                                                changed = True
                                                break
                                            else:
                                                print("Verify Your Password Properly")
                                        else:
                                            print(
                                                "Type a Strong Password mixed of Numbers, Symbols,capital and small letters")
                                    else:
                                        print("your password is weak and vulnerable so type a new one")
                                else:
                                    print("forgot pwd cannot be the password")
                    else:
                        print("username or password is wrong")
                else:
                    print("username or password is wrong")
            else:
                print("user not found")
                break
            if i == 4:
                body = f"Was it You? If it is not you, reply back"
                subject = f"{usrnamel[ind]} Unauthorized entry has been detected"
                print("Out of Chances!")
                mail(uinmail, subject, body)
                exit()
    elif ch == 3:
        plen = int(input("Length of Password You want to Generate"))
        p = pgen(plen)
        print("Your genearted Password: ", p)
        while True:
            feedback = input("Do You want to regenerate: ").strip().lower()
            if feedback.lower() == "y":
                p = pgen(plen)
                print(p)
                feedback = input("Do You want to regenerate: ").strip().lower()
            else:
                break
    elif ch == 4:
        print("""
        Enigma Pwd Manager – Quick Guide

        1. **Login**
           - Enter email and master password.
           - Type `forgotpwd` to reset your password.

        2. **Main Menu Options**
           1. **Add Details** - Save new website login (website, username, password, email, phone).
           2. **Modify Details** - Edit existing credentials.
           3. **Show Details** - View all saved credentials.
           4. **Delete Account** - Permanently delete your account.
           5. **Exit** - Exit the manager.

        3. **Password Generation**
           - Specify length to generate a strong password.

        4. **Security**
           - Master password: 8-16 characters and must be strong.
           - “forgotpwd” cannot be used as a password.

        5. **Forgot Password**
           - Use `forgotpwd` to reset via email verification.

        **Warning:** Deleting your account erases all data permanently!
        """
              )
        use = input("Would you like to try(y/n) now ?: ")
        if use.lower() == "y":
            break
        else:
            print("Dont Forget to try")
            exit()
    elif ch == 5:
        print("Exiting.....")
        break
    else:
        print("Invalid Option")