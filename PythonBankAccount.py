# Python Bank Account
import sqlite3

# Establish database connection
connection = sqlite3.connect('bank_users_details.db')
sql = connection.cursor()

# Create user_details table if not exists
sql.execute('''CREATE TABLE IF NOT EXISTS user_details (
            Id integer PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email_address TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            balance REALd
            )''')
connection.commit()


# Function to register client
def registration_client():
    print('-' * 35)
    print('\nType in:')
    first_name = input('\nYour firstname: ').capitalize()
    last_name = input('Your lastname: ').capitalize()
    phone_number = input('Your phone number: (+998) ')
    email_address = input('Your email address: ')
    username = input('Your unique username: ')
    print()
    balance = 0  # initially balance equals to 0
    if email_address_check(email_address) and first_name.isalpha() and last_name.isalpha() \
            and len(phone_number) == 9 and phone_number.isdigit():
        if checking_existing_username(username):
            print('\nError: A user with this username already exists!')
            return
        else:
            print('_' * 35)
            print('Account successfully created!')
            print('_' * 35)
            print(f'Firstname: {first_name}\n'
                  f'Lastname: {last_name}\n'
                  f'Phone number: {phone_number}\n'
                  f'Email address: {email_address}\n'
                  f'Username: {username}\n'
                  f'Balance: $ {balance:.2f}\n')

            sql.execute(f'''INSERT INTO user_details (first_name, last_name, phone_number, 
            email_address, username, balance) values (?, ?, ?, ?, ?, ?)''',
                        (first_name, last_name, phone_number, email_address, username, balance))
            connection.commit()
    else:
        print('\nError invalid symbols!')

# Function to validate email format
def email_address_check(email_address):
    email_address_valid = '@' in email_address \
                          and '.' in email_address.split('@')[-1] \
                          and not email_address.endswith('.')
    # email has to have @ in it
    # email has to have . in it
    # dividing email to two parts
    # taking second part [-1] to check if in email after @ there is a dot,
    # also email cannot end with dot
    return email_address_valid


# Function to check username existence
def checking_existing_username(username):
    sql.execute('SELECT * FROM user_details WHERE username = ?', (username,))
    return sql.fetchone()


# Function to get user's username
def get_username(username):
    sql.execute('SELECT * FROM user_details WHERE username = ?', (username,))
    user_profile = sql.fetchone()
    if user_profile:
        user_profile_dict = {
            'id': user_profile[0],
            'firstname': user_profile[1],
            'lastname': user_profile[2],
            'phone_number': user_profile[3],
            'email_address': user_profile[4],
            'username': user_profile[5],
            'balance': user_profile[6]
        }
        return user_profile_dict
    return None


# Function to update user's balance
def update_balance(username, new_balance):
    sql.execute('UPDATE user_details SET balance = ? WHERE username = ?', (new_balance, username,))
    print(f'Account: {username}\n'
          f'Account balance: ${new_balance:.2f}')
    connection.commit()


# Function to make a deposit
def make_deposit(username):
    user_profile = get_username(username)
    if user_profile:
        deposit_amount = input('Enter amount of deposit: ')
        try:
            deposit_amount = float(deposit_amount)
            new_balance = user_profile['balance'] + deposit_amount
            print('Making deposit ...\n')
            print('^' * 35)
            print('\nDeposit made successfully!\n')
            update_balance(username, new_balance)
            return new_balance

        except ValueError:
            print('\nError invalid symbols in deposit!')
            return
    else:
        print('\nError invalid username!')


# Function to withdraw
def withdraw(username):
    user_profile = get_username(username)
    if user_profile:
        withdraw_amount = input('Enter withdraw amount: ')
        try:
            withdraw_amount = float(withdraw_amount)
            if user_profile['balance'] >= withdraw_amount:
                new_balance = user_profile['balance'] - withdraw_amount
                print('Withdrawing ...\n')
                print('^' * 35)
                print('Withdraw was made successfully!\n')
                update_balance(username, new_balance)
                return new_balance
            else:
                print('\nError insufficient funds!')
                return
        except ValueError:
            print('\nError invalid symbols in withdraw!')
            return
    else:
        print('\nError invalid username!')


