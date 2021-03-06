from cbapi.defense import *
from lrjob import run_liveresponse
from cbapi.example_helpers import get_cb_defense_object, build_cli_parser


def main():
    parser = build_cli_parser("Cb Defense Live Response example")
    parser.add_argument("sensorid", nargs=1)
    args = parser.parse_args()

    c = get_cb_defense_object(args)

    sensor = c.select(Device, int(args.sensorid[0]))
    run_liveresponse(sensor.lr_session())


if __name__ == '__main__':
    main()