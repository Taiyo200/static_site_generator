import sys
from copy_static import copy_static
from generator import generate_page, generate_pages_recursive

def main():
    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
        if not base_path.endswith("/"):
            base_path += "/"

    static_path = "static"
    output_path = "docs" 
    content_path = "content"
    template_path = "template.html"

    copy_static(static_path, output_path)
    generate_pages_recursive(content_path, template_path, output_path, base_path)



if __name__ == "__main__":
    main()
