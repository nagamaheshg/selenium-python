from networkx import number_of_nodes


browsers = ['chrome', 'firefox', 'safari', 'edge', 'opera']

urls = ("shoping/login", "shoping/dashbord")

user = {"user_name":"nagamaheshg", "passoword":"Admin@123", "role":"Admin"}


for browser in browsers:
    
    print(browser)
print("="*30)

for url in urls:
    print(url)
    
print("="*30)

for user_name, password in user.items():
    print(user_name)
    print(password)

else:
    print("Another data")
    
for num in range(9):
    print(num)


count = 0

while count < 3:
    number_of_tries =  count
    print(number_of_tries)
    count += 1
    

max_num_tries = 3
current_num_tries = 0
success = False

while current_num_tries < max_num_tries and not success:
    
    print(f'Attempting login... (Attempt {current_num_tries + 1})')
    
    login_result = True

    if login_result:
        success = True
        print("Login Successful!")
    
    else:
        current_num_tries += 1
        print("Login Failed, retrying...")
        
if not success:
    print("Max retries reached. Login failed")


test_data = ["valid_data", "invalid_data", "corrupted_data", "more_data"]
for data in test_data:
 if data == "corrupted_data":
    print("Corrupted data found, stopping tests")
    break
 print(f"Processing: {data}")
 
# continue - skips to next iteration
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Odd numbers only:")
for num in numbers:
    if num % 2 == 0: 
        continue
    print(num)