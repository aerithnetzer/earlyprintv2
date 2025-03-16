import sys
import xmltodict
import json


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input.xml>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        input_file_name = input_file.split("/")[-1]
        with open(input_file, "r") as f:
            xml_str = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    try:
        data_dict = xmltodict.parse(xml_str)
    except Exception as e:
        print(f"Error parsing XML: {e}")
        sys.exit(1)

    json_str = json.dumps(data_dict, indent=2)
    try:
        with open(f"{input_file_name}.json", "w") as f:
            f.write(json_str)
        print(json_str)
    except Exception as e:
        print(f"Error writing JSON file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
