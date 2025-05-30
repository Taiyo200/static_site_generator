import os
from markdown_to_html import markdown_to_html_node


def extract_title(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("Markdown does not contain an H1 title")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown_content = f.read()
    
    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    title = extract_title(markdown_content)

    result = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(result)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        full_entry_path = os.path.join(dir_path_content, entry)
        dest_entry_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(full_entry_path):
            generate_pages_recursive(full_entry_path, template_path, dest_entry_path)
        elif entry.endswith(".md"):
            dest_html_path = dest_entry_path.replace(".md", ".html")
            print(f"Generating HTML page from {full_entry_path} to {dest_html_path}")
            generate_page(full_entry_path, template_path, dest_html_path)