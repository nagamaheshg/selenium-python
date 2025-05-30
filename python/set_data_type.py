unique_number = {1, 2, 3, 4, 5, 6,7,8,9,10}
duplicate_numbers = {1,1,2,2,3,3}
print(unique_number)
print(duplicate_numbers)

browsers = {"Chrome", "Firefox", "Safari"}
browsers.add('edge')
browsers.remove('Safari')
print(browsers)

test_env_browsers = {"Chrome", "Firefox"}
prod_env_browsers = {"Chrome", "Firefox", "Safari", "Edge"}

print(test_env_browsers.intersection(prod_env_browsers))
print(prod_env_browsers.difference(test_env_browsers))
uat_env_browsers = test_env_browsers.union(prod_env_browsers)

print(uat_env_browsers)