# Match Statement -> Switch in java

#match variable
# case patten1:
#       code of block
# case patten2:
#       code of block

#Write a program to ask the user which browser he wants to run automation.

browser_name = input("Enter your Browser_name\n")
match browser_name:
    case"firefox":
        print("Starting firefox")
    case "chrom":
        print("Starting firefox")
    case"edge":
        print("Starting firefox")
    case _:  # _ Default if nothing match
        print("Browser Not Found!")




