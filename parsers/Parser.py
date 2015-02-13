class Parser(object):
    """Abstract class for parsing daily data from various internet sources"""

    def __init__(self, path):
        with open(path, "r") as file_in:
            file_in.readline() # skip the column headers
            self.lines = reversed(file_in.readlines())

    def parse(self):
        for line in self.lines:
            parts = line.split(",")
            date = parts[0].strip()
            open_ = float(parts[1].strip())
            high = float(parts[2].strip())
            low = float(parts[3].strip())
            close = float(parts[4].strip())
            volume = int(parts[5].strip())
            yield {"date":date, "open":open_, "high":high, "low":low, "close":close, "volume":volume}
