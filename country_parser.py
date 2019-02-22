#!/usr/bin/env python

import argparse
import json
import os
import pprint


class CountryParser:

    STRING_TEMPLATE = '{}: {}'
    COUNTRY_KEY = 'country'

    def __init__(self, data_dir):
        self.data_dir = os.path.abspath(data_dir)
        self.data = None
        self.sorting_key = None

    def _custom_sort(self, element):
        return int(element[self.sorting_key])

    def _alphabet_sort(self, element):
        return element[self.COUNTRY_KEY]

    def load_category(self, category):
        # Load content of a JSON file to memory.
        for root, dirs, files in os.walk(self.data_dir):
            for filename in files:
                if category.lower() in filename:
                    with open(os.path.join(root, filename)) as f:
                        self.data = json.loads(f.read())

        # Determine sorting key
        self.sorting_key = [k for k in self.data[0].keys() if k != self.COUNTRY_KEY][0]

        # Sanitaze json - replace None values with '0' for consistency
        for entry in self.data:
            if entry[self.sorting_key] is None:
                entry[self.sorting_key] = '0'

    def highest(self):
        highest = sorted(self.data, key=self._custom_sort)[-1]
        return self.STRING_TEMPLATE.format(highest[self.COUNTRY_KEY], highest[self.sorting_key])

    def lowest(self):
        lowest = sorted(self.data, key=self._custom_sort)[0]
        return self.STRING_TEMPLATE.format(lowest[self.COUNTRY_KEY], lowest[self.sorting_key])

    def get_value_for(self, country):
        for entry in self.data:
            if entry[self.COUNTRY_KEY] == country:
                return self.STRING_TEMPLATE.format(entry[self.COUNTRY_KEY], entry[self.sorting_key])

    def all(self):
        return sorted(self.data, key=self._alphabet_sort)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse country data from JSON files')
    parser.add_argument('--category', action='store', required=True,
                        help='This will determine JSON file that will be parsed')
    parser.add_argument('--data-dir', action='store', required=False, default='example_data',
                        help='Path to a directory with JSON files containing raw country data')
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--highest', action='store_true',
                        help='Print the country that has the highest value in the category')
    action.add_argument('--lowest', action='store_true',
                        help='Print the country that has the lowest value in the category')
    action.add_argument('--all', action='store_true',
                        help='Print all countries and their values')
    action.add_argument('--get', action='store', metavar='COUNTRY',
                        help='Print the value for a specified country')
    args = parser.parse_args()

    cp = CountryParser(data_dir=args.data_dir)
    cp.load_category(category=args.category)

    if args.highest:
        print(cp.highest())
    elif args.lowest:
        print(cp.lowest())
    elif args.all:
        pprint.pprint(cp.all())
    else:
        print(cp.get_value_for(args.get))
