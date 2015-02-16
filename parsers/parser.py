class Parser(object):
    """Abstract class for parsing daily data from various internet sources"""

    def __init__(self, path):
        with open(path, "r") as file_in:
            file_in.readline() # skip the column headers
            self.lines = reversed(file_in.readlines())
            self.prev_data = None

    def parse(self):
        for line in self.lines:
            parts = line.split(",")
            date = parts[0].strip()
            open_ = float(parts[1].strip())
            high = float(parts[2].strip())
            low = float(parts[3].strip())
            close = float(parts[4].strip())
            volume = int(parts[5].strip())
            data = {"date":date, "open":open_, "high":high, "low":low, "close":close, "volume":volume}
            if self.prev_data is not None:
                data["return"] = (close / self.prev_data["close"] - 1) * 100
                yield data
            self.prev_data = data
