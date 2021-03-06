import time
import unittest
import click

from app import create_app
from config import config
from config import config_dict


application = create_app(config) 

# production : debug = False, Testing = False,
# Develope : debug = True, 
# Testing : ENV로 구분 후 테스트.py 실행
# Develope : debug = True, 개발
"""test_mode"""
@application.cli.command("test_mode")
@click.argument("test_names_tuple", nargs=-1)  # nargs -1 로 해야 문자열로 받음 아니면 문자로 받음
def test(test_names_tuple):

    application = create_app(config_dict['testing'])
    test_dir = "tests"

    print(
         application.config["ENV"],
        "|- - - Config Check - - - -|\n"
        " |- - - DEBUG : ", application.config["DEBUG"], "- - -|"
        "\n |- - - TESTING : ", application.config["TESTING"], " - -|"
        "\n ┗ - - - - - - - - - - - - -┛\n"
    )


    try:
        # tests 폴더에 없는 요소가 들어오면 에러처리해야함 현재는 비었는지만 처리중 
        # if test_names_tuple in testfolder:
        if test_names_tuple:
            for index in range(len(test_names_tuple)):
                time.sleep(2)
                print(">>> mode: test_mode \n>>> test name : '{}'".format(test_names_tuple[index]))
                name_to_test_suite = unittest.TestLoader().discover(
                    test_dir, test_names_tuple[index]
                )
                unittest.TextTestRunner(verbosity=1).run(name_to_test_suite)
        else:
            raise ValueError

    
    except ValueError:
        print("Error, you must be 'flask test_mode a.py b.py ...' \n")
    

