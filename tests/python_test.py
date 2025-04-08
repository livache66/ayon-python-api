import os
import sys
sys.path.append('../AYON-PYTHON-API')
import ayon_api

# Set up the connection
os.environ["AYON_SERVER_URL"] = "http://192.168.80.20:5000/"
os.environ["AYON_API_KEY"] = "a7735299a85b368cc30a537297644a69ac6dc58c5d025c2105f1f509a215ad54"
con = ayon_api.get_server_api_connection()

# Step 1: Get the project
project_name = "ayontest"  # Replace with your project name
projects = con.get_projects()
project = next((p for p in projects if p["name"] == project_name), None)

if not project:
    print(f"Project '{project_name}' not found.")
else:
    print(f"Found project: {project['name']}")

id=con.get_version_by_id('ayontest','80468a4b096b11f0929de848b8c82000', fields=['version'])
first_value = next(iter(id.values()))  # Get the first value from the dictionary
print("Version:", first_value)