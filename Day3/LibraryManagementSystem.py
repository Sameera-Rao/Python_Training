library = []

def add_item():
    title = input("Enter item title:")
    item_type = input("Enter item type (Book/Magazine/DVD):")

    item_id = input("Enter item ID:")

    item = {
        "title": title,
        "type": item_type,
        "id": item_id,
        "status": "Available"
    }

    if item_type=="book":
        item["author"]=input("Enter author name:")

    elif item_type=="magazine":
        item["publisher"]=input("Enter publisher name:")

    elif item_type=="dvd":
        item["director"]=input("Enter director name:")

    else:
        print("Invalid item type.")
        return

    library.append(item)
    print("Item added successfully.")


def display_items():
    print("Library Items:")
    for item in library:
        print(f"ID: {item['id']}")
        print(f"Title: {item['title']}")
        print(f"Type: {item['type']}")
        print(f"Status: {item['status']}")

        if item["type"]=="book":
            print(f"Author:{item['author']}")
        elif item["type"]=="magazine":
            print(f"Publisher: {item['publisher']}")
        elif item["type"].lower() == "dvd":
            print(f"Director: {item['director']}")

        print()


def check_out_item():
    item_id = input("Enter item ID to check out:")

    for item in library:
        if item["id"] == item_id:
            if item["status"] =="Available":
                item["status"] ="Checked Out"
                print("\nItem checked out successfully.")
            else:
                print("Item is already checked out.")
            return

    print("Item not found.")


def return_item():
    item_id = input("Enter item ID to return:")

    for item in library:
        if item["id"] == item_id:
            if item["status"] =="Checked Out":
                item["status"] ="Available"
                print("Item returned successfully.")
            else:
                print("Item was not checked out.")
            return

    print("Item not found.")
num_items = int(input("Enter number of library items:"))

for _ in range(num_items):
    add_item()

display_items()
check_out_item()
return_item()
display_items()
