import datetime

bank_accounts = {
    1001: {
        "first_name": "Alice",
        "last_name": "Smith",
        "id_number": "123456789",
        "balance": 2500.50,
        "transactions_to_execute": [
         ("2024-08-17 14:00:00", 1001, 1002, 300), ("2024-08-17 15:00:00", 1001, 1003, 200)],
        "transaction_history": [
                          ("2024-08-15 09:00:00", 1001, 1002, 500, "2024-08-15 09:30:00") ]
    },
    1002: {
        "first_name": "Bob",
        "last_name": "Johnson",
        "id_number": "987654321",
        "balance": 3900.75,
        "transactions_to_execute": [],
        "transaction_history": [ ]
    },
    1003: {
        "first_name": "Bob2",
        "last_name": "Johnson2",
        "id_number": "987654320",
        "balance": 3100.75,
        "transactions_to_execute": [],
        "transaction_history": []
    }
}

def create_trx(source_account_no: int, destination_account_no: int, amount: int) -> None:
    source_account = bank_accounts.get(source_account_no)
    transactions_to_execute = source_account.get("transactions_to_execute")
    # also
    # source_account[source_account_no]["transactions_to_execute"]
    trx_tuple = (str(datetime.datetime.now()), source_account_no, destination_account_no, amount)
    transactions_to_execute.append(trx_tuple)

def perform_trx(account_no: int) -> None:
    source_account = bank_accounts.get(account_no)
    transactions_to_execute = source_account.get("transactions_to_execute")
    for trx in transactions_to_execute:
        # ("2024-08-17 14:00:00", 1001, 1002, 300)
        dest_account_no = trx[2]
        amount = trx[3]
        bank_accounts.get(dest_account_no)["balance"] += amount
        balance = bank_accounts.get(dest_account_no).get("balance")
        balance += amount
        source_account["balance"] -= amount
        # trx.append(str(datetime.datetime.now())) # Error
        # 1
        #list_tuple = list(trx) # ["2024-08-17 14:00:00", 1001, 1002, 300]
        #list_tuple.append(datetime.datetime.now())
        #tuple_list = tuple(list_tuple)
        # 2
        # hist_trx = trx + (str(datetime.datetime.now()),)
        # 3
        #source_account["transaction_history"].\
        #   append( (trx[0], trx[1], trx[2], trx[3], datetime.datetime.now()) )
        # 4 -- shortest
        source_account["transaction_history"].append( trx + tuple(datetime.datetime.now(),) )

    transactions_to_execute.clear()


def add_trx():
    while True:
        try:
            source_account_no: int = int(input("what's the source account?"))
            if bank_accounts.get(source_account_no) is None:
                print(f'account {source_account_no} does not exist')
                continue
            destination_account_no: int = int(input("what's the dest account?"))
            if bank_accounts.get(destination_account_no) is None:
                print(f'account {destination_account_no} does not exist')
                continue
            amount: int = int(input("what's the amount?"))
            if amount <= 50:
                print('amount must be at least 50')
                continue
            break

        except:
            print('wrong data...')


def execute_trx():
    pass

def repotrs():
    pass

def show_main_menu():
    while True:
        print('1. Create trx')
        print('2. Execute trx')
        print('3. reports')
        print('4. exit')
        choice = input("what's your choice?")
        if choice == "4":
            # are you sure?
            break
        match choice:
            case "1":add_trx()
            case "2":execute_trx()
            case "3":repotrs()
            case _:print("wrong choice .... try again")
    print("good bye...")

