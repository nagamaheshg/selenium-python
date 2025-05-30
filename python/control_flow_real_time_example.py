


form_data = {
    "user_name": "testuser",
    "email": "test@example.com",
    "password": "password123",
    "confirm_password": "password1234"
}

validation_errors = []

if not form_data['user_name']:
    validation_errors.append("User Name is Required")
    
elif len(form_data["user_name"]) < 3:
    validation_errors.append("User Name must be at least 3 characters")
    
if '@' not in form_data['email']:
    validation_errors.append("Invalid email format")
    
if len(form_data['password']) < 8:
    validation_errors.append("password must be at least 8 characters")
    
if form_data["password"] != form_data["confirm_password"]:
    validation_errors.append("Password Must be match")
    

if validation_errors:
    print("validation failed")
    for error in validation_errors:
        print(f'- {error}')

else:
    print('All Validation Passed')

browsers = ["Chrome", "Firefox", "Edge"]
test_urls = [
 "https://example.com/login",
 "https://example.com/dashboard",
 "https://example.com/profile"
]

test_results = []

for browser in browsers:
    
    print(f'\n--Testing with {browser}')
    for url in test_urls:
        
        print(f'Test URL: {url}')
        
        # simulate test execution
        test_passed = True

        if test_passed:
            result = f"{browser} - {url}: PASSED"
        
        else:
            result = f"{browser} - {url}: FAILED"
            
        test_results.append(result)
        print(result)
        
print("\n---Test Summary----")

passed_tests = [result for result in test_results if "PASSED" in result]
failed_tests = [result for result in test_results if "FAILED" in result]
print(f"Total Tests: {len(test_results)}")
print(f"Passed: {len(passed_tests)}")
print(f"Failed: {len(failed_tests)}")


test_urls = ["http://site1.com", "https://site2.com", "http://site3.com"]

secure_urls = [secure_url for secure_url in test_urls if secure_url.startswith('https')]

for url in secure_urls:
    print(url.upper())
    
domain_name  = [url.split("//")[1] for url in test_urls]

print(domain_name)

test_scenarios = [
    {"name":"valid login", "user_name":"admin","password":"admin@123","expected":"success"},
    {"name":"Invalid login", "user_name":"wrong","password":"admin123","expected":"failure"},
    {"name":"Invalid Password", "user_name":"admin","password":"wrong","expected":"failure"},
    {"name":"Empty fields", "user_name":"","password":"","expected":"failure"},
    
]

for scenario in test_scenarios:
    
    print(f'\nExecuting: {scenario["name"]}')
    
    if scenario['user_name'] == 'admin' and scenario["password"] == 'admin@123':
        result = 'success'
        
    else:
        result = 'failure'
    
    if scenario['expected'] == result:
        print(f'{scenario['name']} - PASSED')
    
    else:
         print(f" {scenario['name']}: FAILED (Expected: {scenario['expected']}, Got: {result}")

environments = {
    "dev": {"url":"https://dev.example.com", "timeout": 30},
    "staging": {"url":"https://staging.example.com", "timeout": 45},
    "prod": {"url":"https://example.com", "timeout": 60},
    
    
}

current_env = 'dev'

if current_env in environments:
    
    config = environments[current_env]
    print(f'Running test on {current_env} environment')
    print(f"URL: {config['url']}")
    print(f"TimeOut: {config['timeout']} seconds")

else:
    print(f'Unknown environment: {current_env}')
    print(f'Available environments: ', list(environments.keys()))
    

def execute_test_with_retry(test_name, max_retries=3):
    
    for attempt in range(1, max_retries+1):
        
        print(f'Executing {test_name} - Attempt({attempt})')  
        
        # # Simulate test execution (replace with actual test)
        import random
        test_result = random.choice([True, False])
        
        if test_result:
             print(f"{test_name} PASSED on attempt {attempt}")
             return True
        
        else:
             print(f"{test_name} Failed on attempt {attempt}")
             if attempt < max_retries:
                 print("Retrying...")
            
             else:
                 print(f"{test_name} Failed after {max_retries} attempts")
                 

test_cases = ["Login Test", "Navigation Test", "Form Submission Test"]

for test_case in test_cases:
    
    success = execute_test_with_retry(test_case)
    if not success:
        print(f'{test_case} requires manual investigation')
    print('-'*40)
    
            