# zpa_scim_tool
Simple tool to interface with the Zscaler ZPA SCIM interface

> [!IMPORTANT]
> This utility are not affiliated with, nor supported by Zscaler in any way.

## TL;DR
pip install -r requirements.txt

export ZPA_SCIM_BASE_URL=**ZPA_SCIM_Service_Provider_Endpoint**

export ZPA_SCIM_TOKEN=**YOUR_ZPA_BEARER_TOKEN**

./cli.py
```
Welcome to ZPA SCIM Tool
           [1] - Create User
           [2] - View All Users
           [3] - Delete User
           [4] - Create Group
           [5] - View All Groups
           [6] - Delete Group
           [7] - Exit
           
           Notes:
           UserID and GroupID entries should be the 'ZPA Internal ID'. Referenced as 'id' in API responses
           ExternalID is an arbitrary unique value used to track ID's in the source ID repository
           Make sure ExternalID is unique for each entry
```

## Why?
Someone had a requirement to temporarily create users in ZPA but they could not utilize their IdP due to access issues.

## How?
Just run `./cli.py` and follow the prompts. If you have note set the environment variables for ZPA_SCIM_BASE_URL and ZPA_SCIM_TOKEN you will be prompted to enter them prior to the menu displaying. You can get this information from your ZPA IdP config page under SCIM section.

This is not a full implementation of all API features just a simple tool to get around a temporary challenge.

## What else can i do?
The API calls are all defined in the `api.py` file. If you wanted to get more elaborate you could use this as a starting point for your project.

The SCIM API reference is available here: https://help.zscaler.com/zpa/scim-api-examples
