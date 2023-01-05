import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r"[~!@#$%^&*()=+\[\{\]\}:?,<>/]", "", new_id)
    while(".." in new_id):
        new_id = new_id.replace("..", ".")
    new_id = new_id.strip(".")
    
    if not new_id:
        new_id = "aaa"
        
    elif len(new_id) > 15:
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")
        
    elif len(new_id) < 3:
        new_id = new_id.ljust(3, new_id[-1])
        
    return new_id