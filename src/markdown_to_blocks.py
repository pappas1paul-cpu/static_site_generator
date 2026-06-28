from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block !="":
            cleaned_blocks.append(stripped_block)
    return cleaned_blocks

def block_to_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    if all(line.startswith(">") or line.startswith("> ") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    is_ordered = True
    for i, line in enumerate(lines):
        expected_start = f"{i+1}. "
        if not line.startswith(expected_start):
            is_ordered = False
            break
    if is_ordered == True and len(lines) > 0 :
        return BlockType.ORDERED_LIST 
    return BlockType.PARAGRAPH