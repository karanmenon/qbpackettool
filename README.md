# qbpackettool
A tool to generate new, randomized Quiz Bowl packets from existing source packets in the form of Microsoft Word documents.

The generated packets follow a category distribution set by the user and as much as possible ensure that 
not two questions of the same category are located consecutively in the new packets.

Unlike most Quiz Bowl packets (included the source packets), where all the tossup questions are located before all the bonus questions,
each bonus question is placed directly after each tossup.

Portions of tossups questions which are worth more points (power portions) are bolded as per standard quiz bowl procedure in generated packets.

The program only works if source files are formatted in a certain way. Check the word document in the packets folder to see how it is formatted.
1. Power portions should be separated from the rest of tossups by "(*)"
2. All tossups should be numbered and placed first, followed by the heading "Bonuses" and all the bonus questions after.
3. Every tossup and bonus question should have a tag at its end that specifies the category and the subcategory. Subcategory names are up to your discretion
but here are the category names and their associated full names. Tags should be in the format <CATEGORY, SUBCATEGORY>

SCI = science
HIST = hist
LIT = literature
FA = fine arts
RMPSS = religion, mythology, philosophy, and social sciences
GEO = geography
CE = current events
MISC. = miscellaneous
TRASH = pop culture

Directions:
1. git clone the repository
2. Open the file packetgen.py
3. Get the address of the "packets" folder located within the the qbpackettool folder and set folder_address to that address. Note that the current address is for the folder on my laptop, and uses MacOS addressing.
4. Go through the dist and bonus_dist dictionaries and set the desired number of tossups (dist) and bonuses (bonus_dist) you want for each category.
5. Format the source packets given the guidelines above and put them in the packets folder.
6. Run the python code through your terminal using the command "python packetgen.py" or through your IDE. The newly generated packets will be in the generated_packets folder in qbpackettool.
