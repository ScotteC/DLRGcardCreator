
import argparse

from os import makedirs
from os.path import exists

from data_import import data_from_isc_seminar, data_from_group_register
from create_cards import create_drsa_cards
from create_lists import create_stamp_list, create_registration_list
from courses import default_course


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DRSA-CardCreator')
    parser.add_argument('--file', type=str,
                        help='Inputfile')
    parser.add_argument('--course', type=str)
    parser.add_argument('--type', type=str, default='isc',
                        help='Type of inputfile (isc, group, json)')
    parser.add_argument('--target', type=str, help='Path for output')

    args = parser.parse_args()

    course = []
    if exists('instance/local.py'):
        from instance.local import local_course
        course = local_course()
    else:
        course = default_course

    data = []

    if args.type == 'isc':
        data = data_from_isc_seminar(args.file)
    elif args.type == 'group':
        data = data_from_group_register(args.file)

    makedirs("{path}{course}".format(path=args.target, course=course[args.course]["id"]), exist_ok=True)
    output_path = "{path}{course}".format(path=args.target, course=course[args.course]["id"])

    create_drsa_cards(data, course[args.course], output_path)
    create_stamp_list(data, output_path)
    create_registration_list(data, course[args.course], output_path)
