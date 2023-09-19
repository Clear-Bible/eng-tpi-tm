import lxml.etree as etree


def write(parsed_entries):
    print("Writing TMX file... !!")
    tmx_root = create_tmx_root()
    tmx_header = create_tmx_header()
    tmx_body = etree.Element("body")
    tmx_root.append(tmx_header)
    tmx_root.append(tmx_body)

    for entry in parsed_entries:
        tu = create_translation_unit()
        eng_tuv = create_translation_variant(entry[0], "en")
        tpi_tuv = create_translation_variant(entry[1], "tpi")
        tu.append(eng_tuv)
        tu.append(tpi_tuv)
        tmx_body.append(tu)

    stringified_tmx = etree.tostring(
        tmx_root, xml_declaration=True, encoding="UTF-8", pretty_print=True
    )

    tree = etree.ElementTree(tmx_root)
    tree.write("output.xml", xml_declaration=True, encoding="UTF-8", pretty_print=True)
    # print(stringified_tmx)
    return stringified_tmx


def create_tmx_root():
    tmx_root = etree.Element("tmx")
    tmx_root.attrib["version"] = "1.4"
    return tmx_root


def create_tmx_header():
    tmx_header = etree.Element("header")
    tmx_header.attrib["segtype"] = "word"
    tmx_header.attrib["srclang"] = "en_US"
    tmx_header.attrib["datatype"] = "plaintext"
    return tmx_header


def create_translation_unit():
    tu = etree.Element("tu")
    return tu


def create_translation_variant(text, lang):
    tuv = etree.Element("tuv")
    tuv.set("lang", lang)
    seg = etree.Element("seg")
    seg.text = text
    tuv.append(seg)
    return tuv