# Function to calculate
def calculate():
    print('^' * 35)
    print('\nInterest types\n')
    print('^' * 35)
    calculate_type = input('\n1. 12 months 1% interest rate\n'
                           '2. 24 months 1% interest rate\n'
                           '3. 36 months 1% interest rate\n'
                           '------------------------------------\n'
                           'Type in number::: ')
    calculate_amount = input('\nEnter deposit amount to calculate: $ ')
    try:
        calculate_amount = float(calculate_amount)
        if calculate_type == '1':
            total_balance = calculate_amount * (1 + 0.01) ** 12
            pure_profit = total_balance - calculate_amount
            print('\nCalculating...')
            print('_' * 35)
            print('After 12 months\n'
                  f'\nPure profit: ${pure_profit:.2f}\n'
                  f'Total balance: ${total_balance:.2f}')
        elif calculate_type == '2':
            total_balance = calculate_amount * (1 + 0.01) ** 24
            pure_profit = total_balance - calculate_amount
            print('\nCalculating...')
            print('_' * 35)
            print('After 24 months\n'
                  f'\nPure profit: ${pure_profit:.2f}\n'
                  f'Total balance: ${total_balance:.2f}')
        elif calculate_type == '3':
            total_balance = calculate_amount * (1 + 0.01) ** 36
            pure_profit = total_balance - calculate_amount
            print('\nCalculating...')
            print('_' * 35)
            print('After 36 months\n'
                  f'\nPure profit: ${pure_profit:.2f}\n'
                  f'Total balance: ${total_balance:.2f}')
        else:
            print('\nError invalid interest type!')
            return

    except ValueError:
        print('\nError invalid symbols in calculate deposit!')
        return


# Function to search user by first name, last name and phone number
def search(first_name, last_name, phone_number):
    sql.execute('SELECT * FROM user_details WHERE first_name = ? or last_name= ? or phone_number= ?', (first_name, last_name, phone_number))
    user_profiles = sql.fetchall()
    return user_profiles


# Function to show account details
def show_account(username):
    account = get_username(username)
    if account:
        print()
        print('-' * 35)
        print(f'User Id: {account["id"]}\n'
              f'Firstname: {account["firstname"]}\n'
              f'Lastname: {account["lastname"]}\n'
              f'Phone number: {account["phone_number"]}\n'
              f'Email address: {account["email_address"]}\n'
              f'Username: {account["username"]}\n'
              f'Balance: {account["balance"]:.2f}\n')
        return account
    else:
        print('\nError username not found!')
        return


# Function to edit account details
def edit_account():
    editing_types = input('\n1. Edit firstname\n'
                          '2. Edit lastname\n'
                          '3. Edit phone number\n'
                          '4. Edit email address\n'
                          '5. Edit username\n'
                          '----------------------------\n'
                          'Type in number::: ')
    if editing_types == '1':
        first_name = input('\nEnter firstname to edit: ').capitalize()
        username = input('Enter username to find bank account: ')
        if get_username(username):
            sql.execute('UPDATE user_details SET first_name =? WHERE username =?', (first_name, username,))
            print()
            print('^' * 35)
            print('Changes are made successfully!')
            show_account(username)
            connection.commit()
        else:
            print('\nError username not found!')
            return
    elif editing_types == '2':
        last_name = input('\nEnter lastname to edit: ').capitalize()
        username = input('Enter username to find bank account: ')
        if get_username(username):
            sql.execute('UPDATE user_details SET last_name = ? WHERE username = ?', (last_name, username,))
            print()
            print('^' * 35)
            print('Changes are made successfully!')
            show_account(username)
            connection.commit()
        else:
            print('\nError username not found!')
            return
    elif editing_types == '3':
        phone_number = input('\nEnter new phone number: (+998) ')
        if len(phone_number) == 9 and phone_number.isdigit():
            username = input('Enter username to find bank account: ')
            if get_username(username):
                sql.execute('UPDATE user_details SET phone_number = ? WHERE username = ?', (phone_number, username,))
                print()
                print('^' * 35)
                print('Changes are made successfully!')
                show_account(username)
                connection.commit()
            else:
                print('\nError username not found!')
                return
        else:
            print('\nError invalid phone number!')
            return
    elif editing_types == '4':
        email_address = input('\nEnter new email address: ')
        if email_address_check(email_address):
            username = input('Enter username to find bank account: ')
            if get_username(username):
                sql.execute('UPDATE user_details SET email_address = ? WHERE username = ?', (email_address, username,))
                print('^' * 35)
                print('Changes are made successfully!')
                show_account(username)
                connection.commit()
            else:
                print('\nError username not found!')
                return
        else:
            print('\nError invalid email address!')
            return
    elif editing_types == '5':
        username = input('\nEnter username to edit:  ')
        if get_username(username):
            new_username = input('Enter new username: ')
            if checking_existing_username(new_username):
                print('\nError: A user with this username already exists!!')
                return
            else:
                sql.execute('UPDATE user_details SET username = ? WHERE username = ?', (new_username, username,))
                print()
                print('^' * 35)
                print('Changes are made successfully!')
                show_account(new_username)
                connection.commit()

        else:
            print('\nError username not found!')
            return
    else:
        print('\nError invalid symbol!')
        return


