import csv
import hashlib
import os


class CsvReader(object):
    """
    Đọc dữ liệu dạng csv
    """

    @classmethod
    def from_abs_path(cls, file_path):
        csv = CsvReader("")
        csv.file_name = file_path
        return csv

    def get_md5(self):
        hasher = hashlib.md5()
        with open(self.file_name, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def __init__(self, csv_file_name):
        self.file_name = os.path.dirname(__file__) + "/data/" + csv_file_name

    def read_first_column(self):
        sentence = []
        for v in self.read():
            if len(v):
                sentence.append(v[0])
        return sentence

    def read(self):
        import codecs
        sentence = []
        f = codecs.open(self.file_name, 'r', 'utf8')
        try:
            reader = csv.reader(f, delimiter='#')
            for row in reader:
                if len(row) > 0:
                    sentence.append(row)
        finally:
            f.close()
        return sentence
