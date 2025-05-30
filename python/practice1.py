# Example 1: Storing test user data
test_users = [
    {"username": "admin", "password": "admin123", "role": "administrator"},
    {"username": "user1", "password": "user123", "role": "regular"},
    {"username": "guest", "password": "guest123", "role": "guest"}
]
# Example 2: Browser configurations
browser_configs = {
    "chrome": {"driver_path": "/path/to/chromedriver", "headless": True},
    "firefox": {"driver_path": "/path/to/geckodriver", "headless": False}
}

browser_versions = {
    "chrome": "V8.0",
    "firefox": "V7.5",
    "safari": "V10.0"
}

website_urls = ["https://example.com/login", "https://example.com/dashboard", "https://example.com/profile"]

print(website_urls[0:])

print(f'your trying to access correct url {website_urls[0] == "https://example.com/login"}')

# Example 3: Test URLs
test_urls = (
    "https://example.com/login",
    "https://example.com/dashboard",
    "https://example.com/profile"
)
login,dashboard, profile = test_urls
print(login, dashboard, profile)


# Example 4: Expected vs Actual results comparison
expected_titles = {"Login Page", "Dashboard", "User Profile"}
actual_titles = {"Login Page", "Dashboard", "Settings"}
missing_titles = expected_titles - actual_titles

print(f"Missing titles: {missing_titles}")  