# Function to delete user account
def delete_account(username):
    if get_username(username):
        sql.execute('DELETE FROM user_details WHERE username = ?', (username,))
        print('^' * 35)
        print('Changes are made successfully!\n')
        print(f'\nNo such bank account with username "{username}" in the database')
        print('^' * 35)
        show_account(username)
        connection.commit()
    else:
        print('\nNo such username is found!')
        return


# Function to show user's profile
def account_profile():
    account_settings = input('\n1. View account\n'
                             '2. Edit account\n'
                             '3. Delete account\n'
                             '-----------------------\n'
                             'Type in number::: ')
    if account_settings == '1':
        username = input('\nEnter username to view: ')
        show_account(username)
    elif account_settings == '2':
        edit_account()
    elif account_settings == '3':
        username = input('\nEnter username to delete:  ')
        delete_account(username)
    else:
        print('\nError invalid symbols!')
        return


# Main menu
while True:
    print()
    print('*' * 35)
    print('\nBank account\n')
    print('*' * 35)
    main_menu = input('1. Create account\n'
                      '2. Make Deposit\n'
                      '3. Withdraw\n'
                      '4. View balance\n'
                      '5. Calculate %\n'
                      '6. Search\n'
                      '7. Accounts profiles\n'
                      '8. Exit\n'
                      '---------------------------\n'
                      'Type in number::: ')
    if main_menu == '1':
        registration_client()
    elif main_menu == '2':
        username = input('\nEnter username to make deposit: ')
        make_deposit(username)
    elif main_menu == '3':
        username = input('\nEnter username to withdraw: ')
        withdraw(username)
    elif main_menu == '4':
        username = input('\nEnter username to view balance: ')
        profile = get_username(username)
        if profile:
            print(f'Balance: ${profile["balance"]:.2f}')
        else:
            print("\nError username not found!")
    elif main_menu == '5':
        calculate()
    elif main_menu == '6':
        first_name = input('\nEnter first name to search: ').capitalize()
        last_name = input('Enter last name to search: ').capitalize()
        phone_number = input('Enter phone number to search: (+998) ')
        profiles = search(first_name, last_name, phone_number)
        if profiles:
            for each_user in profiles:
                print()
                print('-' * 35)
                print(f'User Id: {each_user[0]}\n'
                      f'First name: {each_user[1]}\n'
                      f'Last name: {each_user[2]}\n'
                      f'Phone number: {each_user[3]}\n'
                      f'Email address: {each_user[4]}\n'
                      f'Username: {each_user[5]}\n'
                      f'Balance: ${each_user[6]:.2f}\n')
        else:
            print('\nError invalid search data!')
    elif main_menu == '7':
        account_profile()
    elif main_menu == '8':
        print('\nExit')
        connection.close()
        exit(0)
    else:
        print('\nError invalid symbol')


