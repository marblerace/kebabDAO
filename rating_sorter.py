# Define the file paths
data_file = 'data.txt'
rating_file = 'rating.txt'

# Read the file contents
with open(data_file, 'r') as file:
    content = file.readlines()

# Write the contents to the rating.txt file
with open(rating_file, 'w') as file:
    file.writelines(content)

# Ensure the file write is complete
print("rating.txt has been updated with the contents of data.txt.")
