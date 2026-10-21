from pyscript import document

# Members in each grade
grade_7 = {'Ladis Wushurum', 'Aliso Borgor'}
grade_8 = {'Max Ocupancy', 'Sponge Square'}
grade_9 = {'Patricia Star', 'Patrica Skye'}
grade_10 = {'Nick Gurt', 'The Raver'}

# Members added using the webpage
new_members = set()


def add_member(event):
    first_name = document.getElementById('first-name').value
    last_name = document.getElementById('last-name').value

    new_members.add(f'{first_name} {last_name}')

    # Combine all the sets
    members = grade_7 | grade_8 | grade_9 | grade_10 | new_members

    # Show the member list and total
    document.getElementById('output').innerHTML = ( f'{members}<br>Total Members: {len(members)}')
