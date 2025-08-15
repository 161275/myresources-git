import datetime

today = datetime.datetime.today()

inp_str = ["noun1", "verb1", "noun2", "verb2"]
out_str = []

def get_iput(word_type: str):
    user_ip = (input(f"enter a {word_type}:"))
    return user_ip
    
    
        

for i in inp_str:
    out = get_iput(i)
    if not out.isalpha():
        print("enter correct input")
        exit(1)
    else:
        out_str.append(out)


# adj = get_iput("adjctive")
# noun1 = get_iput("noun1")
# verb1 = get_iput("verb1")
# noun2 = get_iput("noun2")
# verb2 = get_iput("verb2")



story1 = f"""
One sunny day, {out[0]} and {out[2]} decided to {out[1]} together. 
They thought it would be easy, but halfway through, 
something unexpected made them {out[3]}. 
In the end, they both laughed, knowing that adventures are always better when shared.
"""
story2 = f"""
second day, {out[0]} and {out[2]} decided to {out[2]} together. 
They thought it would be easy, but halfway through, 
something unexpected made them {out[2]}. 
In the end, they both laughed, knowing that adventures are always better when shared.
"""
story = [story1, story2]
print(story[1])
print(f"{today:%B %d, %Y}")
