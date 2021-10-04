import os
# locates drives in pc
def drives_in_pc():
    p_s_d = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    my_osDrive_list = []
    for each_drive in p_s_d:
        drive_name = each_drive + ':\\'
        if os.path.exists(drive_name):
            my_osDrive_list.append(drive_name)
    return my_osDrive_list
