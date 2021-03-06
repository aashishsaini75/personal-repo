# import random
# import time
#
# for i in range(10):
#     var = random.randint(7017000000,7017999999 )
#     print(var)
#     time.sleep(1)

import random
domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]

def get_random_domain(domains):
    return random.choice(domains)

def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_emails(nb, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]

def main():
    print(generate_random_emails(10, 7))

if __name__ == "__main__":
    main()



