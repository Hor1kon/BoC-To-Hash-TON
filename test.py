from tonpy.types import Cell


def parse_cell(cell, level=0):
    indent = "  " * level
    print(f"{indent}Cell Hash: {cell.get_hash()}")
    print(f"{indent}Cell Dump: {cell.dump()}")

    cs = cell.begin_parse()
    try:

        # Парсинг и вывод данных ячейки
        if cs.is_exhausted():
            print(f"{indent}Data: [No data available]")
        else:
            print(f"{indent}Remaining Bits: {cs.remaining_bits()}")
            while cs.remaining_bits() > 0:
                data = cs.load_bits(cs.remaining_bits())
                print(f"{indent}Data: {data}")
    except:
        print("error")
    try:
        # Рекурсивно парсим ссылки на другие ячейки, если они есть
        if cs.remaining_refs() > 0:
            for i in range(cs.remaining_refs()):
                print(f"{indent}Parsing reference {i + 1}/{cs.remaining_refs()}:")
                ref = cs.load_ref(i)
                parse_cell(ref, level + 1)
        else:
            print(f"{indent}No references.")
    except:
        print("error")

def main():
    # Замените эту строку на ваш BOC
    boc_string = "Your Boc"

    # Создание ячейки на основе BOC
    cell = Cell(boc_string)

    # Начинаем парсинг с корневой ячейки
    parse_cell(cell)


if __name__ == "__main__":
    main()
