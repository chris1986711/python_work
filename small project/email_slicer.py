email = input("What is your email address?: ").strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
output = "username is '{}' domain name is '{}'".format(user_name,domain_name)
print(output)