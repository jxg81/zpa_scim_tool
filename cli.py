#!/usr/bin/env python
import subprocess
import platform
import json

from api import scim_api
from const import ZPA_BASE_URL, ZPA_TOKEN, ZIA_BASE_URL, ZIA_TOKEN




def clear():
    if platform.system() == 'Windows':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear')

def menu(client: scim_api, action=0, product='ZPA'):
    clear()
    print(f'''
           You are currently managing: {product}
           [1] - Create User
           [2] - View All Users
           [3] - Delete User
           [4] - Create Group
           [5] - View All Groups
           [6] - Delete Group
           [7] - Exit
           
           Notes:
           UserID and GroupID entries should be the 'ZIA/ZPA Internal ID'. Referenced as 'id' in API responses
           ExternalID is an arbitrary unique value used to track ID's in the source ID repository
           Make sure ExternalID is unique for each entry
           The ZIA domain suffix for username must match one of the domains associated with the ZIA tenant''')
    if action == 0:
        action = int(input("What would you like to do today?: "))
    if action == 1:
        clear()
        print('**Enter Details for new user**\n')
        user_dict = {}
        user_dict['external_id'] = input("Enter Unique ExternalID: ")
        user_dict['username'] = input("Enter Username (email format): ")
        user_dict['given_name'] = input("Enter Given Name: ")
        user_dict['family_name'] = input("Enter Family Name: ")
        user_dict['email'] = input("Enter Email: ")
        clear()
        print('**You Have Entered**\n')
        for k, v in user_dict.items():
            print(f'{k}: {v}')
        correct = ''
        while correct not in ('y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO'):
            correct = input('Is this correct[y/n]: ')
        if correct in ('y', 'Y', 'yes', 'Yes', 'YES'):
            data = client.create_user(**user_dict)
            print(json.dumps(data, indent=4))
            input('Press enter to return to menu: ')
        else:
            return action
    elif action == 2:
        clear()
        data = client.get_all_users()
        print(json.dumps(data, indent=4))
        input('Press enter to return to menu: ')
        return 0
    elif action == 3:
        clear()
        user_id = input('Provide UserID (not username): ')
        data = client.delete_user(user_id)
        if 'Success' in data.keys():
            input('SUCCESS: Press enter to return to menu: ')
        else:
            input('DELETE FAILED, Check ID Value: Press enter to return to menu: ')
    elif action == 4:
        clear()
        print('**Enter details for new group**')
        group_dict = {}
        group_dict['external_id'] = input("Enter Unique ExternalID: ")
        group_dict['displayName'] = input("Enter Display Name: ")
        group_dict['member'] =[]
        group_dict['member'].append(input("Enter UserID (not username): "))
        another_member = ''
        while another_member not in ('y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO'):
            another_member = input('Do you want to add another group member [y/n]: ')
            if another_member in ('y', 'Y', 'yes', 'Yes', 'YES'):
                another_member = ''
                group_dict['member'].append(input("Enter UserID (not username): "))
        clear()
        print('**You Have Entered**')
        for k, v in group_dict.items():
            print(f'{k}: {v}')
        correct = ''
        while correct not in ('y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO'):
            correct = input('Is this correct[y/n]: ')
        if correct in ('y', 'Y', 'yes', 'Yes', 'YES'):
            data = client.create_group(**group_dict)
            print(json.dumps(data, indent=4))
            input('Press enter to return to menu: ')
        else:
            return action
    elif action == 5:
        clear()
        data = client.get_all_groups()
        print(json.dumps(data, indent=4))
        input('Press enter to return to menu: ')
    elif action == 6:
        clear()
        group_id = input('Provide GroupID (not group name): ')
        data = client.delete_group(group_id)
        if 'Success' in data.keys():
            input('SUCCESS: Press enter to return to menu: ')
        else:
            input('DELETE FAILED, Check ID Value: Press enter to return to menu: ')
        input('Press enter to return to menu: ')
    elif action == 7:
        print("The program has been exited")
        return 7
    else:
        return 0


if __name__ == '__main__':
    print('''
        Welcome to ZIA/ZPA SCIM Tool
        [1] - ZPA SCIM Management
        [2] - ZIA SCIM Management
        [3] - Exit
        \n''')
    
    choice = int(input("What would you like to do today?: "))
    if choice == 1:
        clear()
        if not ZPA_BASE_URL:
            ZPA_BASE_URL = input('ZPA SCIM Provisioning URL (i.e https://scim.../v2): ')
        if not ZPA_TOKEN:
            ZPA_TOKEN = input('ZPA Bearer Token: ')
        client = scim_api(ZPA_BASE_URL,ZPA_TOKEN)
        product = 'ZPA'
        action = 0
    if choice == 2:
        clear()
        if not ZIA_BASE_URL:
            ZPA_BASE_URL = input('ZIA SCIM Provisioning URL (i.e https://scim.zscal.../scim): ')
        if not ZIA_TOKEN:
            ZPA_TOKEN = input('ZIA Bearer Token: ')
        client = scim_api(ZIA_BASE_URL,ZIA_TOKEN)
        product = 'ZIA'
        action = 0
    if choice not in (1,2):
        action = 7
    while action != 7:
        action = menu(client, action, product)  
    

#external_id = input("Enter External ID: ")
#name = input("Enter Name: ")
#members = input("Enter Members: ")