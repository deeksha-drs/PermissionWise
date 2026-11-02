
from permission_data import analyse_permissions

# Display the PermissionWise welcome screen
print("\n========================================")
print("             PERMISSIONWISE")
print("   See what changed. Know what it means.")
print("========================================")

# Ask the user to enter multiple permissions
permission_input = input(
    "\nEnter Android permissions separated by commas: "
)

# Convert the input into a list
permission_list = permission_input.split(",")

# Analyse all the permissions
results, unknown_permissions, duplicate_permissions = analyse_permissions(permission_list)
submitted_count = len([name for name in permission_list if name.strip()])

print("\n========== ANALYSIS SUMMARY ==========")
print("Total submitted:", submitted_count)
print("Recognised:", len(results))
print("Unknown:", len(unknown_permissions))

# Display the analysis report
print("\n========== ANALYSIS REPORT ==========")

print("Permissions found:", len(results))

for permission in results:
    print("\n------------------------------")
    print("Name:", permission["name"])
    print("Category:", permission["category"])
    print("Description:", permission["description"])
    print("Privacy Concern:", permission["privacy_concern"])
    print("Advice:", permission["user_advice"])
    print("Introduced in API:", permission.get("introduced_api", "Not available"))
    print("Protection Level:", permission.get("protection_level", "Not available"))
    print("Official Source:", permission.get("source", "Not available"))

# Handle the case where no permissions are recognised
if len(results) == 0:
    print("No known permissions were found.")

if unknown_permissions:
    print("\n========== UNKNOWN PERMISSIONS ==========")

    for permission_name in unknown_permissions:
        print("Not found:", permission_name)


if duplicate_permissions:
    print("\n========== DUPLICATE PERMISSIONS ==========")

    for permission_name in duplicate_permissions:
        print("Repeated:", permission_name)
