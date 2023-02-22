import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def __init__(self):
        self.statuses_count = None

    def open_spider(self, spider):
        self.statuses_count = defaultdict(int)

    def process_item(self, item, spider):
        pep_status = item['status']
        self.statuses_count[pep_status] += 1
        return item

    def close_spider(self, spider):
        pattern = '%m-%d-%Y_%H-%M-%S'
        file_name = f'status_summary_{datetime.now().strftime(pattern)}.csv'
        path = Path(BASE_DIR, 'results')
        results = list(self.statuses_count.items())
        results.append(('Total', sum(self.statuses_count.values())))
        with open(Path(path, file_name), 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix', quoting=csv.QUOTE_MINIMAL)
            f.write('Статус, Количество\n')
            writer.writerows(results)
