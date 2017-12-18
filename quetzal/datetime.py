class DateTime:
    def __init__(self, date, hour, minute):
        self.date = date
        self.hour = hour
        self.minute = minute

    def get_date(self):
        return self.date

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def __lt__(self, other):
        return (self.date < other.date) and \
               (self.hour < other.hour) and \
               (self.minute < other.minute)

    def __str__(self):
        return "{} {} {}".format(self.date, self.hour, self.minute)
