#1. Create a grade calculator that takes a list of scores and assigns grades using if/elif/else 

grades = [85, 90, 70, 60, 75, 55,35, 45]
grades_result = []

for grade in grades:
    
    
    if 90 <= grade <= 100:
        grades_result.append("A+")
        
    elif 80 <= grade < 90:
        grades_result.append("A")
        
    elif 70 <= grade < 80:
        grades_result.append("B")
    
    elif 60 <= grade < 70:
        grades_result.append("C")
    
    elif 50 <= grade < 60:
        grades_result.append("D")
    
    elif 40 <= grade < 50:
        grades_result.append("E")
        
    else:
        grades_result.append("Fail")

print(grades)
print(grades_result)
print('-'*40)

emails_list = ["g.nagamahesh62@gmail.com", "nagamaheshgatta@gmail.com", "gattanagamahesh62@gmail.com", "gnmahesh"]

for email in emails_list:
    
    if '@' not in email:
        print(f"Invalid Email format {email}")
        
    else:
        print(f'Valid Email Address: {email}')

print('-'*40)

def execute_flaky_test(test_name, max_retry = 3):
    
    for attempt in range(1, max_retry+1):
        
        print(f'Executing {test_name} Test - Attempt(attempt)')
        import random
        test_result = random.choice([True, False])
        
        if test_result:
            print(f'{test_name} Test PASSED on Attempt({attempt})')
            return True
        else:
            
            print(f'Executing {test_name} Test Failed on {attempt}')
            if attempt < max_retry:
                print('Retrying...')
            
            else:
                 print(f"{test_name} Failed after {max_retry} attempts")

test_cases = ['Login','Navigation','Submission']

for test_case in test_cases:
    
    success = execute_flaky_test(test_case)
    
    if not success:
        print(f"{test_case} test require manual investigation")
    
    print("-"*40)

test_scenarios = [
 {"name": "Valid Login", "username": "admin", "password": "admin123",
"expected": "success"},
 {"name": "Invalid Username", "username": "wrong", "password": "admin123",
"expected": "failure"},
 {"name": "Invalid Password", "username": "admin", "password": "wrong",
"expected": "failure"},
 {"name": "Empty Fields", "username": "", "password": "", "expected":
"failure"}]        

for scenario in test_scenarios:
    
    print(f'\nExecuting: {scenario['name']}')
    
    if scenario['username'] == 'admin' and scenario['password'] == 'admin123':
        result = 'success'

    
    else:
        result = 'failure'
        
    if scenario['expected'] == result:
        print(f'{scenario['name']} - PASSED')
    
    else:
         print(f" {scenario['name']}: FAILED (Expected: {scenario['expected']}, Got: {result}")