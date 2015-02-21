class Parser(object):
    """Parses daily data from various internet sources"""

    def __init__(self, path):
        with open(path, "r") as file_in:
            file_in.readline() # skip the column headers
            self.lines = file_in.readlines()
            self.lines.reverse()

    def parse(self):
        prev_close = None
        for i in range(len(self.lines)):
            line = self.lines[i]
            parts = line.split(",")
            date = parts[0].strip()
            open_ = float(parts[1].strip())
            high = float(parts[2].strip())
            low = float(parts[3].strip())
            close = float(parts[4].strip())
            volume = int(parts[5].strip())
            if prev_close is None:
                prev_close = close
                continue
            ret = close / prev_close - 1
            target = None
            if i+1 < len(self.lines):
                target = 1.0 if float(self.lines[i+1].split(",")[4].strip()) > close else -1.0
            else:
                break
            data = {"date":date, "open":open_, "high":high, "low":low, "close":close, "volume":volume, "return":ret, "target":target}
            yield data
            prev_close = close
