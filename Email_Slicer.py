#Get user email address
email = input("What is your email address: ").strip()

#slice out username

username = email[:email.index("@")]

#slice domain name

domain = email[email.index("@") + 1 :]

#output message

Output = "Your username is {} and your domain name is {}.".format(username , domain)

print(Output)