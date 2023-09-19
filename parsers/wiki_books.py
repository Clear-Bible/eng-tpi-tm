import os
import re

PATH = "data/wiki-books"


def parse():
    """Parse wiki books data return a list of lists"""
    print("Parsing wiki books... !!")
    entries = []
    files = os.listdir(PATH)
    for file in files:
        print(f"Parsing {file}...")
        file_data = open(f"{PATH}/{file}", "r")
        lines = file_data.readlines()
        cleaned_lines = clean_lines(lines)
        for cleaned_line in cleaned_lines:
            parts = cleaned_line.split("-")
            # print(parts)
            eng_parts = clean_parts(parts[0].strip().split(","))
            tpi_parts = clean_parts(parts[1].strip().replace(";", ",").split(","))
            # print(f"{eng_parts} -- {tpi_parts}")
            if len(eng_parts) == 1 and len(tpi_parts) == 1:
                entries.append([eng_parts[0], tpi_parts[0]])
            if len(eng_parts) > 1 and len(tpi_parts) == 1:
                for eng_part in eng_parts:
                    entries.append([eng_part, tpi_parts[0]])
            if len(eng_parts) == 1 and len(tpi_parts) > 1:
                for tpi_part in tpi_parts:
                    # if eng_parts[0] == "antiseptic":
                    # print(tpi_part)

                    entries.append([eng_parts[0], tpi_part])

    for entry in entries:
        print(entry)
    return entries


def clean_lines(dirty_lines):
    cleaned_lines = []

    for dirty_line in dirty_lines:
        cleaned_line = dirty_line.strip()
        if (
            cleaned_line != ""
            and not cleaned_line.startswith(":")
            and not cleaned_line.startswith("=")
        ):
            cleaned_lines.append(cleaned_line)

    return cleaned_lines


def clean_parts(dirty_parts):
    cleaned_parts = []

    for dirty_part in dirty_parts:
        stripped_part = dirty_part.strip()
        cleaned_part = re.sub(r"[\(\[].*?[\)\]]", "", stripped_part)
        if cleaned_part != "":
            cleaned_parts.append(cleaned_part)

    return cleaned_parts
