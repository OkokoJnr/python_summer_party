import pandas as pd
# Define the dataset
data = {
    'group_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'created_date': [
        '2024-10-01', '2024-10-10', '2024-11-05', '2024-10-15',
        '2024-12-01', '2024-10-20', '2024-10-25', '2024-11-10',
        '2024-10-30', '2024-12-15', '2024-10-05', '2024-10-12'
    ],
    'total_messages': [100, 200, 150, 500, 120, 300, 400, 220, 450, 80, 600, 50],
    'participant_count': [25, 55, 40, 100, 35, 50, 60, 45, 80, 15, 90, 10]
}
# Create the DataFrame
whatsapp_group = pd.DataFrame(data)

# DAY ONE - You are a Product Analyst on the WhatsApp team investigating group messaging dynamics. Your team wants to understand how large groups are being used and their messaging patterns. You'll leverage data to uncover insights about group participation and communication behaviors.

        #TASK 1: DETERMINE WHATSAPP GROUP CREATED IN OCTOBER 2024
        # Convert 'created_date' to datetime
whatsapp_group['created_date'] = pd.to_datetime(whatsapp_group['created_date'])
october_2024_groups = whatsapp_group[(whatsapp_group['created_date'].dt.year == 2024) & (whatsapp_group['created_date'].dt.month == 10)]

        #TASK 2: What is the average number of participants in WhatsApp groups that were created in October 2024? This number will indicate the typical group size and inform our group messaging feature considerations.
        
october_2024_groups_avg = october_2024_groups['participant_count'].mean()


        #TASK 3: For WhatsApp groups with more than 50 participants that were created in October 2024, what is the average number of messages sent? This insight will help assess engagement in larger groups and support recommendations for group messaging features.
avg_messages_large_groups = october_2024_groups[october_2024_groups['participant_count'] > 50]['total_messages'].mean()
print(avg_messages_large_groups)        