from copy_static import copy_static
from generator import generate_page, generate_pages_recursive

def main():
    static_path = "static"
    public_path = "public"
    content_path = "content"
    template_path = "template.html"

    copy_static(static_path, public_path)

    generate_pages_recursive(content_path, template_path, public_path)



if __name__ == "__main__":
    main()
