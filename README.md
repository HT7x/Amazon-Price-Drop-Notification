# Amazon Price Tracker

This Python script monitors the price of Amazon products and sends an email notification if the price drops below a specified threshold.

## Features

- Monitors multiple Amazon product URLs.
- Sends email notifications when the price drops below the set threshold.
- Logs all activities to a file for easy debugging and tracking.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`, `lxml`, `yagmail`

## Setup

1. Clone the repository or download the script.
2. Install the required Python packages:
    ```bash
    pip install requests beautifulsoup4 lxml yagmail
    ```
3. Create a `config.json` file in the same directory as the script with the following content:
    ```json
    {
        "email": "your_email@example.com",
        "password": "your_email_password"
    }
    ```
   Replace `your_email@example.com` with the email address you wish to send notifications from, and `your_email_password` with the email account's password.

## Configuration

Edit the section of the script to add the Amazon product URLs and their corresponding price thresholds:
```python
######### Change only this section #########
# Add the url and the corresponding threshhold price for the amazon product, comma separated (The two products are examples)
url_price = {
    "https://a.co/d/0dlwWeDl" : 30, 
    "https://a.co/d/0irn96jy" : 60
}
# email address you want to recieve the notification from
rec_email = "ht.bh@live.com"
############################################
```
## Usage

You can run the script directly:

```bash
python main.py
```
Alternatively, you can use the provided run_script.sh for ease of execution:

1. Ensure run_script.sh has the following content:
```bash
#!/bin/bash
python3 main.py
```
2. Make the run_script.sh executable:
```bash
chmod +x run_script.sh
```
3. Run the script:
```bash
./run_script.sh
```
The script will continuously monitor the specified Amazon product URLs and send an email notification to rec_email if any product's price drops below the set threshold.

## Logging

The script logs all activities to output.log for easy tracking and debugging.

## Automate with Cron Job

To automate the script to run daily, you can set up a cron job. Here are the steps:

1. Open your crontab file for editing:

```bash
crontab -e
```
2. Add the following line to schedule the script to run every day at a specific time (e.g., 7:00 AM):

```bash

0 7 * * * /path/to/your/run_script.sh
```
Replace /path/to/your/run_script.sh with the actual path to your run_script.sh file.

Save and close the crontab file.

This will ensure that the script runs every day at the specified time, checking the prices and sending notifications if necessary.

## Important Notes

* Make sure your email provider allows sending emails from external applications. You might need to enable "less secure apps" if using Gmail.
* Use a dedicated email account for this script to avoid exposing your primary email account.
* This script is written specifically for sending emails from gmail. This might not be compatible with other email providers. 
* Run this on the cloud for better automation. 

## License

This project is licensed under the MIT License.
