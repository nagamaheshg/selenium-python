def create_profile(name, age, email, is_active=True):
    profile = {
        "name":name,
        "age": age,
        "email": email,
        "is_active": is_active
    }
    
    return profile

user1 = create_profile("Mahesh", 30, 'nagamaheshgatta@gmail.com')
user2 = create_profile("Narasimha", 24, 'narasimha@gmail.com')

print(user1)
print(user2)

# Function with default parameters
def wait_for_element(timeout=10, poll_frequency=0.5):
    print(f"Waiting for element with timeout: {timeout}s, polling every {poll_frequency}s")
    return True

# Different ways to call
wait_for_element() # Uses all defaults
wait_for_element(20) # timeout=20, poll_frequency=0.5
wait_for_element(15, 1.0) # timeout=15, poll_frequency=1.0
wait_for_element(poll_frequency=0.2) # timeout=10, poll_frequency=0.2

def run_multiple_tests(*args):
    
    print(f'\nExecuting number of testcases {len(args)}')
    print(list(args))
    for testcase in args:
    
        print(f'Executing {testcase}')
        

run_multiple_tests('Login Test', 'Navigation Test', 'Submitting Test')

def configure_browser(**options):
    
    print("Browser configuration:")
    for key, value in options.items():
        print(f"- {key}: {value}")

configure_browser(headless=True, window_size="1920x1080", timeout=30)

def execute_test(test_name, *test_data, **config):
    print(f"Executing test: {test_name}")
    print(f"Test data: {test_data}")
    print(f"Configuration: {config}")
    
execute_test("login_test", "user1", "password123", browser="chrome",
headless=True)

# Lambda function syntax
square = lambda x: x ** 2
print(square(5)) # Output: 25
# Lambda with multiple parameters
multiply = lambda x, y: x * y
print(multiply(3, 4)) # Output: 12

# Practical use with built-in functions
test_results = [
 {"name": "test1", "duration": 2.5, "status": "passed"},
 {"name": "test2", "duration": 1.8, "status": "failed"},
 {"name": "test3", "duration": 3.2, "status": "passed"}
]

# Sort by duration using lambda
sorted_by_duration = sorted(test_results, key=lambda x: x["duration"])

print("Tests sorted by duration:")

for test in sorted_by_duration:
    print(f"{test['name']}: {test['duration']}s")
    
# Filter passed tests using lambda
passed_tests = list(filter(lambda x: x["status"] == "passed", test_results))
print(passed_tests)
print(f"\nPassed tests: {len(passed_tests)}")

def login_user(username, password, remember_me=False):
    
    print(f"Attempting login for user: {username}")
    valid_credentials = {"admin": "admin123", "user": "user123"}
    
    if(username in valid_credentials and valid_credentials[username] == password):
        
        result = {
            "success": True,
            "message": "Login Successfully",
            "remember_me": remember_me,
            "user_name":  username
        }
        
    else:
        
        result = {
            "success": False,
            "message": "Login Failed",
            "remember_me": False,
            "user_name":  username
        }
    
    print(f"{result['message']}")
    return result

user1 = login_user('admin', 'admin123', remember_me=True)
user2 = login_user('user', 'user123',  remember_me=False)
print(user1)

if user1['success']:
    print(f'welcome {user1['user_name']}')

print('-'* 40)  

def find_element_with_retry(locator, locator_type="id", max_retries=3, wait_time=1):
    
     import time
     for attempt in range(1, max_retries + 1):
         print(f"Attempt {attempt}: Looking for element by {locator_type} ='{locator}'")
         element_found = attempt >= 2 
           
         if element_found:
            print(f" Element found on attempt {attempt}")
            return {"found": True, "attempts": attempt}
        
         else:
                print(f" Element not found, waiting {wait_time}s...") 
                time.sleep(wait_time)
    
     print(f" Element not found after {max_retries} attempts")
     return {"found": False, "attempts": max_retries}
        
def click_element(locator, locator_type="id"):
    """
    Click an element after finding it
    """
    element_result = find_element_with_retry(locator, locator_type,1)

    if element_result["found"]:
        print(f"Clicking element: {locator}")
        return True
    else:
        print(f"Cannot click element: {locator} - not found")
        return False
# U
click_element("submit-button", "id")

print("-"*40)

def load_test_data(data_type):
    
    test_data = {
            "users": [
            {"username": "admin", "password": "admin123", "role":
            "administrator"},
            {"username": "user1", "password": "user123", "role": "regular"},
            {"username": "guest", "password": "guest123", "role": "guest"}
            ],
            "urls": {
            "login": "https://example.com/login",
            "dashboard": "https://example.com/dashboard",
            "profile": "https://example.com/profile"
            },
            "browsers": ["Chrome", "Firefox", "Edge"]
        }

    return test_data.get(data_type, [])

def get_user_by_role(role):
    """
    Get user data by role
    """
    users = load_test_data("users")
    for user in users:
        if user["role"] == role:
            return user
    return None

def get_by_browser(browser_name):
    """
    Get user data by role
    """
    browsers = load_test_data("browsers")
    for browser in browsers:
        if browser == browser_name:
            print(browser)
        else:
            print('No Browser Data found')

admin_user = get_user_by_role("administrator")
print(f"Admin user: {admin_user}")
test_urls = load_test_data("urls")
print(f"Login URL: {test_urls['login']}")   

get_by_browser('chrome')

print('-'*40)

import time

def execute_test_case(test_name, test_function, *args, **kwargs):
    """
    Execute a test case and capture results
    """
    print(f"\n--- Executing: {test_name} ---")
    start_time = time.time()

    try:
        result = test_function(*args, **kwargs)
        end_time = time.time()
        duration = round(end_time - start_time, 2)

        test_result = {
            "name": test_name,
            "status": "PASSED" if result else "FAILED",
            "duration": duration,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        end_time = time.time()
        duration = round(end_time - start_time, 2)

        test_result = {
            "name": test_name,
            "status": "ERROR",
            "duration": duration,
            "error": str(e),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

    print(f"Result: {test_result['status']} ({test_result['duration']}s)")
    return test_result

def simulate_login_test():
    """Sample test function"""
    time.sleep(1)  # Simulate test execution time
    return True

def simulate_failing_test():
    """Sample failing test function"""
    time.sleep(0.5)
    return False

# Execute tests
results = []
results.append(execute_test_case("Login Test", simulate_login_test))
results.append(execute_test_case("Navigation Test", simulate_failing_test))

# Generate summary
def generate_test_summary(test_results):
    """
    Generate summary of test results
    """
    total_tests = len(test_results)
    passed_tests = len([r for r in test_results if r["status"] == "PASSED"])
    failed_tests = len([r for r in test_results if r["status"] == "FAILED"])
    error_tests = len([r for r in test_results if r["status"] == "ERROR"])
    total_duration = sum([r["duration"] for r in test_results])

    summary = {
        "total": total_tests,
        "passed": passed_tests,
        "failed": failed_tests,
        "errors": error_tests,
        "total_duration": round(total_duration, 2),
        "pass_rate": round((passed_tests / total_tests) * 100, 2) if total_tests > 0 else 0
    }

    return summary

summary = generate_test_summary(results)
print(f"\n--- Test Summary ---")
print(f"Total Tests: {summary['total']}")
print(f"Passed: {summary['passed']}")
print(f"Failed: {summary['failed']}")
print(f"Errors: {summary['errors']}")
print(f"Pass Rate: {summary['pass_rate']}%")
print(f"Total Duration: {summary['total_duration']}s")
