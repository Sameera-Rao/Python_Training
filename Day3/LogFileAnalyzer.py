keywords = ["class","objects","attributes","methods","inheritance","file","loops","try","except"]

def analyze_log_file(input_file, output_file):
    keyword_count = {keyword: 0 for keyword in keywords}

    try:
        with open(input_file, "r") as file:
            for line in file:
                for keyword in keywords:
                    if keyword in line:
                        keyword_count[keyword] += 1

        with open(output_file, "w") as out:
            out.write("Log File Analysis Report\n")
            for keyword, count in keyword_count.items():
                out.write(f"{keyword}: {count}\n")

        print("Log file analysis completed successfully.")

    except FileNotFoundError:
        print("Input log file not found.")

input_log = "input_file.txt"
output_report = "output_file.txt"

analyze_log_file(input_log, output_report)
