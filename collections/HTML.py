# Method names:
# renderContents -> encode_contents
# replaceWith -> replace_with
# replaceWithChildren -> unwrap
# findAll -> find_all
# findAllNext -> find_all_next
# findAllPrevious -> find_all_previous
# findNext -> find_next
# findNextSibling -> find_next_sibling
# findNextSiblings -> find_next_siblings
# findParent -> find_parent
# findParents -> find_parents
# findPrevious -> find_previous
# findPreviousSibling -> find_previous_sibling
# findPreviousSiblings -> find_previous_siblings
# getText -> get_text
# nextSibling -> next_sibling
# previousSibling -> previous_sibling


import requests
from bs4 import BeautifulSoup

base_url = 'https://wyborcza.pl/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "xml")

for story_heading in soup.find_all("news"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())