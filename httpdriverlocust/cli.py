#! python3
# -*- encoding: utf-8 -*-
'''
Current module: httpdriverlocust.cli

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:     luokefeng@163.com
    RCS:      httpdriverlocust.cli,  v1.0 2018年10月23日
    FROM:   2018年10月23日
********************************************************************
======================================================================

Provide a function for the automation test

'''


import argparse, sys
from rtsf.p_applog import color_print,logger
from rtsf.p_executer import TestRunner

from httpdriverlocust.__about__ import __version__
from httpdriverlocust import locusts
    
def main_hrun():
    """ parse command line options and run commands."""
    
    parser = argparse.ArgumentParser(description="Tools for http(s) test. Base on rtsf.")
            
    parser.add_argument(
        '--log-level', default='INFO',
        help="Specify logging level, default is INFO.")
    
    parser.add_argument(
        '--log-file',
        help="Write logs to specified file path.")
    
    parser.add_argument(
        'case_file', 
        help="yaml testcase file")
    
    color_print("httpdriver {}".format(__version__), "GREEN")
    args = parser.parse_args()
    logger.setup_logger(args.log_level, args.log_file)    
    
    runner = TestRunner(runner = Driver).run(args.case_file)
    html_report = runner.gen_html_report()
    color_print("report: {}".format(html_report))

def main_locust():
    """ Performance test with locust: parse command line options and run commands.
    """
    logger.setup_logger("INFO")

    sys.argv[0] = 'locust'
    if len(sys.argv) == 1:
        sys.argv.extend(["-h"])

    if sys.argv[1] in ["-h", "--help", "-V", "--version"]:
        locusts.main()
        sys.exit(0)

    try:
        testcase_index = sys.argv.index('-f') + 1
        assert testcase_index < len(sys.argv)
    except (ValueError, AssertionError):
        logger.log_error("Testcase file is not specified, exit.")
        sys.exit(1)

    testcase_file_path = sys.argv[testcase_index]
    sys.argv[testcase_index] = locusts.parse_locustfile(testcase_file_path)

    if "--processes" in sys.argv:
        """ locusts -f locustfile.py --processes 4
        """
        if "--no-web" in sys.argv:
            logger.log_error("conflict parameter args: --processes & --no-web. \nexit.")
            sys.exit(1)

        processes_index = sys.argv.index('--processes')

        processes_count_index = processes_index + 1

        if processes_count_index >= len(sys.argv):
            """ do not specify processes count explicitly
                locusts -f locustfile.py --processes
            """
            processes_count = multiprocessing.cpu_count()
            logger.log_warning("processes count not specified, use {} by default.".format(processes_count))
        else:
            try:
                """ locusts -f locustfile.py --processes 4 """
                processes_count = int(sys.argv[processes_count_index])
                sys.argv.pop(processes_count_index)
            except ValueError:
                """ locusts -f locustfile.py --processes -P 8888 """
                processes_count = multiprocessing.cpu_count()
                logger.log_warning("processes count not specified, use {} by default.".format(processes_count))

        sys.argv.pop(processes_index)
        locusts.run_locusts_with_processes(sys.argv, processes_count)
    else:
        locusts.main()