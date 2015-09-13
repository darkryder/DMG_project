NAME = "final_clean.py"
OUTPUT = "final_clean_updated.py"

with open(NAME, 'r') as infile, open(OUTPUT, 'w') as outfile:
    for inline in infile.readlines():
        if not ("add_info" in inline and "VAR_" in inline):
            outfile.write(inline)
            continue
        first_index = inline.index("add_info(") + len("add_info(")
        end_index = first_index + inline[first_index:].index(",")
        value = int(inline[6:10])
        outline = inline[:first_index] + str(value) + inline[end_index:]
        print "changing|", inline.strip(), "| into |", outline.strip(), "|"
        outfile.write(outline)
