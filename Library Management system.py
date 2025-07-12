from BookInventory import BookInventory
BI=BookInventory()
BI.json_loader()

print("""Welcome to the Library Management System
      1.For Lending  books
      2.For Book returns
      3.To enter Inventory Management System
      4.For checking history
      5.For Exit\n""")
while True:
      x=int(input("Enter your choice: "))

      if x==1:
            BI.lend_book(input("Enter Book ID: "))
      elif x==2:
            BI.return_book(input("Enter Book ID: "))
      elif x==3:
            while True:
                  print("""Welcome to Inventory Management
                  PLease Choose an option:
                  1.For Adding a book
                  2.For Displaying the inventory
                  3.For Saving the inventory to JSON file
                  4.For Displaying the inventory from JSON file
                  5.For Exit\n""")
                  y=int(input("Enter your choice: "))
                  match y:
                        case 1:
                              BI.add_book(input("Enter Book ID: "), input("Enter Book Title: "), input("Enter Author Name: "), int(input("Enter Total Copies: ")))
                        case 2:
                              BI.display()
                        case 3:
                              BI.json_saver()
                        case 4:
                              BI.display_inventory()
                        case 5:
                              print("Exiting Inventory Management")
                              break
      elif x==4:
            BI.display_inventory()
      elif x==5:
            BI.json_saver()
            print("Saving changes and Exiting the Library Management System")
            break