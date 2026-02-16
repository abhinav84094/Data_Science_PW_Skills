# # Task 1 – Clean and Inspect the Raw String

# iphone_version = "iPhone_15_Pro_Max_V1.0_release"
# print("Length of the string:", len(iphone_version))
# print("Position of 'Pro':", iphone_version.find("Pro"))
# sliced_string = iphone_version[7:17]
# print("Sliced string (7 to 20):", sliced_string)
# uppercase_string = iphone_version.upper()
# print("Uppercase string:", uppercase_string)
# lowercase_string = iphone_version.lower()
# print("Lowercase string:", lowercase_string)    
# print()
# print()






# #Task 2 – Format and Update the Version Name

# formatted_string = iphone_version.replace("_", " ")
# print("Formatted string:", formatted_string)
# updated_string = formatted_string.replace("V1.0", "V1.1")
# print("Updated string:", updated_string)
# print("V1.1" in updated_string)
# print("Original String : ", iphone_version)
# print("Updated String : ", updated_string)
# print()
# print()






# #Task 3 – Add Regional Code and Convert Style

# regional_string = iphone_version + "_IN"
# print("Regional string:", regional_string)
# split_string = regional_string.split("_")
# print("Split string:", split_string)
# pascal_string = "".join(split_string)
# print(pascal_string)
# print(" ".join(iphone_version.split("_")).upper())
# print()





# #Task 4 – Generate a Version Release Log

# today_date = "2025-10-11"
# release_log = f"New version {iphone_version} released on {today_date}"

# print(release_log)

# print(release_log.title())

# print(len(release_log.split(" ")))

# print()
# print()





# #Task 5 – Summarize and Extract Core Details
# versions = [
#     "iPhone_15_Pro_Max_V1.0_release",
#     "iPhone_15_Pro_Max_V1.1_IN",
#     "iPhone_15_Pro_Max_V1.2_US",
#     "iPhone_15_Pro_Max_V2.0_EU"
# ]

# version_number = []
# i=0
# for version in versions:
#     parts = version.split("_")
#     version_number.append(parts[4])


# print(version_number)
# region_count = {}
# for version in versions:
#     if version.endswith("_IN"):
#         region_count["IN"] = region_count.get("IN", 0) + 1
#     elif version.endswith("_US"):
#         region_count["US"] = region_count.get("US", 0) + 1
#     elif version.endswith("_EU"):
#         region_count["EU"] = region_count.get("EU", 0) + 1
#     else:
#         region_count["Other"] = region_count.get("Other", 0) + 1

# print(region_count)

# latest_version = max(version_number)
# print("Latest version:", latest_version)

# latest_version_reagon = "" 
# for version in versions:
#     if latest_version in version:
#         latest_version_reagon = version.split("_")[-1]

# print(f'''
#       Model Name: {sliced_string}
#       Latest Version: {latest_version}
#       Region : {latest_version_reagon}
#       Total Version Realsed: {len(versions)}

# ''')
# print()









# # 1. String Task: Format Patient Name Properly
# doctor_name = "dr. rAj mEhta"
# formatted_name = doctor_name.title()
# print("Formatted Patient Name:", formatted_name)


# # 2. String Task: Create Patient ID
# patient_name = "Anjali Verma"  
# year = 2025
# patient_id = f"{patient_name.split()[0].upper()}{patient_name.split()[1][0].upper()}{year}"
# print("Patient ID:", patient_id)

# #3. List Task: Add New Medicines to Inventory
# medicine =  ["Paracetamol", "Ibuprofen"]
# new_medicines = ["Amoxicillin", "Cetrizine"]
# medicine.extend(new_medicines)
# print("Updated Medicine Inventory:", medicine)

# #4. List Task: Remove Discontinued Medicines
# discontinued_medicines = "Amoxicillin"
# medicine.remove(discontinued_medicines)
# print("Medicine Inventory after Removal:", medicine)


