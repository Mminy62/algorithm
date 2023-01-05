import re
def solution(new_id):
    #1
    new_id = new_id.lower()
    #2
    new_id = re.sub(r"[~!@#$%^&*()=+\[\{\]\}:?,<>/]", "", new_id)
    #3
    while(".." in new_id):
        new_id = new_id.replace("..", ".")
    #4
    new_id = new_id.strip(".")
    #5
    if not new_id:
        new_id = "aaa" 
    #6
    elif len(new_id) > 15:
        new_id = new_id[:15]
        new_id = new_id.rstrip(".")
        
    elif len(new_id) < 3:
        new_id = new_id.ljust(3, new_id[-1])
        
    return new_id