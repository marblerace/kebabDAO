import re

# Define the file paths
data_file = 'data.txt'
output_file = 'kebabs.html'

# Read the file contents
with open(data_file, 'r') as file:
    content = file.read()

# Split the content into entries based on the pattern
entries = content.split('Restaurant Name:')

# Define a pattern to extract data
pattern = re.compile(r'''
    \s*(?P<name>.+?)\s*
    Location:\s*(?P<location>.+?)\s*
    Rating\sS:\s*(?P<ratingS>\d*\.?\d*)\s*
    Rating\sJ:\s*(?P<ratingJ>\d*\.?\d*)\s*
    Comments:\s*(?P<comments>.*)\s*
    Image:\s*(?P<image>.+?)\s*
    ''', re.VERBOSE)

# HTML content
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Kebab Places</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        .restaurant {
            margin-bottom: 40px; /* Space between restaurant entries */
        }
        img {
            max-width: 400px;
            height: auto;
            display: block;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h2>Kebab Places</h2>
    <div id="restaurants">
'''

# Parse each entry
for entry in entries:
    if not entry.strip():
        continue

    match = pattern.search(entry)
    if match:
        name = match.group('name').strip()
        location = match.group('location').strip()
        image = match.group('image').strip()

        # Append to the HTML content
        html_content += f'''
        <div class="restaurant">
            <h3>{name}</h3>
            <p>{location}</p>
            <img src="{image}" alt="{name}">
        </div>
        '''

html_content += '''
    </div>
</body>
</html>
'''

# Write the HTML content to the output file
with open(output_file, 'w') as file:
    file.write(html_content)

print("kebabs.html has been updated.")
