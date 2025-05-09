# Context:
I am trying to connect the backend to the  frontend of my application that called ULEM Grant Tracker System

# Tasks:
-	I want to modify the file named donors.html file <#file:donors.hmtl> to show all the donors’ information from API at https://ulem-grant-tracker-db.onrender.com/donors

# Examples or Formats:
Here is what the payload example looks like:
... json

[
    {
        "donor_type": "individual",
        "first_name": "John",
        "last_name": "Smith",
        "organization_name": null,
        "email": "john.smith@email.com",
        "phone": "555-123-4567",
        "address_line1": "123 Main St",
        "address_line2": "Apt 4B",
        "city": "New York",
        "state": "NY",
        "postal_code": "10001",
        "country": "USA",
        "preferred_contact_method": "email",
        "notes": "Regular donor since 2018, prefers quarterly communications",
        "id": 1,
        "created_at": "2025-05-05T15:43:35.585987Z",
        "updated_at": "2025-05-05T15:43:35.585987Z"
    },
  ...
]
 ...


Also modify the table headers of my donors.html page to show only donor ID, first name, last name, email, phone number and notes.