# #5. Tuple Task: Store Patient Vital Signs
# vital_signs = (98.6, 120, 80)
# Temperature = str(vital_signs[0])+ "F"
# print("Temperature:", Temperature)
# BP_Systolic = str(vital_signs[1]) + " mmHg"
# print("BP Systolic:", BP_Systolic)
# BP_Diastolic = str(vital_signs[2]) + " mmHg"    
# print("BP Diastolic:", BP_Diastolic)


# #6. Tuple Task: Identify Room Details
# Room = ("Room No 302", "ICU", "Available")
# print(f"""
#       Room Number: {Room[0]}
#       Type: {Room[1]}
#       Status: {Room[2]}""")

# #7. Set Task: Track Unique Doctors on Duty*
# docotors = {"Dr. A", "Dr. B", "Dr. C"}
# new_doctor = "Dr. D"
# docotors.add(new_doctor)
# print(docotors)

# #8. Set Task: Find Common Doctors between Two Shifts
# morning_shift = {"Dr. A", "Dr. B"}
# evening_shift = {"Dr. B", "Dr. C"}
# print(morning_shift & evening_shift)

# #9. String + List Task: Split Patient Full Name
# name = "Rajesh Kumar Gupta"
# li = list(name.split(" "))
# print(li)

# #10. Set Task: Remove Discharged Patients from Hospital List
# current = {"P1", "P2", "P3"}
# discharged = {"P2"}
# print(current - discharged)



#1. **Create the Product Dictionary**
crocs_products = {
       'CR101': {'name': 'Classic Clog', 'price': 3495, 'color': 'Navy Blue', 'stock': 150},
       'CR102': {'name': 'LiteRide 360 Clog', 'price': 4995, 'color': 'Graphite Grey', 'stock': 90},
       'CR103': {'name': 'Echo Clog', 'price': 5595, 'color': 'Bone White', 'stock': 65},
       'CR104': {'name': 'Bayaband Slide', 'price': 2795, 'color': 'Black/White', 'stock': 200}
   }

#2. **Access Product Details**
print("CR102 price :",crocs_products['CR102']['price'])
print("CR102 stock :",crocs_products['CR102']['stock'])

print(crocs_products.get("CR999"))


# 3. **Add a New Product**
crocs_products['CR105'] = {'name': 'Classic Platform Clog', 'price': 3995, 'color': 'Lavender', 'stock': 80}

#4. **Update Product Information**
crocs_products['CR103']['stock'] = crocs_products['CR103']['stock']-10
print(crocs_products['CR103']['stock'])

print("before price :",crocs_products['CR102']['price'])
crocs_products['CR102']['price'] = crocs_products['CR102']['price'] *1.08 
print("after price :",crocs_products['CR102']['price'])

#5. **Delete a Product**
crocs_products.pop('CR104')

#6. **Display All Product Names**
print("Product Names:")
for product in crocs_products.values():
    print(product['name'])

#7. **Calculate Total Inventory Value**
price = 0
total_value = 0
for product in crocs_products.values():
    price = product['price'] * product['stock']
    total_value += price

print("Total Inventory Value: ₹", total_value)


#8. **Check for Keys and Values**
print("Is 'CR101' a product code?", 'CR101' in crocs_products)

is_lavender = False
for product in crocs_products.values():
    if product['color'] == 'Lavender':
        is_lavender = True
        break

if is_lavender:
    print("Is there any product in 'Lavender' color? Yes")
else:
    print("Is there any product in 'Lavender' color? No")


#9. **Iterate Through the Dictionary**
print("Product Details:")
for key, values in crocs_products.items():
    print(f"Product ID: {key} → {values['name']}")


#10. **Copy and Clear Operations**
duplicate_inventory = crocs_products.copy()
print("Duplicate Inventory:", duplicate_inventory)
duplicate_inventory.clear()
print("Original Inventory:", crocs_products)
print("Duplicate Inventory:", duplicate_inventory)