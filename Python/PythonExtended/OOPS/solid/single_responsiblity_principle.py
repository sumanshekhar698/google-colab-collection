from pathlib import Path

class ReportBad:
    # rows is a list of int
    def __init__(self, rows):
        self.rows = rows

    # sum of nums
    def total(self):# buisness
        return sum(self.rows)

    def to_html(self):# presentation
        return f"<p> {self.total()}</p>"

    def save(self,p):# persistence
        Path(p).write_text(self.to_html())



class Report:
    # rows is a list of int
    def __init__(self, rows):
        self.rows = rows

        # sum of nums
    def total(self):# buisness
        return sum(self.rows)


class HTMLFormatter:
    def format(self, text):
        return f"<p> {text}</p>"

class FileWriter:
    def save(self, p, text):
        Path(p).write_text(text)



nums = [55,21,22,20]
report = Report(nums)
text  = HTMLFormatter().format(report.total())
FileWriter( ).save(".report.html",text)




# FileWriter( ).save(".report.html",HTMLFormatter().format(Report(nums).total()))