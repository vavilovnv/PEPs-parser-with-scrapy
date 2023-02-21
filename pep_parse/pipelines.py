import csv
import os.path
from collections import defaultdict
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent

STATUSES_COUNT = defaultdict(int)
RESULTS = []


class PepParsePipeline:

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        pep_status = item['status']
        STATUSES_COUNT[pep_status] += 1
        return item

    def close_spider(self, spider):
        pattern = '%m-%d-%Y_%H-%M-%S'
        file_name = f'status_summary_{datetime.now().strftime(pattern)}.csv'
        path = f'{BASE_DIR}/results/'
        RESULTS.extend(STATUSES_COUNT.items())
        RESULTS.append(('Total', sum(STATUSES_COUNT.values())))
        with open(os.path.join(path, file_name), 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            f.write('Статус, Количество\n')
            writer.writerows(RESULTS)
