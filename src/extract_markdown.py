import re


def extract_markdown_images(text):
    has_image = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return has_image
def extract_markdown_links(text):
    has_link = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return has_link

