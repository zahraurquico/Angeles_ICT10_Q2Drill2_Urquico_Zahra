from js import document

grade7 = {"Ana Reyes", "Ben Cruz", "Carla Santos"}
grade8 = {"Daniel Lim", "Ella Garcia", "Frank Tan"}
grade9 = {"Grace Lee", "Henry Ong", "Ivy Torres"}
grade10 = {"Jake Dizon", "Kara Mendoza", "Liam Bautista"}

complete_set = grade7 | grade8 | grade9 | grade10

def show_members():
    document.getElementById("output").innerHTML = f"""
        <h2>ALL CLUB MEMBERS</h2>
    <ul>
        {"".join(map(lambda name: f"<li>{name}</li>", sorted(complete_set)))}
    </ul>
    <h3>Total Members: {len(complete_set)}</h3>
    """

def add_member(event):

    first = document.getElementById("first-name").value
    last = document.getElementById("last-name").value

    new_mem = first + " " + last

    complete_set.update({new_mem})

    show_members ()

show_members()
