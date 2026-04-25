# Write a simple Python script for printing the names, affiliation, and the name of the genes you love most, and the name of the organism bearing the gene. 
# The final output should be something like; 
# Hi, my name is Adewale Ogunleye, a researcher at the University of Tübingen. My favorite gene is lexA in Escherichia coli.”

# This script prints my name, role, affiliation, favorite gene,
# and the organism in which the gene is found.
# I stored each piece of information in variables
# and used an f-string to format the final output.

name = "Akinyemi Olanrewaju Akinwale"
role = "Bioinformatics Intern"
affiliation = "HackBio"
gene = "wbeO"
organism = "Vibrio cholerae"

print(
    f"My name is {name}. I am a {role} at {affiliation}."
    f"\nMy favorite gene is {gene} found in \033[3m{organism}\033[0m."
    )



