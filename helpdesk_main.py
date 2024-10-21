import helpdesk

# pre-initialized ticket list
tickets_list = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

print(f"Welcome to Matt's HelpDesk!")
print(f"Input '1' to open a ticket\nInput '2' to update a ticket\nInput '3' to display all tickets\nInput '4' to close this program")
# while loop to control user input
while True:
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Name of person?")
        issue = input(f"Describe the issue {name} is having.")
        helpdesk.open_ticket(tickets_list, name, issue)
    elif choice == '2':
        ticket_id = input("Input ID of ticket to close/reopen.")
        helpdesk.update_ticket(tickets_list, ticket_id)
    elif choice == '3':
        helpdesk.display_tickets(tickets_list)
    elif choice == '4':
        print("Thank you for using Matt's HelpDesk!")
        break
    else:
        print(f"{choice} is not a valid action.")