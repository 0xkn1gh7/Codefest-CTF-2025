#!/usr/bin/env python3

def banner():
    print(f'''
 ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗    ██╗   ██╗██╗███████╗
██╔════╝██║  ██║██╔══██╗██║████╗  ██║    ██║   ██║██║██╔════╝
██║     ███████║███████║██║██╔██╗ ██║    ██║   ██║██║███████╗
██║     ██╔══██║██╔══██║██║██║╚██╗██║    ╚██╗ ██╔╝██║╚════██║
╚██████╗██║  ██║██║  ██║██║██║ ╚████║     ╚████╔╝ ██║███████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝      ╚═══╝  ╚═╝╚══════╝
                                                                                          
A blockchain visualizer. Atleast I think so.
    ''')

def print_menu():
    print('''
1. Add a block to the chain
2. View chain
3. Access a block
4. Exit
    ''')

class Block:
    def __init__(self, block_id, transaction):
        self.id = block_id
        self.transaction = transaction

chain = []

banner()
while True:
    print_menu()
    user = int(input("[-] ENTER OPTION: "))
    if user == 1:
        if len(chain) == 9:
            print('[*] MAX BLOCKS IN CHAIN')
            continue
        money = int(input("[-] MONEY IN THE TRANSACTION: "))
        block = Block(len(chain)+1, money)
        chain.append(block)
    elif user == 2:
        print(f"[*] {len(chain)} BLOCKS IN CHAIN.")
        for i in chain:
            print(f'''
----------
| ID - {i.id} |
----------
            ''')
    elif user == 3:
        user_id = int(input("[-] CHOOSE BLOCK ID: "))-1
        if user_id < 0 or user_id >= len(chain):
            print("[*] INVALID BLOCK ID")
            continue
        block = chain[user_id]
        while True:
            print(f'''
[*] SELECTED BLOCK ID: {block.id}
1. Access Attribute (eg - id)
2. Back to main menu
            ''')
            user2 = int(input("[-] ENTER OPTION: "))
            if user2 == 1:
                attr = input('ATTRIBUTE: ')
                try:
                    eval("print(block."+attr+")")
                except:
                    print("[!] INVALID")
                    continue
            else:
                break
    else:
        break