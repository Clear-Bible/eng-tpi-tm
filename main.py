from parsers.wiki_books import parse as wiki_books_parse
from writers.tmx import write as tmx_write

parsed_wiki_books = wiki_books_parse()
tmx_data = tmx_write(parsed_wiki_books)

# output_file = open("output.xml", "w")
# output_file.write(tmx_data)
# output_file.close()
