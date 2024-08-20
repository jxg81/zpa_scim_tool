# ZPA and ZIA SCIM Tool
Simple tool to interface with the Zscaler ZPA and/or ZPA SCIM interface

> [!IMPORTANT]
> This utility are not affiliated with, nor supported by Zscaler in any way.

## TL;DR
pip install -r requirements.txt

export ZPA_SCIM_BASE_URL=**ZPA_SCIM_Service_Provider_Endpoint**

export ZPA_SCIM_TOKEN=**YOUR_ZPA_BEARER_TOKEN**

export ZIA_SCIM_BASE_URL=**ZIA_SCIM_Service_Provider_Endpoint**

export ZIA_SCIM_TOKEN=**YOUR_ZIA_BEARER_TOKEN**

./cli.py
```
        Welcome to ZIA/ZPA SCIM Tool
        [1] - ZPA SCIM Management
        [2] - ZIA SCIM Management
        [3] - Exit

        What would you like to do today?: 
```

## Why?
Someone had a requirement to temporarily create users in ZPA but they could not utilize their IdP due to access issues.

## How?
Just run `./cli.py` and follow the prompts. If you have not set the environment variables for ZIA/ZPA_SCIM_BASE_URL and ZIA/ZPA_SCIM_TOKEN you will be prompted to enter them after selecting ZIA or ZPA management. You can get this information from your ZIA and/or ZPA IdP config page under SCIM section.

This is not a full implementation of all API features just a simple tool to get around a temporary challenge.

## What else can i do?
The API calls are all defined in the `api.py` file. If you wanted to get more elaborate you could use this as a starting point for your project.

The SCIM API reference is available here: https://help.zscaler.com/zpa/scim-api-examples and here: https://help.zscaler.com/zia/scim-api-examples
