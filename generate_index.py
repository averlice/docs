import os

def update_index():
    # Identify directories to include (excluding hidden and system folders)
    folders = [f for f in os.listdir('.') if os.path.isdir(f) and not f.startswith('.') and f != '.github']
    folders.sort()

    # Create the HTML list items
    list_items = []
    for f in folders:
        list_items.append(f'                <li><a href="{f}/">{f}/</a></li>')
    
    new_content = "\n".join(list_items)

    # Read the current index.html
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: index.html not found.")
        return

    # Define the markers
    start_marker = "<!-- FOLDER_LIST_START -->"
    end_marker = "<!-- FOLDER_LIST_END -->"

    if start_marker in content and end_marker in content:
        # Replace the content between markers
        start_idx = content.find(start_marker) + len(start_marker)
        end_idx = content.find(end_marker)
        
        # Ensure we maintain the structure and spacing
        updated_content = content[:start_idx] + "\n" + new_content + "\n                " + content[end_idx:]
        
        # Write back to index.html
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print("index.html updated successfully.")
    else:
        print("Markers not found in index.html.")

if __name__ == "__main__":
    update_index()