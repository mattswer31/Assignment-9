# opens a ticket with name and their issue with default status open.
# automatically assigns an ID based on length of tickets list
def open_ticket(helpdesk, name, issue):
    index = str(len(helpdesk) + 1)
    while len(index) < 3:
        index = '0' + index
    id = "Ticket" + index
    helpdesk.update({id : {"Customer" : name, "Issue" : issue, "Status": "open"}})
    print(f"{id} of Customer: {name} with Issue: {issue} added successfully.")

# updates a ticket to closed status or reopens it
def update_ticket(helpdesk, ticket_id):
    if ticket_id in helpdesk:
        if helpdesk[ticket_id]["Status"] == "open":
            helpdesk[ticket_id]["Status"] = "closed"
            print(f"{ticket_id} successfully closed.")
        else:
            helpdesk[ticket_id]["Status"] == "open"
            print(f"{ticket_id} successfully reopened.")
    else:
        print(f"Could not find ticket: {ticket_id}.")

# displays a formatted list of all tickets
def display_tickets(helpdesk):
    for ticket in helpdesk:
        current = helpdesk[ticket]
        if current["Status"] == "open":
            print(f"{ticket}:\nName: {current["Customer"]}\nIssue: {current["Issue"]}\nStatus: {current["Status"]}\n")
    for ticket in helpdesk:
        current = helpdesk[ticket]
        if current["Status"] == "closed":
            print(f"{ticket}:\nName: {current["Customer"]}\nIssue: {current["Issue"]}\nStatus: {current["Status"]}\n")

