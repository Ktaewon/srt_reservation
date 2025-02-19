""" Quickstart script for InstaPy usage """

# imports
from srt_reservation.main import SRT
from srt_reservation.util import parse_cli_args


if __name__ == "__main__":
    cli_args = parse_cli_args()

    login_id = cli_args.user
    login_psw = cli_args.psw
    dpt_stn = cli_args.dpt
    arr_stn = cli_args.arr
    dpt_dt = cli_args.dt
    dpt_tm = cli_args.tm

    num_trains_to_check = cli_args.num
    want_reserve = cli_args.reserve
    
    # sms service
    sms_service = cli_args.sms
    
    screen_saver_enable = cli_args.scr
    
    # telegram
    tele_chat_id = cli_args.tele_chat_id
    tele_token = cli_args.tele_token

    srt = SRT(dpt_stn, arr_stn, dpt_dt, dpt_tm, num_trains_to_check, want_reserve, sms_service, screen_saver_enable, tele_chat_id, tele_token)
    srt.run(login_id, login_psw)