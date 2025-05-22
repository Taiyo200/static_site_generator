from htmlnode import LeafNode, ParentNode
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from text_helpers import text_to_children 

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.TEXT:
            block = block.replace("\n", " ")
            children = text_to_children(block)
            html_nodes.append(ParentNode("p", children))

        elif block_type == BlockType.HEADING:
            level = len(block.split(" ")[0]) 
            content = block[level+1:].strip()
            children = text_to_children(content)
            html_nodes.append(ParentNode(f"h{level}", children))

        elif block_type == BlockType.CODE:
            lines = block.split("\n")
            code_lines = lines[1:-1]
            code_content = "\n".join(code_lines)
    
            if not code_content.endswith("\n"):
                code_content += "\n"
    
            code_node = LeafNode("code", code_content)
            html_nodes.append(ParentNode("pre", [code_node]))

        elif block_type == BlockType.QUOTE:
            quote_content = block.lstrip(">").strip()
            children = text_to_children(quote_content)
            html_nodes.append(ParentNode("blockquote", children))

        elif block_type == BlockType.UNORDERED_LIST:
            items = block.split("\n")
            list_nodes = []
            for item in items:
                content = item.lstrip("-").strip()
                children = text_to_children(content)
                list_nodes.append(ParentNode("li", children))
            html_nodes.append(ParentNode("ul", list_nodes))

        elif block_type == BlockType.ORDERED_LIST:
            items = block.split("\n")
            list_nodes = []
            for item in items:
                content = item[item.find(".")+1:].strip()
                children = text_to_children(content)
                list_nodes.append(ParentNode("li", children))
            html_nodes.append(ParentNode("ol", list_nodes))

    return ParentNode("div", html_nodes)