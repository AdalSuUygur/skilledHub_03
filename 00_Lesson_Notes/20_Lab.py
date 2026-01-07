
burak_account = {
    'account no': '12345',
    'password': '123',
    'balance': 2000,
    'additional balance': 1000
}

hakan_account = {
    'account no': '98765',
    'password': '546',
    'balance': 3000,
    'additional balance': 1000
}

ipek_account = {
    'account no': '34567',
    'password': '987',
    'balance': 4000,
    'additional balance': 1000
}

users = [burak_account, hakan_account, ipek_account]

def get_valid_answer(question: str, valid_options: tuple) -> str:
    question += f' ({", ".join(valid_options)}): '
    
    response = input(question)
    
    while response.lower() not in valid_options:
        print('Please type the valid options..!')
        response = input(question)
    
    return response

def account_information(account: dict):
    print(
        f'Account No: {account["account no"]}\n'
        f'Balance: {account["balance"]}\n'
        f'Additional Balance: {account["additional balance"]}'
    )

def withdraw_money(account: dict, amount: int):
    if account['balance'] >= amount:
        account['balance'] -= amount
        account_information(account=account)
    else:
        total_balance = account['balance'] + account['additional balance']
        
        if total_balance >= amount:
            used_additional_balance = get_valid_answer(question='Insufficen balance..!\nDo you want to use additional balance?', valid_options=("y", "n"))
            
            match used_additional_balance:
                case 'y':
                    detech_amount = amount - account['balance']
                    account['balance'] = 0
                    account['additional balance'] -= detech_amount
                    account_information(account=account)
                case 'n':
                    print('Transaction has been cancaled..!')
                    account_information(account=account)
        else:
            print(
                'Insufficent balance..!\n'
                'Transaction has been cancaled..!'
            )
            account_information(account=account)

withdraw_money(account=ipek_account, amount=4500)

# ipek_account --> balance=0, additional balance=500
def deposit_money(account: dict, amount: int):
    if account['additional balance'] < 1000:
        account['balance'] += amount
        short = 1000 - account['additional balance']
        if account['balance'] >= short:
            account['balance'] -= short
            account['additional balance'] += short
        else:
            account['additional balance'] += amount
    account_information(account=account)

deposit_money(account=ipek_account, amount=300)