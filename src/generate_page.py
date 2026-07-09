import os
from markdown_to_html import markdown_to_html_node 
from extract_title import extract_title

def generate_page(from_path, template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    
    with open(from_path, "r", encoding="utf-8") as stream:
        print("reading md")
        md_content = stream.read()
    with open(template_path, "r", encoding="utf-8") as stream:
        print("reading template")
        template_content = stream.read()
    html_node = markdown_to_html_node(md_content)
    html_content = html_node.to_html()
    title = extract_title(md_content)
    html = template_content.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_content)
    dest_dir = os.path.dirname(dest_path)
    
    if dest_dir:
        os.makedirs(dest_dir, exist_ok = True)
    with open(dest_path, "w", encoding="utf-8") as stream:
        stream.write(html)