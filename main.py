from parsers.wiki_books import parse as wiki_books_parse
from writers.tmx import write as tmx_write

parsed_wiki_books = wiki_books_parse()
print(f"Wiki books :: {len(parsed_wiki_books)} entries")
tmx_write(parsed_wiki_books)
