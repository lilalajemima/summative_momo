import xml.etree.ElementTree as ET
import os

# Create the directory for the files containing the categorized data
os.makedirs('Categorised_Data', exist_ok=True)

# Check for raw data from the xml file to parse it
tree = ET.parse(r'C:\Users\lilal\Intranet\summative_momo\back_end\modified_sms_v2.xml')
root = tree.getroot()

# Lists for the categorized data
incoming_money = []
payment_to_code = []
transfer_to_number = []
withdrawals_from_agents = []
bank_deposits = []
third_party_transactions = []
Airtime_purchases = []
Internet_and_voice_bundles = []
cash_power_purchases = []
miscellaneous_messages = []

# For loop to act as a search bar with if conditions
for element in root:
    if 'body' in element.attrib:
        body_text = element.attrib['body'].lower()
        message_xml = ET.tostring(element, encoding='unicode')

        # 1️⃣ Directly Received Money
        if 'received' in body_text:
            incoming_money.append(message_xml)

        # 2️⃣ Transfers (Check for both "transfer" and "fee was:")
        elif 'transfer' in body_text and 'fee was:' in body_text:
            transfer_to_number.append(message_xml)

        # 3️⃣ Payment Transactions (Not a failed payment)
        elif 'payment' in body_text and 'failed' not in body_text:
            if 'mtn cash power' in body_text:
                cash_power_purchases.append(message_xml)  # Now specifically checks for MTN Cash Power
            elif 'airtime' in body_text:
                Airtime_purchases.append(message_xml)
            elif 'bundles and packs' in body_text:
                Internet_and_voice_bundles.append(message_xml)
            elif 'fee was 0 rwf.':
                payment_to_code.append(message_xml)

        # 4️⃣ Third Party Transactions (Check for " a transaction of ")
        elif ' a transaction of ' in body_text:
            third_party_transactions.append(message_xml)

        # 5️⃣ Bank Deposits (Checking for " A bank deposit of ")
        elif ' a bank deposit of ' in body_text:
            bank_deposits.append(message_xml)

        # 6️⃣ Withdrawals
        elif 'withdraw' in body_text:
            withdrawals_from_agents.append(message_xml)

        # 7️⃣ Catch-All Miscellaneous (Least Specific)
        else:
            miscellaneous_messages.append(message_xml)

# Create files for the categorized data's lists
def organise_data_in_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(item)

# Call the function to create the files for the categorized data
organise_data_in_file('Categorised_Data/incoming_money.xml', incoming_money)
organise_data_in_file('Categorised_Data/payment_to_code.xml', payment_to_code)
organise_data_in_file('Categorised_Data/transfer_to_number.xml', transfer_to_number)
organise_data_in_file('Categorised_Data/withdrawals_from_agents.xml', withdrawals_from_agents)
organise_data_in_file('Categorised_Data/bank_deposits.xml', bank_deposits)
organise_data_in_file('Categorised_Data/third_party_transactions.xml', third_party_transactions)
organise_data_in_file('Categorised_Data/Airtime_purchases.xml', Airtime_purchases)
organise_data_in_file('Categorised_Data/cash_power_purchases.xml', cash_power_purchases)
organise_data_in_file('Categorised_Data/miscellaneous_messages.xml', miscellaneous_messages)
