from lib.core.runner import Runner
from lib.core.timer import Timer
from lib.utils.argparser import parse_args
from lib.utils.logger import Logger


def main():
    args = parse_args()
    runner = Runner(show_time=args.time)
    logger = Logger()

    if args.time:
        timer = Timer()
        timer.start()

    if args.all:
        for day_number in range(1, 26):
            runner.run_day(day_number, args.part)
    else:
        runner.run_day(args.day, args.part)

    if args.time:
        timing = timer.stop()
        logger.print_timing("Total execution time", timing.elapsed)


if __name__ == "__main__":
    main()
