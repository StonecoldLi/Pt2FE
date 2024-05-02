def process_ascii_pcd(input_file_name, output_file_name):
    with open(input_file_name, 'r') as file:
        lines = file.readlines()

    # Process header lines to match the desired format
    header = []
    data_started = False
    for line in lines:
        if line.strip() == "DATA ascii":
            header.append(line)
            break
        elif "FIELDS" in line:
            header.append("FIELDS x y z\n")
        elif "SIZE" in line:
            header.append("SIZE 4 4 4\n")
        elif "TYPE" in line:
            header.append("TYPE F F F\n")
        elif "COUNT" in line:
            header.append("COUNT 1 1 1\n")
        else:
            header.append(line)

    # Extract data lines, only taking the first three columns
    data_lines = []
    for line in lines:
        if data_started:
            parts = line.split()
            if len(parts) >= 6:  # Make sure there's enough data in the line
                data_lines.append(f"{parts[0]} {parts[1]} {parts[2]}\n")
        if line.strip() == "DATA ascii":
            data_started = True

    # Write the processed data to a new file
    with open(output_file_name, 'w') as file:
        file.writelines(header)
        file.writelines(data_lines)

def process_ascii_pcd_rgb(input_file_name, output_file_name):
    with open(input_file_name, 'r') as file:
        lines = file.readlines()

    # Process header lines to match the desired format
    header = []
    data_started = False
    for line in lines:
        if line.strip() == "DATA ascii":
            header.append(line)
            break
        elif "FIELDS" in line:
            header.append("FIELDS x y z\n")
        elif "SIZE" in line:
            header.append("SIZE 4 4 4\n")
        elif "TYPE" in line:
            header.append("TYPE F F F\n")
        elif "COUNT" in line:
            header.append("COUNT 1 1 1\n")
        else:
            header.append(line)

    # Extract data lines, only taking the first three columns
    data_lines = []
    for line in lines:
        if data_started:
            parts = line.split()
            if len(parts) >= 4:  # Make sure there's enough data in the line
                data_lines.append(f"{parts[0]} {parts[1]} {parts[2]}\n")
        if line.strip() == "DATA ascii":
            data_started = True

    # Write the processed data to a new file
    with open(output_file_name, 'w') as file:
        file.writelines(header)
        file.writelines(data_lines)